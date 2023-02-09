import pandas as pd
import datetime
from datetime import date, timedelta
# 安装导入图形库plotly
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import statsmodels.api as sm
# 设置模板风格
pio.templates.default = "plotly_white"

# 1 准备好数据集包含两个关于两个营销活动（控制活动和测试活动）的数据文件
control_data = pd.read_csv("control_group.csv", sep=";")
test_data = pd.read_csv("test_group.csv", sep=";")


# 查看展示读取的内容
print(control_data.head())
print(test_data.head())

# 2 调整修改数据集中列名
control_data.columns = ["Campaign Name", "Date", "Amount Spent", "Number of Impressions",
                        "Reach", "Website Clicks", "Searches Received", "Content Viewed", "Added to Cart", "Purchases"]

test_data.columns = ["Campaign Name", "Date", "Amount Spent",
                     "Number of Impressions", "Reach", "Website Clicks",
                     "Searches Received", "Content Viewed", "Added to Cart",
                     "Purchases"]

print(control_data.isnull().sum())
print(test_data.isnull().sum())

# 3 查看数据是否空值等。做一些必要的数据填充
control_data["Number of Impressions"].fillna(value=control_data["Number of Impressions"].mean(),
                                             inplace=True)
control_data["Reach"].fillna(value=control_data["Reach"].mean(),
                             inplace=True)
control_data["Website Clicks"].fillna(value=control_data["Website Clicks"].mean(),
                                      inplace=True)
control_data["Searches Received"].fillna(value=control_data["Searches Received"].mean(),
                                         inplace=True)
control_data["Content Viewed"].fillna(value=control_data["Content Viewed"].mean(),
                                      inplace=True)
control_data["Added to Cart"].fillna(value=control_data["Added to Cart"].mean(),
                                     inplace=True)
control_data["Purchases"].fillna(value=control_data["Purchases"].mean(),
                                 inplace=True)

# 4 合并数据集
ab_data = control_data.merge(test_data,
                             how="outer").sort_values(["Date"])
ab_data = ab_data.reset_index(drop=True)
print(ab_data.head())

# 5 查看样本数据集活动数量，方便做测试评估
print(ab_data["Campaign Name"].value_counts())

# 6 我将首先分析我们从两个活动中获得的展示次数与在两个活动上花费的金额之间的关系
figure = px.scatter(data_frame=ab_data,
                    x="Number of Impressions",
                    y="Amount Spent",
                    size="Amount Spent",
                    color="Campaign Name",
                    trendline="ols")
figure.show()

# 7 根据在两个活动上花费的金额，控制活动。现在让我们看一下两个活动在网站上执行的搜索次数
label = ["Total Searches from Control Campaign",
         "Total Searches from Test Campaign"]
counts = [sum(control_data["Searches Received"]),
          sum(test_data["Searches Received"])]
colors = ['gold', 'lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Control Vs Test: Searches')
fig.update_traces(hoverinfo='label+percent', textinfo='value',
                  textfont_size=30,
                  marker=dict(colors=colors,
                              line=dict(color='black', width=3)))
fig.show()

# 8 测试活动导致在网站上进行了更多搜索。这两个活动的网站点击次数
label = ["Website Clicks from Control Campaign",
         "Website Clicks from Test Campaign"]
counts = [sum(control_data["Website Clicks"]),
          sum(test_data["Website Clicks"])]
colors = ['gold', 'lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Control Vs Test: Website Clicks')
fig.update_traces(hoverinfo='label+percent', textinfo='value',
                  textfont_size=30,
                  marker=dict(colors=colors,
                              line=dict(color='black', width=3)))
fig.show()

# 9 测试活动在网站访问次数。看看从两个活动到达网站后查看的内容量
label = ["Content Viewed from Control Campaign",
         "Content Viewed from Test Campaign"]
counts = [sum(control_data["Content Viewed"]),
          sum(test_data["Content Viewed"])]
colors = ['gold', 'lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Control Vs Test: Content Viewed')
fig.update_traces(hoverinfo='label+percent', textinfo='value',
                  textfont_size=30,
                  marker=dict(colors=colors,
                              line=dict(color='black', width=3)))
fig.show()

# 10 看一下两个活动中添加到购物车的产品数量；
# 对照活动的观众比测试活动观看了更多内容。虽然差别不大，但由于控制活动的网站点击率较低，因此其在网站上的参与度高于测试活动。
label = ["Products Added to Cart from Control Campaign",
         "Products Added to Cart from Test Campaign"]
counts = [sum(control_data["Added to Cart"]),
          sum(test_data["Added to Cart"])]
colors = ['gold', 'lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Control Vs Test: Added to Cart')
fig.update_traces(hoverinfo='label+percent', textinfo='value',
                  textfont_size=30,
                  marker=dict(colors=colors,
                              line=dict(color='black', width=3)))
fig.show()

# 11 看看在这两个活动上花费的金额
# 在测试活动上花费的金额高于控制活动。但正如我们所见，对照活动带来了更多的内容浏览量和购物车中的更多产品，对照活动比测试活动更有效。
label = ["Amount Spent in Control Campaign",
         "Amount Spent in Test Campaign"]
counts = [sum(control_data["Amount Spent"]),
          sum(test_data["Amount Spent"])]
colors = ['gold', 'lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Control Vs Test: Amount Spent')
fig.update_traces(hoverinfo='label+percent', textinfo='value',
                  textfont_size=30,
                  marker=dict(colors=colors,
                              line=dict(color='black', width=3)))
fig.show()

# 12 看看两个活动的购买情况
# 两个广告系列的购买量仅相差 1% 左右。由于控制活动以较少的营销费用实现了更多的销售额，因此控制活动在这里获胜！
label = ["Purchases Made by Control Campaign",
         "Purchases Made by Test Campaign"]
counts = [sum(control_data["Purchases"]),
          sum(test_data["Purchases"])]
colors = ['gold', 'lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Control Vs Test: Purchases')
fig.update_traces(hoverinfo='label+percent', textinfo='value',
                  textfont_size=30,
                  marker=dict(colors=colors,
                              line=dict(color='black', width=3)))
fig.show()

# 13 现在让我们分析一些指标，找出哪个广告活动转化率更高。我将首先查看网站点击次数与从两个活动中查看的内容之间的关系
# 测试活动中的网站点击次数较高，但控制活动中网站点击的参与度较高。所以控制活动获胜！
figure = px.scatter(data_frame=ab_data,
                    x="Content Viewed",
                    y="Website Clicks",
                    size="Website Clicks",
                    color="Campaign Name",
                    trendline="ols")
figure.show()

# 14 分析两个活动中查看的内容量与添加到购物车的产品数量之间的关系；控制活动再次获胜
figure = px.scatter(data_frame=ab_data,
                    x="Added to Cart",
                    y="Content Viewed",
                    size="Added to Cart",
                    color="Campaign Name",
                    trendline="ols")
figure.show()

# 15 现在让我们看一下添加到购物车的产品数量与两个活动的销售数量之间的关系
# 虽然控制活动导致更多的销售和购物车中的更多产品，但测试活动的对话率更高
figure = px.scatter(data_frame=ab_data,
                    x="Purchases",
                    y="Added to Cart",
                    size="Purchases",
                    color="Campaign Name",
                    trendline="ols")
figure.show()
