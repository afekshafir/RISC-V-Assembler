# Modular Simple Loop Example

addi t0, zero, 5    # Initialize counter to 5
addi t1, zero, 0    # Initialize sum to 0

loop:
add t1, t1, t0      # sum += counter
addi t0, t0, -1     # counter--
bne t0, zero, loop  # loop back if counter != 0

end:
jal zero, end       # infinite loop to halt
