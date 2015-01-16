#!/usr/bin/env python
from sympy.mpmath import *
import re
import argparse
import sys

class color:
   red = '\033[91m'
   bold = '\033[1m'
   end = '\033[0m'

def main(string=None):
    string = str(string)
    slen = len(string)
    do = True
    mp.dps = 100000
    try:
        while do:
            pi = str(mp.pi())
            if re.search(string, pi):
                st = pi.find(string)
                nst = st - 3
                if nst < 0:
                    nst = 0
                fstr = st + slen
                nend = fstr + 3
                print('Starting Position of String: ' + str(st))
                print(pi[nst:st] + color.bold + color.red + pi[st:fstr] +\
                      color.end + pi[fstr:nend])
                do = False
            else:
                mp.dps += 100000
    except KeyboardInterrupt:
        print('\n' + 'Number of Characters Checked: <' + str(len(pi)) +\
              '\n' + 'Program Interrupted')
        sys.exit(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('string')

    main(**vars(parser.parse_args()))
