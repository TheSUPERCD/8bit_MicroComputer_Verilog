import sys
sourceName = str(sys.argv[1])
assembled = []
compiler = {'LDA' : "8'b0001_", 'ADD' : "8'b0010_", 'SUBT' : "8'b0011_", 'OUT' : "8'b1110_", 'HLT' : "8'b1111_", 'JMP' : "8'b0100_"}
source = open(sourceName, 'r')
code = source.read().split('\n')
for item in code:
    item = item.strip().split(' ')
    if item == ['OUT'] or item == ['HLT']:
        assembled.append(compiler[item[0]] + "0000")
    elif len(item) == 2 :
        assembled.append(compiler[item[0]] + str(bin(int(item[1]))[2:].zfill(4)))
    else : 
        assembled.append("8'b0000_" + str(bin(int(item[0]))[2:].zfill(4)))
source.close()
binary = open("binary.txt", 'w+')
i=0
binary.write("initial begin\n")
for sign in assembled:
    binary.write("    Memory["+ str(i) +"] = " + sign + ';\n')
    i+=1
while(i < 16):
    binary.write("    Memory["+ str(i) +"] = 8'b0000_0000;\n")
    i+=1
binary.write("end")
binary.close()
print("\nThe binary instruction file has been prepared as binary.txt\nPlease replace the code block in RAM.v that initializes in the begining with the contents of this file...\n")