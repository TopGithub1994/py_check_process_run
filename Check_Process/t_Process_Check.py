#/usr/bin/env python

import os
import sys

pid = str(os.getpid())
pidfile = "./mydemon.pid"

if os.path.isfile(pidfile):
    print("%s already exists, exiting" % pidfile)
    sys.exit()
open(pidfile, 'w').write(pid)
try:
    # Do some actual work here
    print("top...")
finally:
    os.unlink(pidfile)