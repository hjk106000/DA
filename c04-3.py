#############################################################
# chap04-3절 example
# chap04 그래프 그리기
# Do it! 데이터 분석을 위한 판다스 입문
#############################################################

import seaborn as sns
import matplotlib.pyplot as plt
# import pandas as pd

tips = sns.load_dataset('tips')
print(tips)
print(type(tips))

# plt.hist(tips['total_bill'], bins=10)
plt.hist(data=tips, x='total_bill', bins=10)
plt.suptitle('Histogram of Total Bill')
plt.show()

