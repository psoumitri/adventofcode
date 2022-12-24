# see https://adventofcode.com/2022/day/10

testProgram2 = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''

testProgram1='''noop
addx 3
addx -5'''
# Signal strength during 20th, 60th, 100th, 140th, 180th, and 220th cycles

class Instruction(): 

    def __init__( self ):
        self.cycle = 1
    
    def run_step(self, x):
        self.cycle -= 1
        return x

    def is_done(self):
        return self.cycle == 0 

class Noop( Instruction ):
    pass

class AddX( Instruction ):

    def __init__(self, x_incr ):
        self.cycle = 2
        self.x_incr = x_incr

    def run_step(self, x):
        if self.cycle == 1:
            x = x + self.x_incr
        self.cycle -= 1
        return x
    
import re

def processInstructions( inputStr ):
    noop_instr = re.compile('noop')
    addx_instr = re.compile('addx ([-\d]+)')
    # build program
    program = [] 
    for i, instruction in enumerate(inputStr.split('\n')):
        if noop_instr.match(instruction):
            program.append( Noop() )
        elif addx_instr.match(instruction):
            x_incr = addx_instr.match(instruction).groups()[0]
            program.append( AddX(int(x_incr)) )

    x = [1]
    for instr in program:
        while not instr.is_done():  
            curr_x = instr.run_step(x[-1])
            x.append( curr_x )

    #positions = [20, 60, 100, 140, 180, 220]
    #return sum(i*x[i-1] for i in positions if i <= len(x))

    for i,j in enumerate(x[:-1]):
        k = i % 40
        if k == 0: print()
        print_char = '#' if ( j >= k-1 and j <= k+1 ) else '.'
        print(print_char,end='')

#processInstructions(testProgram2)

actualInput = '''addx 1
addx 4
addx 1
noop
addx 4
addx 3
addx -2
addx 5
addx -1
noop
addx 3
noop
addx 7
addx -1
addx 1
noop
addx 6
addx -1
addx 5
noop
noop
noop
addx -37
addx 7
noop
noop
noop
addx 5
noop
noop
noop
addx 9
addx -8
addx 2
addx 5
addx 2
addx 5
noop
noop
addx -2
noop
addx 3
addx 2
noop
addx 3
addx 2
noop
addx 3
addx -36
noop
addx 26
addx -21
noop
noop
noop
addx 3
addx 5
addx 2
addx -4
noop
addx 9
addx 5
noop
noop
noop
addx -6
addx 7
addx 2
noop
addx 3
addx 2
addx 5
addx -39
addx 34
addx 5
addx -35
noop
addx 26
addx -21
addx 5
addx 2
addx 2
noop
addx 3
addx 12
addx -7
noop
noop
noop
noop
noop
addx 5
addx 2
addx 3
noop
noop
noop
noop
addx -37
addx 21
addx -14
addx 16
addx -11
noop
addx -2
addx 3
addx 2
addx 5
addx 2
addx -15
addx 6
addx 12
addx -2
addx 9
addx -6
addx 7
addx 2
noop
noop
noop
addx -33
addx 1
noop
addx 2
addx 13
addx 15
addx -21
addx 21
addx -15
noop
noop
addx 4
addx 1
noop
addx 4
addx 8
addx 6
addx -11
addx 5
addx 2
addx -35
addx -1
noop
noop'''

processInstructions(actualInput)