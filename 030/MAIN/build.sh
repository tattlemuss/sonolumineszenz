#!/usr/bin/env sh
vasmm68k_mot -Felf -devpac -nocase -m68030 -I .. -I ../../mdata/ -I ../CIA/ -I ../../ -I ../../DATA/ MAIN_1.S -o MAIN_1.O

vlink MAIN_1.O -s -M -b ataritos -o SL.PRG > syms.txt

