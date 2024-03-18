import math
import os
import re
import sys
import csv
import pprint

enable_PTK = True

args = sys.argv
formatted_data = []
path = args[1].replace("\\", "/")
framerate = float(args[2])

def time2frame(t):
    h, m, s = map(float, t.split(":"))
    f = int(math.floor((h * 3600 + m * 60 + s) * framerate))
    return f

def str2hex(strings):
    strings = strings.encode("utf-16-le").hex()
    while len(strings) < 4096:
        strings += "0"
    return strings

# require PSDToolKit
def build_block(serial_number, start_frame, end_frame, strings):
    if enable_PTK:
        return ("[" + str(serial_number) + "]\nstart=" + str(start_frame) + "\nend=" + str(end_frame) + "\nlayer=1\noverlay=1\ncamera=0\n["
            + str(serial_number) + ".0]\n_name=テキスト\nサイズ=1\n表示速度=0.0\n文字毎に個別オブジェクト=0\n移動座標上に表示する=0\n自動スクロール=0\nB=0\nI=0\ntype=0\nautoadjust=0\nsoft=0\nmonospace=0\nalign=0\nspacing_x=0\nspacing_y=0\nprecision=0\ncolor=ffffff\ncolor2=000000\nfont=MS UI Gothic\ntext="
            + str2hex('<?s=[==[\n' + strings + '\n]==];require("PSDToolKit").subtitle:set(s,obj,true);s=nil?>') + "\n[" + str(serial_number) + ".1]\n_name=標準描画\nX=0.0\nY=0.0\nZ=0.0\n拡大率=100.00\n透明度=100.0\n回転=0.00\nblend=0\n")
    else:
        return ("[" + str(serial_number) + "]\nstart=" + str(start_frame) + "\nend=" + str(end_frame) + "\nlayer=1\noverlay=1\ncamera=0\n["
            + str(serial_number) + ".0]\n_name=テキスト\nサイズ=34\n表示速度=0.0\n文字毎に個別オブジェクト=0\n移動座標上に表示する=0\n自動スクロール=0\nB=0\nI=0\ntype=0\nautoadjust=0\nsoft=0\nmonospace=0\nalign=0\nspacing_x=0\nspacing_y=0\nprecision=0\ncolor=ffffff\ncolor2=000000\nfont=MS UI Gothic\ntext="
            + str2hex(strings) + "\n[" + str(serial_number) + ".1]\n_name=標準描画\nX=0.0\nY=0.0\nZ=0.0\n拡大率=100.00\n透明度=0.0\n回転=0.00\nblend=0\n")

def build_exo(l):
    end_frame = l[-1][1]
    header = "[exedit]\nwidth=640\nheight=480\nrate=" + f"{framerate:n}" + "\nscale=1\nlength=" + str(end_frame) + "\naudio_rate=48000\naudio_ch=2\n"
    with open("str.exo", mode = "w", newline = "", encoding = "shift_jis") as f:
        f.write(header)
        for i, j in enumerate(formatted_data):
            f.writelines(build_block(i, j[0], j[1], j[2]))

# open csv file
with open(path, mode = "r", newline = "", encoding = "utf-8-sig") as f:
    reader = csv.reader(f)
    csv_data = [row for row in reader]

for start, end, strings in csv_data:
    formatted_data.append([time2frame(start) + 1, time2frame(end), strings])
pprint.pprint(formatted_data)
build_exo(formatted_data)
