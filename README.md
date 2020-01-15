# 8bit_MicroComputer_Verilog
This project was inspired by the efforts of Ben Eater to build an 8 bit computer on a breadboard. Even though this one was not built on a breadboard, it has the functionalities of his computer and modelled using Verilog HDL. This was developed for the Mini Project in Digital Systems course in my 3rd semester at IIT Palakkad.


  The VerilogModules folder contains all the Verilog source codes to simulate the 8-bit computer and also the testbench file.
  The modules required for the computer are defined separately and then combined and interfaced in a common module named CPU.v .
  It also contains a testbench file named CPU_tb.v which is used to simulate the behaviour of the computer.

  The AssemblyCode folder contains the Assembly language compiler in the form of a python script as well as a Program.txt file which is essentially a 16 byte executable assembly code. The compiler accepts the compilable text file as an argument in the compilation line and writes the binary sequence in a file named binary.txt .

# IMPORTANT : 
  In order to use the assembler, please use below mentioned syntax :
    python assembler.py <input_filename_with_extension>
  And press Enter.
  Now just copy the contents of the newly generated binary.txt file and use it to replace the similar looking block in RAM.v file.
  Now you can synthesize the CPU_tb.v file and see the output.


# System Requirements :
  Make sure you have Python3 installed in your system.


# Recommended :
  Install iverilog (an open source verilog code synthesizer) and type in the set of below mentioned commands in your Command Prompt or Terminal window.
  iverilog CPU_tb.v
  vvp a.out
  gtkwave dump.vcd
  
  Now the gtkwave program (also an open source waveform viewer) will display the output of the 8bit Computer in a new window.


# THANK YOU !!!
