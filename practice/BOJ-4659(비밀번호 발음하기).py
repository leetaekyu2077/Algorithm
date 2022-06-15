import sys

lst = []
vowel = ['a', 'e', 'i', 'o', 'u']

def have_vowel(password):
    if (('a' in password) or ('e' in password) or
        ('i' in password) or ('o' in password) or 
        ('u' in password)):
        return True
    else:
        return False
    
def consecutive_three(password):
    flag = -1
    v = 0
    c = 0
    for a in password:
        if a in vowel:
            if flag == 0: 
                v += 1
            else: 
                v = 1
                flag = 0
        else:
            if flag == 1:
                c += 1
            else:
                c = 1
                flag = 1
        
        if v >= 3 or c >= 3:
            return False
    return True

def consecutive_same(password):
    std = password[0]
    for i in range(1, len(password)):
        if password[i] == std and (password[i] != 'e' and password[i] != 'o'):
            return False
        std = password[i]        
    return True

while True:
    password = sys.stdin.readline().rstrip()
    if password == 'end':
        break
    else:
        lst.append(password)
        
for password in lst:
    while True:
        flag = have_vowel(password)
        if flag == False: break
        
        flag = consecutive_three(password)
        if flag == False: break
        
        flag = consecutive_same(password)
        if flag == False: break
        
        break
        
    if flag: print('<'+password+'>', 'is acceptable.')
    else: print('<'+password+'>', 'is not acceptable.')