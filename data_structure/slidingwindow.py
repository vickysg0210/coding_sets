def findSubstring(s):
    N = len(s) #数组/字符串长度
    left, right = 0, 0 #双指针, 表示当前遍历的区间[left, right], 闭区间
    counter = collections.Counter() #用于统计 子数组/子区间是否有效
    res = 0 #result
    while right < N: # 搜索直到 数组/字符串 的结尾
        counter[s[right]] += 1 #增加当前右指针的element计数
        while 区间[left, right] 不符合题意: 
            counter[s[left]] -= 1
            left += 1 #真正的移动左指针
        res = max(res, right-left+1)
        right += 1
    return res