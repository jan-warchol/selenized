#!/usr/bin/python2

# input: table from the-values (copy-pasted)

# output: color expressions for scala

import sys
import re

r = re.compile(r'(\w+)\s+([0-9]+)\s+(?:[-0-9]+\s+){2}[0-9\s]+#(\w+)\s+#\w+')

for line in sys.stdin.readlines():
    m = r.match(line)
    if m:
        sys.stdout.write('new Color("{0}", "{2}", {1}),\n'.format(*m.group(1,2,3)))
