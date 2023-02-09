#小院里的霍大侠 - 兴趣编程
#案例 - 生成二维码
#学习点： 
#pyqrcode：生成二维码的函数库
#import：导入类库语法可以用import,和from ... import
import pyqrcode 
from pyqrcode import QRCode 
  
# 二维码其实都是一个网络地址生成的
s = "https://www.xfeater.com"
# 这个是二维码类库的创建二维码方法
url = pyqrcode.create(s) 
# 生成图形文件保存，可以是png,jpg等
url.svg("my_qr_code.png", scale = 8) 
print("一个my_qr_code.png的二维码图片文件已经生成到你的代码目录")
input()