# n 个人选取一支有队长的队伍
小Q所在的部门有n个人，要从这n个人中选任意数量的人组成一只队伍，再在这些人中选出一名队长，求不同的方案数对1e9+7取模的结果。如果两个方案选取的人的集合不同或者选出的队长不同，则认为这两个方案是不同的。

>输入  
一行一个数字n，1<=n <= 1e9  
输出  
一行一个数字表示答案  

>样例输入  
2  
样例输出  
4  

# 题目解析

又是一题数学题  
n个人选取不同的人数的队伍，即选取1, 2, 3... n个人，人数记为m，来当一个队伍  
每次分出的队伍还需要选取一位队长 m个人就会有m种可能性  
而选取m个人的时候，又会有Cnm种可能性

```python3
import math

def cnm(n, m):
	return math.factorial(n)/(math.factorial(m) * math.factorial(n-m))

n = int(input())

ret = 0
for i in range(n+1):
	ret += cnm(n,i)*i

print(ret)
```

# 总结

需要阶乘，这次知道了python里面的阶乘是math.factorial

还复习了一下Cnm和Anm  
Cnm = n!/(m!* (n-m)!)  
Anm = n!/(n-m)!  
Anm比Cnm少除以一个m!
