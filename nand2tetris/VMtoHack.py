# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 11:20:52 2018

@author: vcian
"""

import os

class Parser(object):
    def __init__(self,filename):
#        Opens the input file/stream and gets ready to parse it
        self.file = open(filename)
        self.raw_command = ""
        self.command = []
        self.filename = filename.strip(".vm")
        self.command_no = 0
        
        self.hasMoreCommands = True
        
    def advance(self):
#        Reads the next command from the input and makes it the current command. Should be called only if hasMoreCommands() is true. Initially there is no current command.
        self.raw_command = self.file.readline()
        if self.raw_command == '':
            self.hasMoreCommands = False
            return
        self.command = self.raw_command.strip().split()
        if ((self.command == []) or (self.command[0].startswith("//"))):
            self.advance()
        self.command_no += 1

    def commandType(self):
        if self.command[0] in ["push","pop","label","goto","if-goto","function","call","return"]:
            return self.command[0]
        if self.command[0] in ["eq","lt","gt","add","sub","neg","and","or","not"]:
            return "arithmetic"
        else:
            raise Exception('{} is not a valid command.'.format(self.command[0]))

    def arg1(self):
#        Returns the first argument of the current command. In the case of C_ARITHMETIC, the command itself (add, sub, etc.) is returned. Should not be called if the current command is C_RETURN.
        if self.commandType() == "arithmetic":
            return self.command[0]
        return self.command[1]

    def arg2(self):
#        Returns the second argument of the current command. Should be called only if the current command is C_PUSH, C_POP, C_FUNCTION, or C_CALL
        return self.command[2]
    
class CodeWriter(object):   
    def __init__(self):
        self.current_file = None
        self.current_parser = None
        self.current_function = ""
        self.labels = []
        self.instances = {}
        
    def setFileName(self,new_parser):
#        Informs the code writer that the translation of a new VM file is started. 
        self.current_parser = new_parser
        self.current_file = self.current_parser.filename
        print("Parsing {}".format(self.current_file))
        
    def setDestName(self,name):
        self.filename = name.strip(".vm") + ".asm"
        self.file = open("temp.txt",'w')
        
    def writeDebug(self):
        self.file.write('\n //' + self.current_parser.raw_command + '\n')
        
    def writeInit(self,is_directory = False):
#        Writes the assembly code that effects the VM initialization (also called bootstrap 
#        code). This code should be placed in the ROM beginning in address 0x0000.
#
#        By convention, this code is:
#           SP=256          // initialize the stack pointer to 0x0100
#           call Sys.init   // invoke Sys.init
        
        if is_directory:
            self.file.write("""@256
                                D = A
                                @SP
                                M = D
                                @$INIT
                                0;JMP
                                
                                ($COMP)
                                @SP
                                A = M
                                M = -1
                                @SP
                                M = M + 1
                                @$TMP$$COMP
                                A = M
                                0;JMP
                                
                                ($INIT)
                                """)
            self.writeCall("Sys.init","0")
        else:
            self.file.write("""@256
                                D = A
                                @SP
                                M = D
                                @$INIT
                                0;JMP
                                
                                ($COMP)
                                @SP
                                A = M
                                M = -1
                                @SP
                                M = M + 1
                                @$TMP$$COMP
                                A = M
                                0;JMP
                                
                                ($INIT)
                                """)
        
    def writeLabel(self,label):
#        Create the globally unique symbol current_function:label.
        for char in label:
            if char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_:.":
                raise Exception('{} is not a valid label.'.format(label))
        current_label = "{}${}".format(self.current_function,label)
        if current_label in self.labels:
            raise Exception('{} is already defined.'.format(current_label))
        else:
            self.labels.append(current_label)
            self.file.write("(" + current_label + ")" + "\n")
        
    def writeGoto(self,label):
#        Jump to label.
        current_label = "{}${}".format(self.current_function,label)
        self.file.write("""@{}
                            0;JMP
                            """.format(current_label))
    
    def writeIf(self,label):
#        If the top entry of the stack is not zero, jump to label.
        current_label = "{}${}".format(self.current_function,label)
        self.file.write("""@SP
                           AM = M - 1
                           D = M
                           @{}
                           D;JNE
                           """.format(current_label))
    
    def writeCall(self,function,numArgs):
#        Call function with numArgs arguments.
#        Store (respectively) a return address and the calling function's pointers, then initialize the new function's pointers.
        if function not in self.instances:
            self.instances[function] = 0
        self.instances[function] += 1
        self.file.write("""@{function}$$RET{no} // Push return address
                           D = A
                           @SP
                           A = M
                           M = D
                           @SP
                           M = M + 1
                           
                           @LCL                 // Push LCL
                           D = M 
                           @SP
                           A = M
                           M = D
                           @SP
                           M = M + 1
                           
                           @ARG                 // Push ARG
                           D = M
                           @SP
                           A = M
                           M = D
                           @SP
                           M = M + 1
                           
                           @THIS                // Push THIS
                           D = M
                           @SP
                           A = M
                           M = D
                           @SP
                           M = M + 1
                           
                           @THAT                // Push THAT
                           D = M
                           @SP
                           A = M
                           M = D
                           @SP
                           M = M + 1
                           
                           @{numArgs}           // Initialize ARG = SP - (5 + numArgs)
                           D = A
                           @5
                           D = D + A
                           @SP
                           D = M - D
                           @ARG
                           M = D
                           
                           @SP                 // Initialize LCL = SP
                           D = M
                           @LCL
                           M = D
                           
                           @{function}        // Jump to function
                           0;JMP
                           
                           ({function}$$RET{no}) // mark return address
                           """.format(numArgs = numArgs,function = function,no = self.instances[function]))   
    
    def writeReturn(self):
#        Return to the last calling function.
        
#        Temporarily store pointers for the scope of the function being restored
        self.file.write("""@LCL          // tmp_FRAME = LCL
                           D = M
                           @$$TMP$FRAME
                           M = D
                           @5
                           A = D - A     // tmp_RET = LCL - 5
                           D = M
                           @$$TMP$RETADD
                           M = D
                           """)
        
#        Restore scope pointers then jump to the return address. The function should 
#        leave its return value at its ARG 0 position.
        self.file.write("""@SP            // pop inner_ARG 0
                           AM = M - 1
                           D = M
                           @ARG
                           A = M
                           M = D
                           
                           @ARG           // SP = inner_ARG + 1
                           D = M
                           @SP
                           M = D + 1
                           
                           @$$TMP$FRAME      // THAT = FRAME - 1
                           AM = M - 1
                           D = M
                           @THAT
                           M = D
                           
                           @$$TMP$FRAME       // THIS = FRAME - 2
                           AM = M - 1
                           D = M
                           @THIS
                           M = D
                           
                           @$$TMP$FRAME       // ARG = FRAME - 3
                           AM = M - 1
                           D = M
                           @ARG
                           M = D
                           
                           @$$TMP$FRAME       // LCL = FRAME - 4
                           A = M - 1
                           D = M
                           @LCL
                           M = D
                           
                           @$$TMP$RETADD
                           A = M
                           0;JMP
                           """)
        
    def writeFunction(self,function,numLocals):
#        Define function with numLocals local variables.
        self.current_function = function
        self.file.write("({})\n".format(self.current_function))
        for i in range(int(numLocals)):
            self.writePushPop("push","constant",0)
        self.file.write("\n")
        

    def writeArithmetic(self,command):
#        Writes the assembly code that is the translation of the given arithmetic command.
#        If the command is binary, the second argument is the top of the stack.
        
        arith_dict = {'eq':"""@{function}$$C{no}
                            D = A
                            @$TMP$$COMP
                            M = D
                            @SP
                            AM = M - 1
                            D = M
                            @SP
                            AM = M - 1
                            D = M - D
                            @$COMP
                            D;JEQ
                            @SP
                            A = M
                            M = 0
                            @SP
                            M = M + 1
                            ({function}$$C{no})
                            """,
            
            'lt':"""@{function}$$C{no}
                    D = A
                    @$TMP$$COMP
                    M = D
                    @SP
                    AM = M - 1
                    D = M
                    @SP
                    AM = M - 1
                    D = M - D
                    @$COMP
                    D;JLT
                    @SP
                    A = M
                    M = 0
                    @SP
                    M = M + 1
                    ({function}$$C{no})
                    """,
            
            'gt':"""@{function}$$C{no}
                    D = A
                    @$TMP$$COMP
                    M = D
                    @SP
                    AM = M - 1
                    D = M
                    @SP
                    AM = M - 1
                    D = M - D
                    @$COMP
                    D;JGT
                    @SP
                    A = M
                    M = 0
                    @SP
                    M = M + 1
                    ({function}$$C{no})
                    """,
            
            'add':"""@SP
                    AM = M - 1
                    D = M
                    @SP
                    AM = M - 1
                    D = D + M
                    @SP
                    A = M
                    M = D
                    @SP
                    M = M + 1
                    """,
                    
            'sub':"""@SP
                    AM = M - 1
                    D = M
                    @SP
                    AM = M - 1
                    D = M - D
                    @SP
                    A = M
                    M = D
                    @SP
                    M = M + 1
                    """,
            
            'neg':"""@SP
                    AM = M - 1
                    D = -M
                    @SP
                    A = M
                    M = D
                    @SP
                    M = M + 1
                    """,
            
            'not':"""@SP
                    AM = M - 1
                    D = !M
                    @SP
                    A = M
                    M = D
                    @SP
                    M = M + 1
                    """,
                
            'and':"""@SP
                    AM = M - 1
                    D = M
                    @SP
                    AM = M - 1
                    D = D & M
                    @SP
                    A = M
                    M = D
                    @SP
                    M = M + 1
                    """,
            
            'or':"""@SP
                    AM = M - 1
                    D = M
                    @SP
                    AM = M - 1
                    D = D | M
                    @SP
                    A = M
                    M = D
                    @SP
                    M = M + 1
                    """}    
        self.file.write(arith_dict[command].format(function = self.current_function,no = self.current_parser.command_no))
        
    def writePushPop(self,pushpop,segment,index):
#        Writes the assembly code that is the translation of the given command, where command is either C_PUSH or C_POP. 
        
        seg_dict = {"local": "LCL",
                    "argument": "ARG",
                    "this": "THIS",
                    "that": "THAT",
                    "static": 16,
                    "pointer": 3,
                    "temp": 5,
                    "constant": 0}
                    
        if pushpop == "push":
            if segment == "constant":
                self.file.write("""@{index}
                D = A
                """.format(index=index))
            elif segment in ["temp","pointer"]:
                self.file.write("""@{index}
                D = M
                """.format(index = int(index) + seg_dict[segment]))
            elif segment == "static":
                self.file.write("""@{file}.{index}
                                    D = M
                                    """.format(file = self.current_file,index = index))
            else:
                self.file.write("""@{segment}
                                    D = M
                                    @{index}
                                    A = D + A
                                    D = M
                                    """.format(segment = seg_dict[segment],index=index))
            self.file.write("""
                            @SP
                            A = M
                            M = D
                            @SP
                            M = M + 1
                            """)
                
        if pushpop == "pop":
            if segment in ["constant","temp","pointer"]:
                self.file.write("""@{index}
                                D = A
                                """.format(index = int(index) + seg_dict[segment]))
            elif segment == "static":
                self.file.write("""@{file}.{index}
                                    D = A
                                    """.format(file = self.current_file,index=index))
            else:
                self.file.write("""@{segment}
                                    D = M
                                    @{index}
                                    D = D + A
                                    """.format(segment = seg_dict[segment],index=index))
            self.file.write("""@$TMP$$POP
                                M = D
                                @SP
                                AM = M - 1
                                D = M
                                @$TMP$$POP
                                A = M
                                M = D
                                """.format(segment = seg_dict[segment],index=index))
        
    def close(self):
#        Closes the output file.
        self.file.close()
        clean = open(self.filename,'w')
        temp = open('temp.txt')
        for line in temp:
            clean.write(line.lstrip())
        temp.close()
        clean.close()
        
def main(target):
    start_dir = os.getcwd()
    target = os.path.realpath(target)
    codeWriter = CodeWriter()
    codeWriter.setDestName(os.path.split(target)[1])
    
    if os.path.isdir(target):
        os.chdir(target)
        is_directory = ("Sys.vm" in os.listdir())
        codeWriter.writeInit(is_directory)
        for file in os.listdir(target):
            if file.endswith(".vm"):
                translate(file,codeWriter)
    else:
        os.chdir(os.path.split(target)[0])
        target = os.path.split(target)[1]
        if os.path.isfile(target):
            if target.endswith(".vm"):
                codeWriter.writeInit(is_directory=False)
                translate(target,codeWriter)
    codeWriter.close()
    os.chdir(start_dir)
    
def translate(file,codeWriter):
    parser = Parser(file)
    codeWriter.setFileName(parser)
    
    parser.advance()
    while parser.hasMoreCommands:
#        codeWriter.writeDebug()
        command = parser.commandType()
        if command == "arithmetic":
            codeWriter.writeArithmetic(parser.arg1())
        if command in ["push","pop"]:
            codeWriter.writePushPop(command,parser.arg1(),parser.arg2())
        if command == "function":
            codeWriter.writeFunction(parser.arg1(),parser.arg2())
        if command == "return":
            codeWriter.writeReturn()
        if command == "call":
            codeWriter.writeCall(parser.arg1(),parser.arg2())
        if command == "goto":
            codeWriter.writeGoto(parser.arg1())
        if command == "if-goto":
            codeWriter.writeIf(parser.arg1())
        if command == "label":
            codeWriter.writeLabel(parser.arg1())
        parser.advance()