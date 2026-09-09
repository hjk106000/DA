#############################################################
# chap05-2절 example
# chap05 깔금한 데이터 만들기
# Do it! 데이터 분석을 위한 판다스 입문
#############################################################

import pandas as pd

pew = pd.read_csv('./DA/data/pew.csv')
# print(pew)
# print(type(pew))

pew_long = pew.melt(id_vars='religion', 
                    var_name='income', value_name='count')
print(pew_long)



