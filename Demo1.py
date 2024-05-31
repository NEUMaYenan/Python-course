'''定义函数：def语句，def my_abs(x):
如果已经把my_abs()函数定义保存在test1.py文件中，则可以用from test1 import my_abs来导入my_abs()函数。
对参数类型做检查，只允许整数和浮点数类型的参数，可以用内置函数isinstance()来实现.
raise raise的基本语法结构raise exceptionName (reason) exceptionName ：异常名称，须是定义好的错误类型，或本身存在的错误类型；
raise TypeError('bad operand type')'''
'''import math
from test1 import my_abs , move
print(my_abs(-9))
x,y=move(100,100,60,math.pi/6)
print('%.2f %.2f'%(x,y))
from test1 import quadratic
print('quadratic(2,3,1)=',quadratic(2,3,1))
print('quadratic(1,3,-4)=',quadratic(1,3,-4))'''
'''from test1 import findMinAndMax
if findMinAndMax([])!=(None,None):
    print('测试失败！')
elif findMinAndMax([7])!=(7,7):
    print('测试失败！')
elif findMinAndMax([7,1])!=(1,7):
    print('测试失败！')
elif findMinAndMax([7,1,3,9,5])!=(1,9):
    print('测试失败！')
else:print('测试成功！')'''

