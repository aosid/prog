//push constant 0    
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
//pop local 0         // initializes sum = 0
@LCL
D = M
@0
D = D + A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D
//label LOOP_START
(BasicLoop.$LOOP_START)
//push argument 0    
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
//push local 0
@LCL
D = M
@0
A = D + A
D = M
@SP
A = M
M = D
@SP
M = M + 1
//add
@SP
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
//pop local 0	        // sum = sum + counter
@LCL
D = M
@0
D = D + A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D
//push argument 0
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
//push constant 1
@1
D = A
@SP
A = M
M = D
@SP
M = M + 1
//sub
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
//pop argument 0      // counter--
@ARG
D = M
@0
D = D + A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D
//push argument 0
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
//if-goto LOOP_START  // If counter > 0, goto LOOP_START
@SP
AM = M - 1
D = M
@BasicLoop.$LOOP_START
D;JNE
//push local 0
@LCL
D = M
@0
A = D + A
D = M
@SP
A = M
M = D
@SP
M = M + 1
