# 8bit_MicroComputer_Verilog
  The VerilogModules folder contains all the Verilog source codes to simulate the 8-bit computer and also the testbench file.
  The modules required for the computer are defined separately and then combined and interfaced in a common module named CPU.v .
  It also contains a testbench file named CPU_tb.v which is used to simulate the behaviour of the computer.

  The parent folder contains the Assembly language compiler in the form of a python script as well as a DemoProgram.asm file which is essentially a 16 byte executable assembly code. The compiler accepts the compilable text file as an argument in the compilation line and writes the binary sequence in a file named binary.txt .

# IMPORTANT : 
  In order to use the assembler, please use below mentioned syntax :
  # Method 1 :

    python Assembler_v2.py <input_filename_with_extension>


    And press Enter.


    Now the RAM.v module in the VerilogModules folder will be updated with the new set of instructions.
    No need to copy paste anything into the RAM module.

    THIS METHOD IS RECOMMENDED.


  # Method 2 :

    python Assembler_v1.py <input_filename_with_extension>


    And press Enter.

  
    Now just copy the contents of the newly generated binary.txt file and use it to replace the similar looking block in RAM.v file.
    Now you can synthesize the CPU_tb.v file and see the output.

# System Requirements :
  Make sure you have Python3 installed in your system.


  Make sure you have iverilog (abbreviation of Icarus Verilog) or Vivado synthesizer/simulator.


# Recommended :
  Install iverilog (an open source verilog code synthesizer) from here <https://bleyer.org/icarus/> and type in the set of below mentioned commands in your Command Prompt or Terminal window.
  
  
  iverilog CPU_tb.v


  vvp a.out


  gtkwave dump.vcd

  
  Now the gtkwave program (also an open source waveform viewer) will display the output of the 8bit Computer in a new window.


# THANK YOU !!!
