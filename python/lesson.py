# 模块
# import语句
# 几种方式
import module
import module.function_1
from module import function_1, Class_a
from module import * # 将模块中的所有函数导入命名空间，如非必要不推荐使用
from . import echo
from .. import formats
from ..filters import equalizer

# __name__属性
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')
'''   
每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。

说明：__name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格。
'''

# dir()函数
# 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回
import nr, sys
dir(nr)

# 包
# 多个函数和类组成子模块，多个子模块组成包

# 输入和输出
# 输入和输出
input() # 输入函数
print() # 输出函数
def f(x):
    print('hello, {}'.format(x)) # format函数，实现字符串格式化

# 读和写文件(略)
f = open(filename, mode)
f.read()

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

'''
通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。

通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
'''
pickle.dump(obj, file, [,protocol])
x = pickle.load(file)

# File(略)
# OS(略)
 
# 错误和异常
# 语法错误
# 异常
# 异常处理
while True:
        try:
            x = int(input("Please enter a number: ")) # 若是一切正常则执行该语句
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again   ")# 若是遇到报错则执行该语句

# 抛出异常（略）
# 用户自定义异常（略）
# 定义清理行为（略）
# 预定义的清理行为（略）


