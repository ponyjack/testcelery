from lic.loadtask.slavetasks import StartSpaw
import sys


def main(count):
    print "i am strat"
    for _ in range(count):
        s = StartSpaw.apply_async((1,))
    print(s)
    print "i am end"


if __name__ == "__main__":
    main(int(sys.argv[1]))

