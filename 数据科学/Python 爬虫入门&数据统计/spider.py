import requests  # 发送请求
import pandas as pd  # 存取 excel 数据
import xlwings as xw  # 读写excel数据 
from time import sleep # 数据
#  在下拉的过程中 页面ajax动态刷新页面  get请求 返回特定的参数即可 
import json # json格式的数据 
from bs4 import BeautifulSoup  # 解析网页

title = []  # 电影名称
score = []  # 电影评分
regions = []  #地区
url = []  # 地址
release_date= []  # 发布日期
vote_count = []  # 评论人数

def get_movie_info(url, headers):
    """
    获取豆瓣电影详情数据
    :param url: 爬取地址
    :param headers: 爬取请求头
    :return: None
    """
    # 调用requests库，发送HTPP请求，访问特定的url，返回网页文件
    res = requests.get(url, headers=headers)
    # 使用BeautifulSoup进行HTML解析，方便根据类名，对电影相关信息，直接进行检索。
    soup = BeautifulSoup(res.text, 'html.parser')
    # 检索 item类
    for movie in soup.select('.item'):
        # 根据类名获取电影各个字段，并存储在列表中
        name = movie.select('.hd a')[0].text.replace('\n', '')  # 电影名称
        title.append(name)
        star = movie.select('.rating_num')[0].text  # 电影评分
        score.append(star)
        star_people = movie.select('.star span')[3].text  # 评分人数
        star_people = star_people.strip().replace('人评价', '')
        vote_count .append(star_people)




def save_to_file_pd(excel_name):
    """
    利用pandas将数据保存到excel
    :return: None
    """

    df = pd.DataFrame()  # 初始化一个DataFrame对象
    df['电影名'] =title
    df['评分'] = score
    df['地区'] = regions
    df['地址'] = url
    df['发布日期'] =release_date
    df['评论人数'] =vote_count
    df.to_excel(excel_name, encoding='utf_8_sig', index=False)  # 将数据保存为xlsx文件，不保存列索引

    

def save_to_file_xw(excel_name):
    """
    利用xlwings将数据保存到excel
    :return: None
    """

    app = xw.App(visible=True, add_book=False)
    wb = app.books.add()  # 新建工作簿
    sht = wb.sheets['sheet1']  # 选中表1
    columns=['电影名','评分','地区','地址','发布日期','评论人数']
    # 因为有9个列，所以选中Excel的A到I列
    ids = ['A1', 'B1', 'C1', 'D1', 'E1',' F1']
    movies = (title, score, regions, url, release_date, vote_count)
    for id, movie, column in zip(ids, movies, columns):
        movie.insert(0, column)
        # range()方法可以选中列，使用value属性设置这一整个列的值
        sht.range(id).options(transpose=True).value=movie

    wb.save(excel_name)
    wb.close()
    app.quit()

if __name__ =="__main__":
    # 爬取豆瓣喜剧电影排行榜前200部电影的相关信息
    df = pd.DataFrame(columns=['电影名','评分','地区','地址','发布日期','评论人数'])
    url = 'https://movie.douban.com/j/chart/top_list'  # 豆瓣电影地址
     # 利用 headers进行伪装
    headers =  {
        "User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    } 

     # 页面是ajax动态刷新的 每下拉到二十部 就刷新一次页面  所以181的下标 包含了前200部
    for num in range(0,181,20):   
        param = {
            'type': '24',
            'interval_id': '100:90',
            'action': '',
            'start': num,
            'limit': '20'
        }
         # 页面为get请求 可以在网站的headers中看到
        response = requests.get(url=url,params=param,headers=headers)  
        content=response.json()  # Content-Type 为 json格式的数据 
        length=len(content)
        for i in range(0,length):
            s = pd.Series({'电影名':content[i].get('title'),
                            '评分':eval(content[i].get('score')), 
                           '地区':content[i].get('regions')[0] , 
                           '地址':content[i].get('url'),
                           '发布日期':content[i].get('release_date'),
                           '评论人数':content[i].get('vote_count')
                          })
            # 这里必须选择ignore_index=True 或者给 Series 一个index值
            df = df.append(s, ignore_index=True)

        sleep(1)  # 等待1秒,防止反爬

    # 保存为excel文件
    df.to_excel('./douban_pd.xlsx',encoding='utf-8',index=False,index_label=None)
    df.to_excel('./douban_xw.xlsx',encoding='utf-8',index=False,index_label=None)