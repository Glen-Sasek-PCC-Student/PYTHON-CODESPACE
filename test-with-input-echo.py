import builtins
import runpy
import sys

script, input_file = sys.argv[1:]
with open(input_file, encoding="utf-8") as source:
    def input(prompt=""):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        line = source.readline()
        if line == "":
            raise EOFError
        sys.stdout.write(line if line.endswith("\n") else line + "\n")
        sys.stdout.flush()
        return line.rstrip("\n")

    builtins.input = input
    sys.argv = [script]
    runpy.run_path(script, run_name="__main__")
