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
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1
@$$C10
D = A
@13
M = D
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@COMP
D;JEQ
@SP
A = M
M = 0
@SP
M = M + 1
($$C10)
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1
@16
D = A
@SP
A = M
M = D
@SP
M = M + 1
@$$C13
D = A
@13
M = D
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@COMP
D;JEQ
@SP
A = M
M = 0
@SP
M = M + 1
($$C13)
@16
D = A
@SP
A = M
M = D
@SP
M = M + 1
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1
@$$C16
D = A
@13
M = D
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@COMP
D;JEQ
@SP
A = M
M = 0
@SP
M = M + 1
($$C16)
@892
D = A
@SP
A = M
M = D
@SP
M = M + 1
@891
D = A
@SP
A = M
M = D
@SP
M = M + 1
@$$C19
D = A
@13
M = D
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@COMP
D;JLT
@SP
A = M
M = 0
@SP
M = M + 1
($$C19)
@891
D = A
@SP
A = M
M = D
@SP
M = M + 1
@892
D = A
@SP
A = M
M = D
@SP
M = M + 1
@$$C22
D = A
@13
M = D
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@COMP
D;JLT
@SP
A = M
M = 0
@SP
M = M + 1
($$C22)
@891
D = A
@SP
A = M
M = D
@SP
M = M + 1
@891
D = A
@SP
A = M
M = D
@SP
M = M + 1
@$$C25
D = A
@13
M = D
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@COMP
D;JLT
@SP
A = M
M = 0
@SP
M = M + 1
($$C25)
@32767
D = A
@SP
A = M
M = D
@SP
M = M + 1
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1
@$$C28
D = A
@13
M = D
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@COMP
D;JGT
@SP
A = M
M = 0
@SP
M = M + 1
($$C28)
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1
@32767
D = A
@SP
A = M
M = D
@SP
M = M + 1
@$$C31
D = A
@13
M = D
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@COMP
D;JGT
@SP
A = M
M = 0
@SP
M = M + 1
($$C31)
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1
@$$C34
D = A
@13
M = D
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@COMP
D;JGT
@SP
A = M
M = 0
@SP
M = M + 1
($$C34)
@57
D = A
@SP
A = M
M = D
@SP
M = M + 1
@31
D = A
@SP
A = M
M = D
@SP
M = M + 1
@53
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
@112
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
D = M - D
@SP
A = M
M = D
@SP
M = M + 1
@SP
AM = M - 1
D = -M
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
D = D & M
@SP
A = M
M = D
@SP
M = M + 1
@82
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
D = D | M
@SP
A = M
M = D
@SP
M = M + 1
@SP
AM = M - 1
D = !M
@SP
A = M
M = D
@SP
M = M + 1
