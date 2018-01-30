#!/usr/bin/python

import readline
import subprocess
import os
readline.write_history_file('file1.txt')
P = subprocess.Popen(['hostname '], stdout=subprocess.PIPE, shell=True)








