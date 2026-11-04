import argparse
from core.assembler import Assembler

def to_hex_string(instruction_hex):
    return f"{instruction_hex:08x}"

def main():
    parser = argparse.ArgumentParser(description="Modular RISC-V Assembler")
    parser.add_argument("input", help="Input assembly file (.asm)")
    parser.add_argument("-o", "--output", default="program.hex", help="Output hex file")
    args = parser.parse_args()

    try:
        with open(args.input, 'r') as infile:
            lines = infile.readlines()
            
        assembler = Assembler()
        machine_codes = assembler.assemble(lines)
        
        with open(args.output, 'w') as outfile:
            for code in machine_codes:
                outfile.write(f"{to_hex_string(code)}\n")
                
        print(f"Success! Assembled {len(machine_codes)} instructions. Output written to {args.output}")
        
    except FileNotFoundError:
        print(f"Error: File {args.input} not found.")
    except Exception as e:
        print(f"Assembly failed: {e}")

if __name__ == "__main__":
    main()
