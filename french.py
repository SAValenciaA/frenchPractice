from translate import practice
import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="Command line french practice app.")
    parser.add_argument("-f","--translate-from",metavar="",help="Practice translating from french")
    parser.add_argument("-t","--translate-to",metavar="",help="Practice translating to french")
    parser.add_argument("-b","--bitacora",help="Practice french words from the bitacora")
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    if args.translate_from:
        practice(int(args.translate_from), "TRANSLATE TO ENGLISH")
    elif args.translate_to:
        practice(int(args.translate_to),  "TRANSLATE TO FRENCH")
    elif args.bitacora:
        print("bitacora")

if __name__ == "__main__":
    main()
