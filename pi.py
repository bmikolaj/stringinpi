#!/usr/bin/env python
from sympy.mpmath import *
import re
import argparse
import sys

def main(string=None):
    string = str(string)
    do = True
    mp.dps = 10000
    try:
        while do:
            pi = str(mp.pi())
            if re.search(string, pi):
                st = pi.find(string)
                nst = st - 3
                if nst < 0:
                    nst = 0
                nend = st + len(string) + 3
                print('Start: ' + str(st))
                print(pi[nst:nend])
                do = False
            else:
                mp.dps += 10000
    except KeyboardInterrupt:
        print('\n' + str(len(pi)) + '\n' + 'Interrupted')
        sys.exit(-1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('string')

    main(**vars(parser.parse_args()))
