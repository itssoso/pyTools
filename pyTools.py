import os
import csv
import json
import collections
import argparse

import constants

def delimitToJson(
  src, 
  dest=os.path.join('.', constants.DEFAULT_OUTPUT_FOLDER, constants.DEFAULT_JSON_OUTPUT), 
  delimiter='\t', 
  quotechar='"'):
  OrderedDict = collections.OrderedDict

  header = []
  data = []
  with open(src, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
    for row in reader:
      if header == []:
        header = row
        continue
      if row[0].strip()[0] == '#':
        continue
      row = filter(None, row)
      data.append(OrderedDict(zip(header, row)))

  with open(dest, 'w') as jsonfile:
    jsonfile.write(json.dumps(data, indent=2))

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  subparsers = parser.add_subparsers()

  # delimitToJson
  parser_delimitToJson = subparsers.add_parser('delimitToJson', help="Delimits file to JSON")
  parser_delimitToJson.add_argument('-s', '--src', required=True, help='source file')
  parser_delimitToJson.add_argument('-d', '--dest', help='destination file')
  parser_delimitToJson.set_defaults(func=delimitToJson)

  args = parser.parse_args()

  if args.func.__name__ == 'delimitToJson':
    if not os.path.exists(constants.DEFAULT_OUTPUT_FOLDER):
      os.makedirs(constants.DEFAULT_OUTPUT_FOLDER)
    args.func(args.src, args.dest)
