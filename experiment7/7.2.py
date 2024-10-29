# 运⾏下⾯的程序，在当前⽂件夹中⽣成饭店营业额模拟数据⽂件data.csv。


# import csv
# import random
# import datetime
#
# fn = 'data.csv'
# with open(fn, 'w', encoding='UTF-8') as fp:
#     # 创建 csv 文件写入对象
#     wr = csv.writer(fp)
#     # 写入表头
#     wr.writerow(['日期', '销量'])
#     # 生成模拟数据
#     startDate = datetime.date(2017, 1, 1)
#     # 生成 365 个模拟数据，可以根据需要进行调整
#     for i in range(365):
#         # 生成一个模拟数据，写入 csv 文件
#         amount = 300 + i * 5 + random.randrange(100)
#         wr.writerow([str(startDate), amount])
#         # 下一天
#         startDate = startDate + datetime.timedelta(days=1)

# 1)使⽤ pandas读取⽂件data.csv中的数据，创建DataFrame对象，并删除其中所有缺失值;
import pandas as pd

df = pd.read_csv('data.csv')
df.dropna(inplace=True)
print(df)

# 2)使⽤ matplotlib ⽣成折线图，反应该饭店每天的营业额情况，并把图形保存为本地⽂件first.jpg;

import matplotlib.pyplot as plt

plt.plot(df['日期'], df['销量'])
plt.savefig('first.jpg')

# 3)按⽉份进⾏统计，使⽤matplotlib绘制柱状图显⽰每个⽉份的营业额，并把图形按⽉份进⾏统计，找出相邻两个⽉最⼤涨幅，并把涨幅最⼤的⽉份写⼊⽂件maxMonth.txt;



# 4)按季度统计该饭店2017年的营业额数据，使⽤ matplotlib ⽣成饼状图显⽰ 2017 年4个季度的营业额分布情况，并把图形保存为本地⽂件third.jpg。




