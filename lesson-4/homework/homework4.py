# 1
d = {'David': 11, 'Jack': 7, 'John': 2}
asc = sorted(d.items(), key = lambda x:x[1])
desc = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(asc)
print(desc)

# 2
d = {'David': 11, 'Jack': 7, 'John': 2}
d['Harry']=6
print(d)

# 3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

# 4 
n = 5
d = {x: x*x for x in range (1, n+1)}
print(d)

# 5
n = 15
d = {x: x*x for x in range (1, n+1)}
print(d)

# Set exercises
#1
s = {1,2,3,4,5,6}
print(s)

# 2
