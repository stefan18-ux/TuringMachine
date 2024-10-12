from engine import *
import sys

if len(sys.argv) > 1:
    arg = sys.argv[1]
else:
    arg = 3
if int(arg) > 10:
    arg = 10
set_instructions()
run_simulation(arg)
