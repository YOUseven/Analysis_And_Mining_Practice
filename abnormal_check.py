# @Time    : 2019/5/8 22:11
# @Author  : Seven
# @Email   : ysq96@126.com
# @File    : abnormal_check.py
# @Software: PyCharm Community Edition

import pandas as pd
import matplotlib.pyplot as plt

catering_sale='./data/catering_sale.xls' # 餐饮数据
data = pd.read_excel(catering_sale, index_col=u'日期') # 以日期为列索引
# print(data.describe()) # 描述数据
plt.rcParams['font.sans-serif'] = ['SimHei'] # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False # 显示正负号

plt.figure()
p = data.boxplot(return_type='dict')
x = p['fliers'][0].get_xdata() # fliers为异常值的标签
y = p['fliers'][0].get_ydata()
y.sort()

for i in range(len(x)):
    if i>0:
        plt.annotate(y[i], xy=(x[i],y[i]), xytext=(x[i]+0.05-0.8/
                                                   (y[i]-y[i-1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i],y[i]), xytext=(x[i]+0.08,y[i]))
plt.show()

