#!/usr/bin/env python3
import argparse
import breathing

parser = argparse.ArgumentParser()
parser.add_argument("--standing", type=bool, default=None, help="whether the user is standing")
args = parser.parse_args()

if args.standing is not None:
    standing = args.standing
else:
    standing_response = input("Are you standing? (y/n)")
    if standing_response.lower() == "y":
        standing = True
    else:
        standing = False

calm.calm(10, standing=standing)
