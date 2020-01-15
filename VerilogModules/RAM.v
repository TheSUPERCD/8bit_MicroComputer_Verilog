`timescale 1ns/1ps
module RAM(input clk, input [3:0] address, input [7:0] data_in, input write_enable, input reset, output reg [7:0] data_out);
reg [7:0] Memory[15:0];
integer i;

initial begin
    Memory[0] = 8'b0001_1001;
    Memory[1] = 8'b0010_1010;
    Memory[2] = 8'b0100_0111;
    Memory[3] = 8'b0011_1011;
    Memory[4] = 8'b0010_1100;
    Memory[5] = 8'b1110_0000;
    Memory[6] = 8'b0001_1101;
    Memory[7] = 8'b1110_0000;
    Memory[8] = 8'b1111_0000;
    Memory[9] = 8'b0000_0011;
    Memory[10] = 8'b0000_0010;
    Memory[11] = 8'b0000_0001;
    Memory[12] = 8'b0000_0101;
    Memory[13] = 8'b0000_1010;
    Memory[14] = 8'b0000_0000;
    Memory[15] = 8'b0000_0000;
end


always @(posedge clk)
begin
    if(!reset)
    begin
        if(write_enable)
        begin
            Memory[address] <= data_in;
        end
        else
        begin
            data_out <= Memory[address];
        end
    end
    else
    begin
        for(i=0;i<=15;i=i+1)
        begin
            Memory[i] <= 0;
        end
    end
end
endmodule