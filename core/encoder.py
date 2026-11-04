from isa.instructions import INSTRUCTIONS
from isa.registers import get_reg

class Encoder:
    def __init__(self, labels):
        self.labels = labels

    def assemble_line(self, line, current_address):
        parts = line.split()
        mnemonic = parts[0]
        
        if mnemonic not in INSTRUCTIONS:
            raise ValueError(f"Unknown instruction: {mnemonic}")
            
        instr_def = INSTRUCTIONS[mnemonic]
        instr_type = instr_def['type']
        opcode = instr_def['opcode']
        
        if instr_type == 'R':
            return self._encode_r_type(parts, instr_def, opcode)
        elif instr_type == 'I':
            return self._encode_i_type(parts, instr_def, opcode)
        elif instr_type == 'S':
            return self._encode_s_type(parts, instr_def, opcode)
        elif instr_type == 'B':
            return self._encode_b_type(parts, instr_def, opcode, current_address)
        elif instr_type == 'J':
            return self._encode_j_type(parts, instr_def, opcode, current_address)
        
        raise ValueError(f"Unsupported instruction type: {instr_type}")

    def _encode_r_type(self, parts, instr_def, opcode):
        rd = get_reg(parts[1])
        rs1 = get_reg(parts[2])
        rs2 = get_reg(parts[3])
        funct3 = instr_def['funct3']
        funct7 = instr_def['funct7']
        return (funct7 << 25) | (rs2 << 20) | (rs1 << 15) | (funct3 << 12) | (rd << 7) | opcode

    def _encode_i_type(self, parts, instr_def, opcode):
        rd = get_reg(parts[1])
        funct3 = instr_def['funct3']
        
        if '(' in parts[2]: # e.g. lw x1, 4(x2)
            offset_part, base_reg_part = parts[2].split('(')
            rs1 = get_reg(base_reg_part.replace(')', ''))
            imm = int(offset_part, 0) & 0xFFF
        else: # e.g. addi x1, x2, 4
            rs1 = get_reg(parts[2])
            imm = int(parts[3], 0) & 0xFFF 
            
        return (imm << 20) | (rs1 << 15) | (funct3 << 12) | (rd << 7) | opcode

    def _encode_s_type(self, parts, instr_def, opcode):
        rs2 = get_reg(parts[1])
        funct3 = instr_def['funct3']
        offset_part, base_reg_part = parts[2].split('(') 
        rs1 = get_reg(base_reg_part.replace(')', ''))
        imm = int(offset_part, 0) & 0xFFF
        
        imm_11_5 = (imm >> 5) & 0x7F
        imm_4_0 = imm & 0x1F
        return (imm_11_5 << 25) | (rs2 << 20) | (rs1 << 15) | (funct3 << 12) | (imm_4_0 << 7) | opcode

    def _encode_b_type(self, parts, instr_def, opcode, current_address):
        rs1 = get_reg(parts[1])
        rs2 = get_reg(parts[2])
        funct3 = instr_def['funct3']
        target = parts[3].strip(',')
        
        if target in self.labels:
            imm = (self.labels[target] - current_address) & 0x1FFF
        else:
            imm = int(target, 0) & 0x1FFF 
            
        imm_12 = (imm >> 12) & 1
        imm_10_5 = (imm >> 5) & 0x3F
        imm_4_1 = (imm >> 1) & 0xF
        imm_11 = (imm >> 11) & 1
        return (imm_12 << 31) | (imm_10_5 << 25) | (rs2 << 20) | (rs1 << 15) | (funct3 << 12) | (imm_4_1 << 8) | (imm_11 << 7) | opcode

    def _encode_j_type(self, parts, instr_def, opcode, current_address):
        rd = get_reg(parts[1])
        target = parts[2].strip(',')
        
        if target in self.labels:
            imm = (self.labels[target] - current_address) & 0x1FFFFF
        else:
            imm = int(target, 0) & 0x1FFFFF
            
        imm_20 = (imm >> 20) & 1
        imm_10_1 = (imm >> 1) & 0x3FF
        imm_11 = (imm >> 11) & 1
        imm_19_12 = (imm >> 12) & 0xFF
        return (imm_20 << 31) | (imm_10_1 << 21) | (imm_11 << 20) | (imm_19_12 << 12) | (rd << 7) | opcode
