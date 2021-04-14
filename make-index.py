""" Build index from directory listing
make_index.py ./docs
"""

import os
import argparse

EXCLUDED = ['index.md','header.md']

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    args = parser.parse_args()
    fnames = [remove_suffix(fname, ".md") for fname in sorted(os.listdir(args.directory))
              if fname not in EXCLUDED]
    with open("./docs/header.md","r") as f:
        index = open("./docs/index.md","w+")
        index.write(f.read())
        index.write(template(fnames))
        f.close()
        index.close()
def template(fnames):
    result = '\n\n### Table of contents:\n\n'
    for f in fnames:
        result += "* [{}]({})\n".format(f.capitalize(),f)
    return result
"""
In order to support those of us with vintage
python installations. 
From: https://stackoverflow.com/a/66683635
"""
def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string
if __name__ == '__main__':
    main()
