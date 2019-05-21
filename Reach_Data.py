import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_boston
boston = load_boston()
bs = pd.DataFrame(boston.data)
bs.columns = boston.feature_names
bs

x = bs['CRIM']
plt.hist(x, bins = 50);
plt.xlabel('something')
plt.ylabel('something else')
plt.title('some some')
plt.show()
