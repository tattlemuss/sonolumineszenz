#!/usr/bin/env sh

# Clean
rm SL.LNK
rm SL.PRG
rm *.O

# Build the main prg
vasmm68k_mot -Felf -devpac -nocase -m68030 -I ..  -I 030/MAIN -I 030/CIA/ -I 030 -I DATA/ 030/MAIN/MAIN_1.S -o MAIN_1.O
vlink MAIN_1.O -s -M -b ataritos -o SL.PRG > syms.txt

# Build the WAD tool
cd tools/unlinker && make all

# Build the WAD
cd ../..
tools/unlinker/bin/linkfile unpacked/*.PRG unpacked/*.AON

