#!/usr/bin/env python3
import os
import sys

def main(args):
    command = "ffmpeg "
    command += "-i " + args[1]
    command += " -filter_complex "
    command += "\"[0:0]trim=start=0:duration=10[a];"
    command += "[0:0]trim=start=10:duration=10,setpts=PTS-STARTPTS[b];"
    command += "[b]negate[c];"
    command += "[a][c]concat[d];"
    command += "[0:0]trim=start=20:duration=60,setpts=PTS-STARTPTS[e];"
    command += "[d][e]concat[f];"
    command += "[0:0]trim=start=80:duration=10,setpts=PTS-STARTPTS[g];"
    command += "[g]negate[h];"
    command += "[f][h]concat[i];"
    command += "[0:0]trim=start=90,setpts=PTS-STARTPTS[j];"
    command += "[i][j]concat[out1]\" "
    command += "-map [out1] "
    command += "-c:v libvpx-vp9 -b:v 2M -pix_fmt yuv420p -map 0:1 -c:a copy -map 0:2 output.mkv"
    os.system(command)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv)
    else:
        print("Missing filepath parameter")
        print("Usage: python3 ./changing_codec.py <filepath")
