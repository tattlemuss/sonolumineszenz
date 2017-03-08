from PIL import Image, ImageDraw, ImageColor
import fileinput

starts = {
    "mars_data" : 1797000,
    "fish_data" : 0,
    "title_data" : 1797000,
    "tree_data" : 150000,
    "letters_data" : 0,
    "pic1_data" : 1797000,
    "bee_data" : 450000,
    "inside_data" : 420000,
    "mhed_data" : 150000,
    "tunnel_data" : 720000,
    "maphead_data" : 955000,
    "avena_data" : 1422000,
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
