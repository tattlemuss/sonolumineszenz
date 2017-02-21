# coding=utf-8

# Motorola m68k disassembly functions
import array
import struct

def read_struct(fh, fmt):
    # Read a binary structure from the file of the given format
    size = struct.calcsize(fmt)
    data = fh.read(size)
    return struct.unpack(fmt, data)

def loader_tos(input_file, fh):
    # Load a TOS-format executable file and create the disassembly context
    # See http://toshyp.atari.org/en/005005.html for TOS header details
    # and https://github.com/libretro/hatari/blob/master/tools/debugger/gst2ascii.c for an example of reading DRI
    (header, textlen, datalen, bsslen, symbollen, reserved1, flags, relocinfo) = read_struct(fh, '>HIIIIIIH')
    if header != 0x601a:
        raise Exception('m68kdis: Incorrect PRG file header')
    
    #print "Text length %u" % textlen
    #print "Data length %u" % datalen
    #print "Symbol length %u" % symbollen
    #print "BSS length %u" % bsslen
    print "%s,%d" % (input_file, textlen + datalen + symbollen + bsslen)
    
if __name__ == '__main__':
    import sys, getopt, os
    
    for input_file in sys.argv[2:]:
        try:
            fh = open(input_file, 'rb')
            # Load based on filename extension
            loader_tos(input_file, fh)
        finally:
            fh.close()    
        
