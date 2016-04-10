#!/usr/bin/python2

import sys
import re

r = re.compile(r'(\w+)\s+(?:[-0-9]+\s+){3}(#\w+)\s+#\w+')

with open('selenized.css', 'w') as out:
    for line in sys.stdin.readlines():
        m = r.match(line)
        if m:
            out.write('c [f={0}] {{ color: {1}; }}\n'.format(*m.group(1,2)))
            out.write('c [b={0}] {{ background-color: {1}; }}\n'.format(*m.group(1,2)))
