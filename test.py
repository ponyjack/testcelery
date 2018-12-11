from lic.loadtask.slavetasks import StartSpaw



s = StartSpaw.apply_async((10,))
print(s)

