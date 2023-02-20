import glob
import os

print(glob.glob("/home/adam/*"))
def main():
    path = os.getcwd()
    ts_files = glob.glob(path + "/*.ts")

    for ts in ts_files:
        os.system("tsc " + ts)

if __name__ == "__main__":
    main()

