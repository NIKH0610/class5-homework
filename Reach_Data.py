import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_boston
boston = load_boston()
bs = pd.DataFrame(boston.data)
bs.columns = boston.feature_names
bs

x = bs['AGE']
plt.hist(x,bins = 20);
plt.xlabel('AGE')
plt.ylabel('NO. OF PEOPLE')
plt.title('AGE v/s PEOPLE')
plt.show()

y = bs['TAX']
plt.scatter(x,y,marker = '*')
plt.xlabel('AGE')
plt.ylabel('TAX PAID')
plt.title('AGE v/s TAX')
plt.show()



