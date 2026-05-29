a=[1,3,4,5,6,]
print("type:",type(a))
print("len:",len(a))
print("sum:",sum(a))
print("reverse:",a[::-1])
print("reverse from 3 to 6:",a[:1:-1])
a[1:3]=["apple","Banana"]
print(a)
a.remove('apple')
print("remove funtion:",a)
a.insert(0,4)
print("insert funtion:",a)
a.append('graps')
print("append funtion:",a)

