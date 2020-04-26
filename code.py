# --------------
#Code starts here
import sys
def palindrome(num):
    numstr = str(num)
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
print(palindrome(9))



# --------------
#Code starts here
def a_scramble(str_1,str_2):
    result=True
    for i in (str_2.lower()):
        if i not in (str_1.lower()):
            result=False
            break
        str_1=str_1.replace(i,'',1) #Removing the letters from str_1 that are already checked
    
    return (result)
a_scramble("ticket","chat")


# --------------
#Code starts here
def check_fib(num):
    num1 = 1
    num2 = 1
    while True:
        if num2 <= num:
            if num2 == num:
                return True
            else:
                tempnum = num2
                num2 += num1
                num1 = tempnum
        else:
            return False

check_fib(145)




# --------------
#Code starts here
def compress(word):
    word=word.lower()
    mist=[]
    l=0
    while(l<len(word)):
        m=word[l]
        j=0
        while(l<len(word) and word[l]==m):
                 j=j+1
                 l=l+1    

        mist.append(m)
        mist.append(str(j))
    
    return ''.join(mist)



# --------------
#Code starts here
def k_distinct(string,k):
    a = set(string.lower())
    print(a)
    if len(a) == k:
        return True
    else:
        return False
k_distinct('banana',4)



