#!/usr/bin/env sh
vasmm68k_mot -Ftos -devpac -nocase -m68030 -I .. -I ../../mdata/ -I ../CIA/ -I ../../ -I ../../DATA/ MAIN_1.S
