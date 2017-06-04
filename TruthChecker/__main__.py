import sys

from TruthChecker.Main import create_question, run

if len(sys.argv) == 1:
    print("Ask me for something! : ./main [question]")
    exit(1)

question = create_question(sys.argv)
run(question)
