# @Time    : 2019/5/11 17:06
# @Author  : Seven
# @Email   : ysq96@126.com
# @File    : statistics_analyze.py
# @Software: PyCharm Community Edition

import pandas as pd
import matplotlib.pyplot as plt

catering_sale = './data/catering_sale.xls'
data = pd.read_excel(catering_sale, index_col=u'日期')
data = data[(data[u'销量']>400)&(data[u'销量']<5000)] # 过滤异常数据
statistics = data.describe()

statistics.loc['range'] = statistics.loc['max'] - statistics.loc['min']
statistics.loc['var'] = statistics.loc['std'] / statistics.loc['mean']
statistics.loc['dis'] = statistics.loc['75%'] - statistics.loc['25%']

print(statistics)
