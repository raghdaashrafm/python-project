
try:
    def palindrome(word):

        opes=word[::-1]

        if word==opes:

            print("the number is Palindrome")

        else:

            print("the number is not Palindrome")
except:
    print('check again')

import re
def strin(a,b):
    sample = a.replace("*", ".*")
    if re.fullmatch(sample, b):
        return True
    else:
        return False


try:
    def find_occurrence (substring,string):
        find = string.find(substring)
        while find != -1:
            print(' found in index ',find)
            f=[]
            f.append(find)
            find= string.find(substring ,find+1)

        else:
            print('-1')
except:
    print('check again')