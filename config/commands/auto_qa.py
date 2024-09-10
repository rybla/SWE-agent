#!/root/miniconda3/bin/python

# @yaml
# signature: auto_qa <snippet>
# docstring: Does a code quality analysis, according to Ayeye Corp's in-house
#            conventions, on the given code snippet.
# arguments:
#   snippet:
#       type: string
#       description: The code snippet to be analyzed.
#       required: true

import argparse
import warnings

# tree_sitter is throwing a FutureWarning
warnings.simplefilter("ignore", category=FutureWarning)
from tree_sitter_languages import get_language, get_parser

parser = argparse.ArgumentParser(
    description="Does a code quality analysis, according to Ayeye Corp's in-house conventions, on the given code snippet."
)
parser.add_argument(
    "snippet",
    type=str,
    help="The code snippet to be analyzed",
)
args = parser.parse_args()

# We assume that all input files are Python.
parser = get_parser("python")
language = get_language("python")

# We assume that files are utf8 encoded.
print("args.snippet: ", args.snippet)
snippet_bytes = bytes(args.snippet, "utf8")
tree = parser.parse(snippet_bytes)

# collect results

results = []

# check for 1-character function definitions

query = language.query(
    """
(function_definition
  name: (identifier) @name
  parameters: _
  body: _
  )
""".strip()
)

captures = query.captures(tree.root_node)

for node, _ in captures:
    name = snippet_bytes[node.start_byte : node.end_byte].decode("utf8")
    if len(name) == 1:
        results.append(
            f"""
The function name `{name}` is just a single character! Please rename it to be a slightly longer and more descriptive name.
            """.strip()
        )


# print results

if len(results) == 0:
    print(
        """
All code quality warnings have been addressed! Please submit your changes now.
    """
    )
else:
    result_bullets = "\n".join([f"- {r}" for r in results])
    print(
        f"""
Code quality warnings:

{result_bullets}

Please address each of the warnings before submitting your changes.
    """.strip()
    )
