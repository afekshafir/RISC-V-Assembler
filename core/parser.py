class Parser:
    def __init__(self):
        self.labels = {}

    def first_pass(self, lines):
        parsed_instructions = []
        address = 0
        
        for line_num, line in enumerate(lines):
            # Clean comments and whitespace
            line = line.split('#')[0].split('//')[0].strip()
            if not line:
                continue
                
            # Handle labels
            if ':' in line:
                label, rest = line.split(':', 1)
                self.labels[label.strip()] = address
                if rest.strip():
                    parsed_instructions.append((line_num, address, rest.strip()))
                    address += 4
            else:
                parsed_instructions.append((line_num, address, line))
                address += 4
                
        return parsed_instructions
