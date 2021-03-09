import argparse
import json

from json2html import *

parser = argparse.ArgumentParser()
parser.add_argument('-i',           help='path of input json')
parser.add_argument('-o',           help='path of output json')

def main(i, o):
    data = json.load(open(i, encoding='utf-8'))
    print(json2html.convert(json = data).encode("utf-8"))



if __name__ == '__main__':
  args = parser.parse_args()
  main(args.i, args.o)