# enumerate 
# 1. 对于iterable/遍历的对象(list/string), enumberate将其组成一个索引序列,利用它可以同时获得索引和值
# 2. enumerate多用于for loop得到计数
# e.g. to a sequence => (0, seq[0]), (1, seq[1]), (2, seq[2]) 
for index, item in enumerate(list1):
    print index, item
# 3. enumerate还可以接收第二个参数, 用于指定索引起始值
for index, item in enumerate(list1, 1):
    print index, item