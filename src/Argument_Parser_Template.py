"""
Argument parser template
"""

import argparse

parser = argparse.ArgumentParser(description='Your application description')
# simple argument (mandatory)
parser.add_argument('a', help='some description')
# cast positional argument to int
parser.add_argument('b', type=int, help='some description')
# option (optional)
parser.add_argument('-r', help='some description')
# set silent=True if this option available
parser.add_argument('-s', '--silent', action='store_true', default=False, help='some description')
# parse arguments/options to an object args
args = parser.parse_args()

# call the arguments/options
print(args.a)
print(args.b)
print(args.r)
print(args.s)
print(args.silent)