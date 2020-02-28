@256
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
@Sys.init$$RET1 // Push return address
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
@0           // Initialize ARG = SP - (5 + numArgs)
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
@Sys.init        // Jump to function
0;JMP
(Sys.init$$RET1) // mark return address
(Class1.set)
@ARG
D = M
@0
A = D + A
D = M
@SP
A = M
M = D
@SP
M = M + 1
@Class1.0
D = A
@$TMP$$POP
M = D
@SP
AM = M - 1
D = M
@$TMP$$POP
A = M
M = D
@ARG
D = M
@1
A = D + A
D = M
@SP
A = M
M = D
@SP
M = M + 1
@Class1.1
D = A
@$TMP$$POP
M = D
@SP
AM = M - 1
D = M
@$TMP$$POP
A = M
M = D
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
@LCL          // tmp_FRAME = LCL
D = M
@$$TMP$FRAME
M = D
@5
A = D - A     // tmp_RET = LCL - 5
D = M
@$$TMP$RETADD
M = D
@SP            // pop inner_ARG 0
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
(Class1.get)
@Class1.0
D = M
@SP
A = M
M = D
@SP
M = M + 1
@Class1.1
D = M
@SP
A = M
M = D
@SP
M = M + 1
@SP
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
@LCL          // tmp_FRAME = LCL
D = M
@$$TMP$FRAME
M = D
@5
A = D - A     // tmp_RET = LCL - 5
D = M
@$$TMP$RETADD
M = D
@SP            // pop inner_ARG 0
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
(Class2.set)
@ARG
D = M
@0
A = D + A
D = M
@SP
A = M
M = D
@SP
M = M + 1
@Class2.0
D = A
@$TMP$$POP
M = D
@SP
AM = M - 1
D = M
@$TMP$$POP
A = M
M = D
@ARG
D = M
@1
A = D + A
D = M
@SP
A = M
M = D
@SP
M = M + 1
@Class2.1
D = A
@$TMP$$POP
M = D
@SP
AM = M - 1
D = M
@$TMP$$POP
A = M
M = D
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
@LCL          // tmp_FRAME = LCL
D = M
@$$TMP$FRAME
M = D
@5
A = D - A     // tmp_RET = LCL - 5
D = M
@$$TMP$RETADD
M = D
@SP            // pop inner_ARG 0
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
(Class2.get)
@Class2.0
D = M
@SP
A = M
M = D
@SP
M = M + 1
@Class2.1
D = M
@SP
A = M
M = D
@SP
M = M + 1
@SP
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
@LCL          // tmp_FRAME = LCL
D = M
@$$TMP$FRAME
M = D
@5
A = D - A     // tmp_RET = LCL - 5
D = M
@$$TMP$RETADD
M = D
@SP            // pop inner_ARG 0
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
(Sys.init)
@6
D = A
@SP
A = M
M = D
@SP
M = M + 1
@8
D = A
@SP
A = M
M = D
@SP
M = M + 1
@Class1.set$$RET1 // Push return address
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
@2           // Initialize ARG = SP - (5 + numArgs)
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
@Class1.set        // Jump to function
0;JMP
(Class1.set$$RET1) // mark return address
@5
D = A
@$TMP$$POP
M = D
@SP
AM = M - 1
D = M
@$TMP$$POP
A = M
M = D
@23
D = A
@SP
A = M
M = D
@SP
M = M + 1
@15
D = A
@SP
A = M
M = D
@SP
M = M + 1
@Class2.set$$RET1 // Push return address
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
@2           // Initialize ARG = SP - (5 + numArgs)
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
@Class2.set        // Jump to function
0;JMP
(Class2.set$$RET1) // mark return address
@5
D = A
@$TMP$$POP
M = D
@SP
AM = M - 1
D = M
@$TMP$$POP
A = M
M = D
@Class1.get$$RET1 // Push return address
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
@0           // Initialize ARG = SP - (5 + numArgs)
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
@Class1.get        // Jump to function
0;JMP
(Class1.get$$RET1) // mark return address
@Class2.get$$RET1 // Push return address
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
@0           // Initialize ARG = SP - (5 + numArgs)
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
@Class2.get        // Jump to function
0;JMP
(Class2.get$$RET1) // mark return address
(Sys.init$WHILE)
@Sys.init$WHILE
0;JMP
