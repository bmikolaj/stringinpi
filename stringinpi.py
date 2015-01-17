#!/usr/bin/env python
#String in Pi, stringinpi.py v1.0
#Copyright (c) 2015 by Brian Mikolajczyk, brianm12@gmail.com

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import re
from sympy.mpmath import *
import sys

class color:
   red = '\033[91m'
   bold = '\033[1m'
   end = '\033[0m'

def main(string=None):
    string = str(string)
    print('Searching for ' + string + ' in ' + u'\U0001D6D1')
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

def intcheck(val):
    try:
        val = int(val)
    except ValueError:
        raise argparse.ArgumentTypeError("{} is not a positive integer value"\
                                         .format(val))

    if val < 1:
        raise argparse.ArgumentTypeError("{} is not a positive integer value"\
                                         .format(val))
    else:
        return val

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('string', type=intcheck)
    parser.add_argument('--version', action='version',\
                         version='stringinpi.py v1.0')

    main(**vars(parser.parse_args()))