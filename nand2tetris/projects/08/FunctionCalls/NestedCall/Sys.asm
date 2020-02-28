@$INIT
0;JMP
(COMP)
@SP
A = M
M = -1
@SP
M = M + 1
@13
A = M
0;JMP
($INIT)
(Sys.init)
@4000
D = A
@SP
A = M
M = D
@SP
M = M + 1
@3
D = A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D
@5000
D = A
@SP
A = M
M = D
@SP
M = M + 1
@4
D = A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D
@Sys.main$$RET1 // Push return address
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
@Sys.main        // Jump to function
0;JMP
(Sys.main$$RET1) // mark return address
@6
D = A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D
(Sys.init$LOOP)
@Sys.init$LOOP
0;JMP
(Sys.main)
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
@4001
D = A
@SP
A = M
M = D
@SP
M = M + 1
@3
D = A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D
@5001
D = A
@SP
A = M
M = D
@SP
M = M + 1
@4
D = A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D
@200
D = A
@SP
A = M
M = D
@SP
M = M + 1
@LCL
D = M
@1
D = D + A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D
@40
D = A
@SP
A = M
M = D
@SP
M = M + 1
@LCL
D = M
@2
D = D + A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D
@6
D = A
@SP
A = M
M = D
@SP
M = M + 1
@LCL
D = M
@3
D = D + A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D
@123
D = A
@SP
A = M
M = D
@SP
M = M + 1
@Sys.add12$$RET1 // Push return address
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
@1           // Initialize ARG = SP - (5 + numArgs)
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
@Sys.add12        // Jump to function
0;JMP
(Sys.add12$$RET1) // mark return address
@5
D = A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D
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
@LCL
D = M
@1
A = D + A
D = M
@SP
A = M
M = D
@SP
M = M + 1
@LCL
D = M
@2
A = D + A
D = M
@SP
A = M
M = D
@SP
M = M + 1
@LCL
D = M
@3
A = D + A
D = M
@SP
A = M
M = D
@SP
M = M + 1
@LCL
D = M
@4
A = D + A
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
D = D + M
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
D = D + M
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
D = D + M
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
D = D + M
@SP
A = M
M = D
@SP
M = M + 1
@LCL          // tmp_FRAME = LCL
D = M
@5
M = D
@5
D = D - A     // tmp_RET = LCL - 5
@6
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
@5       // THAT = FRAME - 1
AM = M - 1
D = M
@THAT
M = D
@5       // THIS = FRAME - 2
AM = M - 1
D = M
@THIS
M = D
@5       // ARG = FRAME - 3
AM = M - 1
D = M
@ARG
M = D
@5       // LCL = FRAME - 4
A = M - 1
D = M
@LCL
M = D
@6         // tmp_RETURNADD
A = M
A = M
0;JMP
(Sys.add12)
@4002
D = A
@SP
A = M
M = D
@SP
M = M + 1
@3
D = A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D
@5002
D = A
@SP
A = M
M = D
@SP
M = M + 1
@4
D = A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D
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
@12
D = A
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
D = D + M
@SP
A = M
M = D
@SP
M = M + 1
@LCL          // tmp_FRAME = LCL
D = M
@5
M = D
@5
D = D - A     // tmp_RET = LCL - 5
@6
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
@5       // THAT = FRAME - 1
AM = M - 1
D = M
@THAT
M = D
@5       // THIS = FRAME - 2
AM = M - 1
D = M
@THIS
M = D
@5       // ARG = FRAME - 3
AM = M - 1
D = M
@ARG
M = D
@5       // LCL = FRAME - 4
A = M - 1
D = M
@LCL
M = D
@6         // tmp_RETURNADD
A = M
A = M
0;JMP
