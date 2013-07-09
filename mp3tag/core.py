import os, itertools

def confirm(text):
    ''' asks some confirmation '''
    prompt =  text + " [y/n]"
    while True:
        answ = raw_input(prompt)
        if answ not in  ['y', 'Y', 'n', 'N']:
            print ("enter y or n")
            continue
        return answ == "y" or answ == "Y"

def print_help(fileName):
    print ("use %s [-r] [-c] [-v] <target directory>" % os.path.basename(fileName))
    print (" -r  - recursive")
    print (" -v  - verbose")
    print (" -c  - auto-confirmation")

def parse_args(args):
    ''' parses command line arguments '''
    if(len(args) <= 1):
        print_help(args[0])
        return None
    v = '-v' in args
    r = '-r' in args
    c = '-c' in args
    t = args[-1]
    if not os.path.exists(t):
        print_help(args[0])
        return None
    return { 'verbose': v, 'recursive': r, 'confirm': c, 'target': t }

def mp3_filter(f):
    return f[-4:] == ".mp3"

def list_files(target, filt = None, recursive = False):    
    if os.path.isdir(target):
        for root, dirs, files in os.walk(target):
            fg = [root + "/" + f for f in files if filt == None or filt(f)]
            if recursive:
                return itertools.chain(fg, *[list_files(root + "/" + d, filt, recursive) for d in dirs])
            else:
                return fg
    else:
        return [target] if filt(target) else None
