def match_words(words):
    
    counter = 0
    lst = []
    
    for word in words:
        if len(word) >1 and word[0]==word[-1]:
            
            counter = counter + 1
            lst.append(word)
            
    print("List of words with first and last character same\n",lst)
    return counter 

li = ['abc','cfc','xyz','aba','1221',"nabilan","roser","nusaiban"]

count = match_words(li)

print("Number of words having the same fist and last:",count)