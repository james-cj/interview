"""
输入任意N个数，返回K个最小的数。返回的形式可以是：
a) 逐个返回数字，输出在同一行
b) 逐个返回字符串，输出在同一行
c) 返回一个包含k个最小数的数组
"""
x = [int(i) for i in input().split()]
k = x[-1]
x.remove(x[-1])
x.sort()
print(' '.join(list(map(str,x[:k]))))


# a = list(map(int, input().split()))
# lists, k = a[:-1], a[-1]
# print(" ".join(list(map(str, sorted(lists)[:k]))))
