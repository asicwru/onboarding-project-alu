module alu (
    input  logic [31:0] a,
    input  logic [31:0] b,
    input  logic [3:0]  op,
    output logic [31:0] y
);

always_comb begin
    case (op)
        // ADD
        // SUB
        // AND
        // OR
        // XOR
        // NOT
        // SLL
        // SRL
        // SLT
        // EQ
        default:
    endcase
end

endmodule
