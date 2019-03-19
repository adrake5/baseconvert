x=0
while x!=666:

    x = int(input("number to be converted?"))
    b = int(input("base of number being converted?"))
    print("conversion base for (",x,")",b," ?")
    c=int(input())



    if b<c:
        i=0
        e=len(str(x))-1
        conv=0
        for j in range(len(str(x))):
           d=str(x)[i]
           conv+=int(d)*(b**e)
           e-=1
           i+=1
    elif b>c:
        div=x
        conv=''
        while div>0:
            conv+=str(div%c)
            div=div//c
        conv=conv[::-1]
    else:
        conv = x
        print("That's easy!")


    print("(",x,")",b," = (",conv,")",c)
    print()

       
       
       
