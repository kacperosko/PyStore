import os
from os.path import isfile, join


def main():
    path = os.getcwd()

    ts_files = [f for f in os.listdir(path) if isfile(join(path, f)) and f.endswith(".ts")]
    print(ts_files)
    os.chdir(path)
    del path

    for ts in ts_files:
        print("Running\n", "tsc " + ts)
        os.system("tsc " + ts)

    print("Compiled all TypeScript files")


if __name__ == "__main__": main()
