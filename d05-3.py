###############################################################################
# 5.3 example
# chap5 Getting Started with Pandas
# PYthon for Data Analysis
###############################################################################

import numpy as np
import pandas as pd

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],
                   index=["a", "b", "c", "d"],
                   columns=["one", "two"])


print(df)

print()
print( df.sum() )

print()
print( df.sum(axis="columns") )
