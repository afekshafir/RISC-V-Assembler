# Modular RISC-V Assembler

A lightweight, modular, and easily extensible two-pass RISC-V Assembler written in Python. This project is designed for readability and scalability, making it easy to add new instructions, extensions, or linting features.

## Project Structure

This assembler uses a component-based architecture:

```
riscv_assembler/
├── core/
│   ├── assembler.py      # Main assembly pipeline (two-pass controller)
│   ├── parser.py         # Parses lines, cleans comments, extracts labels
│   └── encoder.py        # Bitwise operations to encode R/I/S/B/J instructions
├── isa/                  
│   ├── registers.py      # RISC-V ABI register mapping
│   └── instructions.py   # Opcode and function definitions for instructions
├── utils/
│   └── errors.py         # Custom error handling
├── main.py               # CLI entry point
└── example.asm           # Sample RISC-V program
```

### Components in Detail:
1. **`core/parser.py` (Pass 1):** Scans the raw text, removes comments, and records the memory addresses of all labels (e.g., `loop:`).
2. **`core/encoder.py` (Pass 2):** Takes the cleaned instructions and converts them to 32-bit machine code based on their type, automatically calculating relative branch/jump offsets.
3. **`isa/` (Instruction Set Architecture):** The "data dictionary" of the assembler. If you want to add support for a new instruction (like `mul` or `div`), you only need to update `isa/instructions.py` and potentially add a new encoding method in `encoder.py`.

## Features
- **Two-Pass Architecture**: Forward and backward label referencing works flawlessly out of the box.
- **ABI Compliance**: Full support for RISC-V ABI register names (`t0-t6`, `a0-a7`, `s0-s11`, etc.).
- **Extensible**: Clean separation of concerns means you can add custom instructions without touching the core parsing logic.

## Usage
Run the assembler via the command line:

```bash
python main.py example.asm -o output.hex
```
