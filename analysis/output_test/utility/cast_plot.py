import sys
import os
import subprocess

which = sys.argv[1]
conf = sys.argv[2:]

cmd_string = 'python plot.py ' 
if which == 'tau':
    for item in conf:
        cmd_string = cmd_string + '../tau_configuration_' + item + '.root '
if which == 'qcd':
    for item in conf:
        cmd_string = cmd_string + '../qcd_configuration_' + item + '.root '

print cmd_string
subprocess.call(cmd_string, shell = True)
