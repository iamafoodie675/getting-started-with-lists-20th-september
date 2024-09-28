def sq(l):
    square = []
    for i in l:
        square.append(i*i)
        
    return square

li =[4,5,1,2,9,7,10,8]
print("Original list :",li)

res =sq(li)

print("Squared list: ",res)