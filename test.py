from lic.loadtask.slavetasks import StartSpaw

print "i am strat"
while True:
    s = StartSpaw.apply_async((1,))
print(s)
print "i am end"
