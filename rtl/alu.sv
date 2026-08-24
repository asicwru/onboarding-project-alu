module alu (
    input  logic [31:0] a,
    input  logic [31:0] b,
    input  logic [3:0]  opcode,
    output logic [31:0] result
);

/*
The opcode for the add operation is 4'h0. Fill in the rest of the local parameters.
*/

localparam ADD = 4'h0;
localparam SUB =
localparam AND =
localparam OR =
localparam XOR =
localparam NOT =
localparam SLL =
localparam SRL =
localparam SLT =
localparam EQ =

/*
The combinational statement for the ADD operation is given. Fill in the rest.
*/

always_comb begin
    case (opcode)
        4'h0: result = a + b;   // ADD
                                // SUB
                                // AND
                                // OR
                                // XOR
                                // NOT
                                // SLL
                                // SRL
                                // SLT
                                // EQ
        default: result = 32'b0; // Invalid opcode
    endcase
end

endmodule     
