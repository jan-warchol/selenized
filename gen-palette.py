#!/usr/bin/python2

# input: table from the-values (copy-pasted)

# output: some css rules for easy color appliance

import sys
import re

r = re.compile(r'(\w+)\s+(?:[-0-9]+\s+){3}(#\w+)\s+#\w+')

with open('selenized.css', 'w') as out:
    for line in sys.stdin.readlines():
        m = r.match(line)
        if m:
            out.write('[f={0}] {{ color: {1}; }}\n'.format(*m.group(1,2)))
            out.write('[b={0}] {{ background-color: {1}; }}\n'.format(*m.group(1,2)))
