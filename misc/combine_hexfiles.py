#!/usr/bin/env python3

import pystk500v2
import sys

def main():
    if len(sys.argv) < 2:
        print('Usage: {} <hexfile1> [hexfile2] [hexfile3...]'.format(sys.argv[0]))
        sys.exit(0)
    
    h = pystk500v2.HexFile()
    for f in sys.argv[1:]:
        h.fromIHexFile(f)

    print(h.toIHexString())

if __name__ == '__main__':
    main()
