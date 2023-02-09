import pandas as pd
import xlwings as xw
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体，防止中文乱码
plt.rcParams["axes.unicode_minus"] = False  # 防止“-”负号的乱码问题


def show_country(data):
    # pandas数据处理
    country = data['地区'].str.split(' ', expand=True)  # 因为有的电影涉及到多个国家，所以将含有多个多家的每一项扩展开，方便统计国家的数目
    #这里会发现，共有六列，由此可见，在数据中一个电影只有1个国家
    part_columns = ['part1']  # 设置1个part
    country.columns = part_columns  # 设置列名
    country = country.apply(pd.value_counts).fillna(0)  # 统计每一个part中值出现的次数，同时将NaN填充为0，方便横向求和
    country['counts'] = country.apply(lambda x: x.sum(), axis=1)  # 横向求和，并添加一个新的列counts
    country = country.sort_values('counts', ascending=False)  # 按照counts将国家进行排列
    final_country = country.drop(columns=part_columns, inplace=False)  # drop掉引入的多余的part部分，只剩下counts
    # matplotlib绘图
    ## 柱形图 
    ### 使用xlwings将图的结果保存到excel中
    app = xw.App(visible=True, add_book=False)
    wb = app.books.open("./douban_pd.xlsx")
    sht = wb.sheets.add()
    
    fig1 = plt.figure(figsize=(20, 6))  # 设置画布大小
    plt.title("豆瓣喜剧电影涉及到的国家数量", )  # 为图像设置标题
    plt.xticks(rotation=45)  # 横轴刻度旋转45度，防止并排文字太挤而看不清楚
    plt.bar(final_country.index.values, country['counts'])  # 画柱形图的函数，其中需要传入横坐标，还有与其对应的纵坐标
    plt.savefig('country_bar.jpg')
    sht.pictures.add(fig1, name='BarPlot',left=0, top=0, update=True)
    ## 饼状图
    fig2 = plt.figure(figsize=(20, 6))
    plt.pie(final_country['counts'][:10], labels=final_country.index.values[:10], autopct='%1.1f%%', counterclock=False, startangle=45)
    plt.title('Top10-国家喜剧电影占比')
    plt.tight_layout()
    plt.savefig('country_pie.jpg')  # 保存到本地
    
    sht.pictures.add(fig2, name='PiePlot', left=0, top=400, update=True)

    wb.save()
    wb.close()
    app.quit()




if __name__ == '__main__':

    # 读取excel数据
    path = './douban_xw.xlsx'
    data = pd.read_excel(path)
    show_country(data=data)


    