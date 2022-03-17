import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

FOLDER = 'random0'
MODEL = 'random0_108010'

data = list(pd.read_csv(f'{FOLDER}/{MODEL}.csv', header=None).loc[0])

x = {}

for i in list(dict.fromkeys(data)):
    x[i] = data.count(i)

print(np.mean(data))
print(np.percentile(data, 5))
print(np.percentile(data, 95))

print(np.std(data))

plt.bar(x.keys(), x.values())
plt.savefig(f'{FOLDER}/{MODEL}.png')
plt.show()