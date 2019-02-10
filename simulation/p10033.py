
def interpret(mem):
  pc = 0
  reg = [0]*10
  ins_commited = 0
  halted = False
  while not halted:
    ir = mem[pc]
    opcode = ir[0]
    op1 = int(ir[1])
    op2 = int(ir[2])
    ins_commited += 1
    pc = ( pc + 1 ) % 1000
    if opcode == "1": # Halt
      halted = True
    elif opcode == "2":  # Load imm
      reg[op1] = op2
    elif opcode == "3": # Add I
      reg[op1] += op2
      reg[op1] %= 1000
    elif opcode == "4":  # Mul I
      reg[op1] *= op2
      reg[op1] %= 1000
    elif opcode == "5":  # Move R
      reg[op1] = reg[op2]
    elif opcode == "6":  #  Add R
      reg[op1] += reg[op2]
      reg[op1] %= 1000
    elif opcode == "7": # Mul r
      reg[op1] *= reg[op2]
      reg[op1] %= 1000
    elif opcode == "8":  # Load
      reg[op1] = int(mem[reg[op2]])
    elif opcode == "9":  # Store
      v = str(reg[op1]).zfill(3)
      mem[reg[op2]] = v
    elif opcode == "0":  # Jump
      if reg[op2] != 0:
        pc = reg[op1]
    else:
      raise ValueError("unexpected instrution")
  return ins_commited
num_cases = int(input())
input()

from sys import stdin, stdout
for c in range(num_cases):
  mem = ["000"] * 1001

  line = stdin.readline().strip()
  i = 0
  while line != "":
    mem[i] = line
    i += 1
    line = stdin.readline().strip()
  
  stdout.write("{}\n".format(interpret(mem)))
  if c < num_cases - 1:
    stdout.write("\n")