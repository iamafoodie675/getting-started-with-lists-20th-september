l = [4,5,1,2,9,7,10,8]
print("original list:",l)

count = 0

for i in l:
    count = count +i
avg = count/len(l)

print("sum =",count)
print("average =",avg)

l.sort()
print(l)

print("smallest element is:",l[0])
print("largest element is:",l[-1])
