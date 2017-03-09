from PIL import Image, ImageDraw, ImageColor
import fileinput

def adjust(x):
    return x - 0x64410

load_address_pic1 = adjust(0x21af98)
load_address_maphead = adjust(0x14d688)
load_address_bee = adjust(0xd21e0)
load_address_tunnel = adjust(0x114090)
#load_address_install = adjust(0x64390)
load_address_avena = adjust(0x1bf6c0)
load_address_1 = adjust(0x64410)
load_address_2 = adjust(0x88e00)
load_address_3 = adjust(0x165940)
load_address_mhed = adjust(0x88e00)
load_address_inside = adjust(0xcacb0)

#Implicit
#;load_address_1:		ds.b	150000		;fish/letters/pic2
#;load_address_2:		ds.b	300000		;mhed/tree
#;load_address_3:		ds.b	300000		;title/mars_data

load_address_mars = load_address_3
load_address_fish = load_address_1
load_address_title = load_address_3 
load_address_tree = load_address_2
load_address_letters = load_address_1
load_address_pic2 = load_address_1

starts = {
    "mars_data" : load_address_mars,
    "fish_data" : load_address_fish,
    "title_data" : load_address_title,
    "tree_data" : load_address_tree,
    "letters_data" : load_address_letters,
    "pic1_data" : load_address_pic1,
    "bee_data" : load_address_bee,
    "inside_data" : load_address_inside,
    "mhed_data" : load_address_mhed,
    "tunnel_data" : load_address_tunnel,
    "maphead_data" : load_address_maphead,
    "avena_data" : load_address_avena,
    "pic2_data" : 0,
}


sizes = {
    "mars_data" : 308420,
    "fish_data" : 345884,
    "title_data" : 257426,
    "tree_data" : 195788,
    "letters_data" : 83662,
    "pic1_data" : 185482,
    "bee_data" : 601262,
    "inside_data" : 278860,
    "mhed_data" : 112150,
    "tunnel_data" : 229010,
    "maphead_data" : 465036,
    "avena_data" : 70242,
    "pic2_data" : 803982,
}

first_step = {}
last_step = {}

colours = {
    "mars_data" : "red",
    "fish_data" : "blue",
    "title_data" : "white",
    "tree_data" : "green",
    "letters_data" : "grey",
    "pic1_data" : "orange",
    "bee_data" : "yellow",
    "inside_data" : "lime",
    "mhed_data" : "purple",
    "tunnel_data" : "yellow",
    "maphead_data" : "brown",
    "avena_data" : "white",
    "pic2_data" : "cyan",
}


#;../../unpacked/AVENA.PRG,70242			70242	1422000	1492242
#;../../unpacked/BEE.PRG,601262			    601262	450000	1051262
#;../../unpacked/FISH.PRG,345884			345884	0	345884
#;../../unpacked/INSIDE.PRG,278860			278860	420000	698860
#;../../unpacked/LETTERS.PRG,83662			83662	0	83662
#;../../unpacked/MAPHEAD.PRG,465036			465036	955000	1420036
#;../../unpacked/MARS.PRG,308420			308420	1797000	2105420
#;../../unpacked/MHED.PRG,112150			112150	150000	262150
#;../../unpacked/PIC1.PRG,185482			185482	1797000	1982482
#;../../unpacked/TITLE.PRG,257426			257426	1797000	2054426
#;../../unpacked/TREE.PRG,195788			195788	150000	345788
#;../../unpacked/TUNR.PRG,229010			229010	720000	949010
#;../../unpacked/PIC2.PRG,803982			803982	0	803982

import sys

div = 1024 * 2
y = 0

blockheight = 5
for line in fileinput.input():
    if line.find("execute") != -1:
        #print "***", line, "***"
        rest = line.split("\t")[3]
        progname = rest.split(",")[0]

        last_step[progname] = y
        if not first_step.has_key(progname):
            print "%s seen at %d" % (progname, y)
            first_step[progname] = y

        y += 1

# Now render them

i = Image.new("RGB", (1600, 700), (64, 64, 64))

draw = ImageDraw.Draw(i)
for progname in first_step.keys():
    start = starts[progname]
    size = sizes[progname]
    end = start + size

    first = first_step[progname]
    last = last_step[progname]

    print "%s seen at %d -> %d" % (progname, first, last)
    
    col = ImageColor.getcolor(colours[progname], "RGB")
    draw.rectangle( (start / div, first * blockheight, 
                    end / div,
                    (last + 1) * blockheight), outline=col)
    draw.text( (start / div, first * blockheight), progname)

fp = open("map.png", "wb")
i.save(fp, "PNG")
fp.close()
print y
