list= [1, 3, 2, 1, 4, 1, 3]
count={}
for i in list:
    count[i]=count.get(i,0)+1
print(count)
c={key:value for key,value in count.items() }


