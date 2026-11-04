from .parser import Parser
from .encoder import Encoder

class Assembler:
    def __init__(self):
        self.parser = Parser()
        self.encoder = Encoder(self.parser.labels)

    def assemble(self, lines):
        # Pass 1: Parse labels and map line numbers to addresses
        parsed_instructions = self.parser.first_pass(lines)
        
        # Pass 2: Encode instructions to machine code
        machine_codes = []
        for line_num, address, line in parsed_instructions:
            try:
                code = self.encoder.assemble_line(line, address)
                machine_codes.append(code)
            except Exception as e:
                raise ValueError(f"Error on line {line_num + 1} '{line}': {e}")
                
        return machine_codes
