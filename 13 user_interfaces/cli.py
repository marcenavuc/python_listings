import argparse

parser = argparse.ArgumentParser(description="Some argument Parser")

parser.add_argument("some_arg", type=int, help="Help please!!")
parset.add_argument("-v", "--verbose", help="increase output verbosity")

args = parser.parse_args()

