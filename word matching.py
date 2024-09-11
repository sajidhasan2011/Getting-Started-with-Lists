def match_words(words):
    
    count = 0 
    lst = []
    
    for word in words :
        if len(words) > 1 and word[0] == word[-1]:
            count = count + 1
            lst.append(word)
            
    print("List of words with first and last character same\n",lst)
    return count

li = ["abc","cfc","xyz","aba","1221","sajidss","safwanss","nahianss","afnanss"]
word = match_words(li)

print("Number of words having first and last Charcter Same", word)