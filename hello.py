#for o in range(1,10):
#    print(o)
#
#y = 40

#for c in range (1,y):
#    if c % 3 == 0:
#        if c >= 6:
#            print (c)

#numbers = [2,4,6,8,10] #Sequence object iteration
#for n in numbers:
#    if n < 8:
#        print("Hello")
#    else:
#        print('n =',n)

#x = 5               # While iteration (if variable is contain true value)
#x += 5
#while x > 5:
#    print ("pt")

#x = 2               # While iteration (if variable value reaching while loop statement value) 
#while x < 5:
#    print ("pt")
#    x += 1

#i = 10
#while i > 4:
#     if i == 5:
#          i = 10
#     i -= 1
#     print(i)

#a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(a_list[:2])

#a = [1,2,3,4]
#b = a*2
#print(b)

#tup1 = (20,11,34,50) 
#print(tup1.count(100))

#list1 = [10,20,30,40]
#print(10 in list1)
#print(50 not in list1)

#list_array = [[1,2,3],[4,5,6],[7,8,9]]
#for item in list_array:
#  if item == [1,2,3]:
#    print("Hello!")
#    continue
#  print('item =',item) # 2D Array example


#---Dictionary methods---

#-Dict get
#dic = {'a':10,'b':20,'c':30,'d':40}
#a = dic.get('a') # fungsi get untuk mendapatkan value dari key a
#print(a)

#dic = {'a':10,'b':20,'c':30,'d':40}  #dengan default_value
#b = dic.get('z',0) # tidak terdapat key z dalam dictionary dic sehingga dikembalikan value 0
#print(b)

##-Dict Pop
dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
print(dic.pop('a')) # meremove key-value pair dengan key a
print(dic)

##-Dict Popitem 
## menghapus value-elemen secara acak/ yg terakhir
#dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
#print(dic.popitem())
#('d',40)

##-Dict Clear
#dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
#print(dic) 
#dic.clear() # meremove semua value dalam dictionary dic
#print(dic)

##-Dict Key
#dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
#print(dic.keys()) # mengakses seluruh key yang ada dalam dictionary

##-Dict Value
#dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
#print(dic.values()) # mengakses seluruh values yang ada dalam dictionary

##-Dict Clear
#dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
#print(dic.items()) # mengakses seluruh items yang ada dalam dictionary
#for str1,num, in dic.items():
#    print(str1,':',num)

#dic = {'w': 10,'x': 20,'y': 30}
#for str,elemens in dic.items():
#    if elemens > 10:
#        print("Hello!")

##-Dict Update
#dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
#print(dic)
#dic.update(a=90) # mengupdate value dari key a
#print(dic)