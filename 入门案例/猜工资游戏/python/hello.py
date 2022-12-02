# 有个小院-兴趣编程
import random
def guessnum():
  n=random.randrange(1,100)
  print('请在1-100之间猜一个数字:')
  counter=0
  while True:
    counter+=1
    guess=int(input())
    if n<guess:
      print('猜大了!!!')
    elif n>guess:
      print('猜小了！！！')
    elif n==guess:
      print('恭喜你，下个月涨薪资!!!')
      print('你总共猜了%d次' %counter)
      break
  if counter>=8:
    print('很遗憾，涨薪资的机会渺茫!!!')
print('>>>>>=====-游戏开始-=====<<<<<')
guessnum()
while True:
  option=input('还想再闯关一次吗？(回答y或n)\n')
  yes='y'
  no='n'
  if option==yes:
    guessnum()
  elif option==no:
    print('>>>>>=====-游戏结束-=====<<<<<')
    break
  else:
    print('您的回答超出大脑!')
    print('>>>>>=====-游戏结束-=====<<<<<')