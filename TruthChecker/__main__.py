import sys

from TruthChecker.src.Main import *

# MAIN SCRIPT :
if len(sys.argv) == 1:
    print("Ask me for something! : ./main [question]")
    exit(1)

question = create_question(sys.argv)
run(question)
