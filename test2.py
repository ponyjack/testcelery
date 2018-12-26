import pandas as pd

import time


now = time.time()
pd.read_csv("./stats.log")

print time.time() - now