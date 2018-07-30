import sys
import numpy as np
import pandas as pd

age = pd.read_csv(sys.argv[1], sep='\t')

mean_age = sum(age)/len(age)
assert mean_age < 100
assert mean_age > 10

np.savetxt("demeaned_" + sys.argv[1], age-mean_age)

print("done!")
