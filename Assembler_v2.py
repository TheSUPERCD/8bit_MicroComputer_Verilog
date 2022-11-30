import sys
sourceName = str(sys.argv[1])
assembled = []
compiler = {'LDA' : "0001_", 'ADD' : "0010_", 'SUBT' : "0011_", 'OUT' : "1110_", 'HLT' : "1111_", 'JMP' : "0100_"}
source = open(sourceName, 'r')
code = source.read().split('\n')
for item in code:
    item = item.strip().split('//')[0]
    item = item.strip().split(' ')
    if item == ['OUT'] or item == ['HLT']:
        assembled.append(compiler[item[0]] + "0000")
    elif item == ['']:
        continue
    elif len(item) == 2 :
        assembled.append(compiler[item[0]] + str(bin(int(item[1]))[2:].zfill(4)))
    else : 
        assembled.append("0000_" + str(bin(int(item[0]))[2:].zfill(4)))
source.close()
binTemp = open("RAMtemplate.v", 'r')
binaryCode = binTemp.read()
binTemp.close()
if sys.platform == "win32":
    binFile = open("VerilogModules\\RAM.v", 'w+')
elif (sys.platform == "linux") or (sys.platform == "darwin"):
    binFile = open("VerilogModules/RAM.v", 'w+')
else:
    print("What Operating system are you using?\nBecause this program is only made for Windows, Linux and MacOS")
binFile.write(binaryCode.format(assembled[0], assembled[1], assembled[2], assembled[3], assembled[4], assembled[5], assembled[6], assembled[7], assembled[8], assembled[9], assembled[10], assembled[11], assembled[12], assembled[13], assembled[14], assembled[15]))
binFile.close()