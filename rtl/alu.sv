/*
Insert the ports required for the ALU. Remember, we need two input ports that are 32 bits wide to perform the operation on, another port to signal what type of operation we're going to perform, and a port that will store those results.
Hint
*/
module alu (
    

    
);

/*
The opcode for the add operation is 4'h0. Fill in the rest of the local parameters. What are the other operations that can be done by the ALU? The bit width of the ADD operation should serve as a hint to show you at least how many possible operations
there can be.
*/

localparam ADD = 4'h0;

/*
The combinational block for the ADD operation is given. Fill in the rest. The sample ports given (result, input1, and input2) can serve as a hint for the earlier step here and you may rename them.
You will also need to provide a variable inside the parentheses of the "case( PLACE VARIABLE HERE )" which should also be one of your ports. This will act as a selector and will determine what operation
will be performed based on its stored value. Structurally, the case statement maps out to be a multiplexer.
Lastly, you'll need to figure out and to provide a default case. It's important to cover all cases or every input combination because not doing so will create an 'accidental' latch. A default statement is used
so we can provide a value when our selector is of an undefined value.
*/

always_comb begin
    case()
        ADD: result = input1 + input2;  // ADD
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
