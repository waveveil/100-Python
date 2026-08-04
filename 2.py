# print("please input the num that you want")
# print("\n")
# num = int(input())
# num_c = num
# for i in range(1, num):
#     num_c = num_c * i
# print(num_c)

"""
竟然一个函数的return返回结果还可以调用他自己所在的这个函数，还真实申请啊
"""
def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)
print("请输入一个数字：")
x = int(input())#好久没有用input() 函数了，都有些忘记了，现在有用起来，有一总好奇妙的感觉
print(fact(x))