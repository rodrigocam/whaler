import os
import argparse
from . import analyser


def main():
    parser = argparse.ArgumentParser(description='Analyse docker files.')
    parser.add_argument(
        'files', nargs='+',
        help='a list of files or folders to analyse'
    )

    args = parser.parse_args()
    for f in args.files:
        if os.path.isfile(f):
            analyser.process_file(f)
        else:
            analyser.process_folder(f)
