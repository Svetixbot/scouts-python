#!/usr/bin/python

import sys
import pyfpm
import re
import os

def run(input, output):
  with open(output, 'w+') as out:
    with open(input) as f:
        f.next()
        nextF = f
        nextF.next()
        for line, nextLine in zip(f, nextF):
          lost = loss(parseLine(line), parseLine(nextLine))
          if lost is not None:
            out.write(lost + os.linesep)
        
def parseLine(line):
  lines = line.split(",")
  lines[3] = re.search('"(\d{4}.+\d{1})"', lines[3]).group(1)
  lines[4] = re.search('"(\d{4}.+\d{1})"', lines[4]).group(1)
  return lines

def loss(line, nextLine):
  if line[0] == nextLine[0] and line[1] == nextLine[1] and line[4] != nextLine[3]:
    return line[0] + "," + line[1] + "," + line[4] + "," + nextLine[3]

run(sys.argv[1], sys.argv[2])