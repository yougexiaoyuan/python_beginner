#小院里的霍大侠 - 兴趣编程
#案例 -  打印彩色文本
#学习点： 
#colorama：这个模块类库主要功能是显示字体不同的颜色和背景
#Fore, Back, Style：Fore是针对字体颜色，Back是针对字体背景颜色，Style是针对字体格式
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)#初始化，设置自动恢复

print(Fore.BLUE+Back.YELLOW+"大家好，我的名字叫霍大侠。 "+ Fore.YELLOW+ Back.GREEN+"我梦想有个小院，院子里有一群朋友为了共同兴趣学习交流。")
print(Back.LIGHTBLUE_EX+"今天在我的小院，希望有兴趣朋友和我一起学习编程")
print(Fore.RED + Back.RED+ "和大家一起，每天学习一点点，编程改变自己，改变世界！")
input()