# Oxygen Compiler v0.1
Compiles Oxygen code into assembly.

# How to Use
```
py src/main.py tests/test.ox
nasm -f elf64 output.asm -o output.o
ld output.o -o output
```
Use `python` or `python3` if that doesn't work.

You'll need NASM and LD for this.

# Changelogs
v0.1:
- Release (you can exit)
