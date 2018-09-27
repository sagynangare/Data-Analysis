from matplotlib import style
#f=open('demo.txt','w+')
c=0
for i in style.available:
    print(i)
    c+=1
    #f.write(i+'\n')
#f.close()
print(c)
