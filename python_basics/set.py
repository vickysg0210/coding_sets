# ---------------------------------------创建---------------
# 1. {} -> create
set1 = {"student", "teacher", 222, "student"}
print(len(set1)) #3
print(set1) #去重 {222, 'teacher', 'student'}

# 2. 用空set集合 set(), 表示空set不能用 set2 = {}
set2 = set()
print(set2) # set()

# 3. 用set()函数创建集合
set3 = set(("1", "2", 1, 2, 1)) #只能传入一个参数, 可以是list,tuple
print(set3) # {'2', 1, 2, '1'}
set4 = set("aaaaa")  #字符串是一个序列
print(set4) # a





