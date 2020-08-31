import random
import os
a = [['_','_','_','_'],['_','_','_','_'],['_','_','_','_'],['_','_','_','_']]
schet = 0

def vyvod(a):
    spisok_max = []
    for i in range(len(a)):
        cc = []
        for j in range(len(a)):
            cc.append(len(str(a[j][i])))
        spisok_max.append(max(cc))
    for i in a:
        b = ''
        ch = 0
        for ii in i:
            b += '|' + (spisok_max[ch]-len(str(ii)))*'_' + str(ii)
            ch += 1
        b += '|'
        print(b)

def is_full(a):
    for i in a:
        for j in i:
            if j == '_':
                return False
    return True

def rand_hod(a): # a- pole, randomno stavit na pole chislo 2 ili 4
    b = [2,4]
    kk = []
    ch = 0
    for i in a:
        kk.append(list(i))
    a = kk
    while True:
        uslovie = random.randint(1,4)
        if uslovie <= 3:
            chislo = '2'
        else:
            chislo = '4'
        c = [random.randint(0,len(a)-1), random.randint(0,len(a)-1), chislo]
        if a[c[0]][c[1]] == '_':
            a[c[0]][c[1]] = c[2]
            return(a)
        if is_full(a):
            return(a)

def del_prob(a): #a - один список, который выполняет роль строки
    b = []
    for i in a:
        if i != '_':
            b.append(i)
    b.reverse()
    while len(b) != len(a):
        b.append('_')
    b.reverse()
    return(b)

def hod(a): # a - один список, который выполняет роль строки поля
    a = del_prob(a)
    a.reverse()
    cc = len(a)
    for i in range(cc):
        if i+1 < cc:
            if a[i] == a[i+1] and a[i] != '_':
                a[i] = str(int(a[i])+int(a[i+1]))
                a[i+1] = '_'
                a.reverse()
                a = del_prob(a)
                a.reverse()
        if a[i] == '_':
            break
    a.reverse()
    return(a)

def tup_to_list(a): #a - pole
    b = []
    for i in a:
        b.append(list(i))
    a = b
    return(a)

def igra(a,b): #a - pole; b - tip hoda(w,a,s,d)
    answ = []
    if b == 'd':
        for i in a:
            answ.append(hod(i))
        return(answ)
    if b == 'a':
        for i in a:
            i.reverse()
            cc = hod(i)
            cc.reverse()
            answ.append(cc)
        return(answ)
    if b == 's':
        a = list(zip(*a))
        for i in a:
            i = list(i)
            answ.append(hod(i))
        kk = tup_to_list(list(zip(*answ)))
        return(kk)
    if b == 'w':
        a = list(zip(*a))
        for i in a:
            i = list(i)
            i.reverse()
            cc = hod(i)
            cc.reverse()
            answ.append(cc)
        kk = tup_to_list(list(zip(*answ)))
        return(kk)
    else:
        return(a)

def score(a): #a - pole
    global schet
    for i in a:
        for j in i:
            if j != '_':
                schet += int(j)
                
            
            
                
        


a = rand_hod(a)
print('Ваш счет: ',schet)
vyvod(a)

while True:
    ss = input('vvedi tip hoda(w,a,s,d): ')
    a = igra(a, ss)
    a = rand_hod(a)
    os.system('cls')
    print('Ваш счет: ',schet)
    score(a)
    vyvod(a)

vyvod(a)
