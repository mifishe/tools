from mutagen.easyid3 import EasyID3
import os, sys, re, core

romanMap =  {
    100 : 'C',
    90  : 'XC',
    50  : 'L', 
    40  : 'XL',
    10  : 'X',
    9   : 'IX',
    5   : 'V',
    4   : 'IV',
    1   : 'I',
}

#evaluating keys
romanKeys = list(reversed(sorted(romanMap.keys())))

def toRoman(numb):
    ''' converts decimal number to roman '''
    roman = ''
    for i in romanKeys:
        while numb >= i:
            roman += romanMap[i]
            numb -= i
    return roman

def checkUntitled(title):
    return title == None or title[0] == "Untitled"

def title_files(files, verbose = False, confirm = False):
    ''' changes titles of given mp3 files '''
    for f in files:
        a = EasyID3(f)
        if checkUntitled(a["title"]):
            m = re.search('^(\d+)(/\d*)?$', a["tracknumber"][0])
            if m:
                tn = int(m.group(1))
                if(confirm or core.confirm("change title for %s?" % f)):
                    a["title"] = toRoman(tn)
                    if(verbose):
                        print "%s => %s" % (f, a["title"])
                    a.save()
                
                

def main(target, recursive = False, verbose = False, confirm = False):
    title_files(core.list_files(target, core.mp3filter, recursive), verbose, confirm)

if __name__ == '__main__':
    args = core.parseArgs(sys.argv)
    if(args != None):
        main(args['target'], args['recursive'], args['verbose'], args['confirm'])