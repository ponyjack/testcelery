from lic.loadtask.slavetasks import StartSpaw

print "i am strat"
s = StartSpaw.apply_async((10,))
print(s)
print "i am end"
