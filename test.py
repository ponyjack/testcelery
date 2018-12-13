from lic.loadtask.slavetasks import StartSpaw
import sys


def main(count, queue='celery'):
    print "i am strat"
    for _ in range(count):
        s = StartSpaw.apply_async((1,),queue=queue)
    print(s)
    print "i am end"


if __name__ == "__main__":
    if len(sys.argv) ==3:
        main(int(sys.argv[1]),sys.argv[2])
    else:
        main(int(sys.argv[1]))

