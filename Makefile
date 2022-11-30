CC = iverilog
FLAGS = -g2012

SIMULATION_EXEC = vvp
SIGNAL_PLOT = gtkwave

VERILOG_DIR = VerilogModules
OUTPUT_DIR = outputFiles

OUTPUT = CPU_tb_output

TARGET = CPU_tb

make:
	cd $(VERILOG_DIR) && \
	$(CC) $(FLAGS) $(TARGET).v -o ../$(OUTPUT_DIR)/$(OUTPUT) && \
	cd ../$(OUTPUT_DIR) && \
	$(SIMULATION_EXEC) $(OUTPUT) && \
	$(SIGNAL_PLOT) dump.vcd

clean:
	rm $(OUTPUT_DIR)/*