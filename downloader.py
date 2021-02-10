import argparse
import subprocess
import os

def cmdcall(command):
    process = subprocess.Popen(command)
    process.communicate()

def isValidUrl(url):
    return True

def main(args):
    if not isValidUrl(args.url):
        return -1
    url = args.url
    tmp = 'tmp.ogg'
    dst = args.out + ".mp3"
    
    command_tmp = 'vlc ' + url + ' --sout=#transcode{acodec="opus",ab="128","channels=2",samplerate="44100"}:standard{access=file,mux=ogg,dst=' + tmp +'} vlc://quit'
    command_out = 'vlc ' + tmp + ' --sout=#transcode{acodec="mp3",ab="128","channels=2",samplerate="44100"}:standard{access=file{no-overwrite},mux=dummy,dst=' + dst + '} vlc://quit'

    if not args.verbose:
        command_tmp += " --qt-notification=0 --qt-start-minimized"
        command_out += " --qt-notification=0 --qt-start-minimized"

    cmdcall(command_tmp)
    cmdcall(command_out)
    os.remove(tmp)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Specify youtube url to download audio from.")
    parser.add_argument('--out', default="out", metavar="<FILENAME>", help="Specify name of output file.")
    parser.add_argument("-verbose", action="store_true", help="Show VLC media player GUI when downloading audio.")
    args = parser.parse_args()
    main(args)