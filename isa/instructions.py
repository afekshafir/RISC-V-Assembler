INSTRUCTIONS = {
    # R-Type
    'add':  {'opcode': 0x33, 'funct3': 0x0, 'funct7': 0x00, 'type': 'R'},
    'sub':  {'opcode': 0x33, 'funct3': 0x0, 'funct7': 0x20, 'type': 'R'},
    'and':  {'opcode': 0x33, 'funct3': 0x7, 'funct7': 0x00, 'type': 'R'},
    'or':   {'opcode': 0x33, 'funct3': 0x6, 'funct7': 0x00, 'type': 'R'},
    'xor':  {'opcode': 0x33, 'funct3': 0x4, 'funct7': 0x00, 'type': 'R'},
    'slt':  {'opcode': 0x33, 'funct3': 0x2, 'funct7': 0x00, 'type': 'R'},
    
    # I-Type
    'addi': {'opcode': 0x13, 'funct3': 0x0, 'type': 'I'},
    'lw':   {'opcode': 0x03, 'funct3': 0x2, 'type': 'I'},
    'jalr': {'opcode': 0x67, 'funct3': 0x0, 'type': 'I'},
    
    # S-Type
    'sw':   {'opcode': 0x23, 'funct3': 0x2, 'type': 'S'},
    
    # B-Type
    'beq':  {'opcode': 0x63, 'funct3': 0x0, 'type': 'B'},
    'bne':  {'opcode': 0x63, 'funct3': 0x1, 'type': 'B'},
    
    # J-Type
    'jal':  {'opcode': 0x6f, 'type': 'J'}
}
