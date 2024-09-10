#!/root/miniconda3/bin/python

# @yaml
# signature: translate_ipsentiloese <file_path>
# docstring: Translate a string from Ipsentiloese to English.
# arguments:
#   input:
#       type: string
#       description: The string to translate
#       required: true

import argparse
import warnings

warnings.simplefilter("ignore", category=FutureWarning)

parser = argparse.ArgumentParser(
    description="Translate a string from Ipsentiloese to English."
)
parser.add_argument("input", type=str, help="The string to translate.")
args = parser.parse_args()

alphabet = [c for c in "abcdefghijklmnopqrstuvwxyz"]


def translate(s: str):
    cs = []
    for c in s:
        try:
            cs.append(alphabet[(alphabet.index(c) - 1) % len(alphabet)])
        except ValueError:
            cs.append(c)
    return "".join(cs)


print(translate(args.input))
