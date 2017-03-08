
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

colours = {
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
from PIL import Image, ImageDraw
i = Image.new("RGB", (2000, 400), (128, 128, 128))

draw = ImageDraw.Draw(i)

div = 1024 * 2
y = 0

draw.line((0, 0, 400, 400), fill=128)
blockheight = 5
for line in fileinput.input():
    if line.find("execute") != -1:
        #print "***", line, "***"
        rest = line.split("\t")[3]
        progname = rest.split(",")[0]

        start = starts[progname]
        size = sizes[progname]
        end = start + size
        draw.rectangle((start / div, y, end / div, y + blockheight), fill=colours[progname])

        print start / div
        y += blockheight

fp = open("map.png", "wb")
i.save(fp, "PNG")
fp.close()
