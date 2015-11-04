from mutagen.easyid3 import EasyID3
import os, sys, re, core


# add code here


def main(target, recursive = False, verbose = False, confirm = False):
    # add code here

if __name__ == '__main__':
    args = core.parse_args(sys.argv)
    if(args != None):
        main(args['target'], args['recursive'], args['verbose'], args['confirm'])
