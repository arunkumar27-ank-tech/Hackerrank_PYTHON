def scoreword(words):
    totalcount = 0
    for word in words:
        count = 0
        for letter in word:
            if letter in 'aeiouy':
                count+=1
        if count %2==0:
            totalcount +=2
        else:
            totalcount +=1
    return totalcount

n = int(input())
words = str(input()).split()
print(scoreword(words))