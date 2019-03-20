
#Fills a list of number and letter characters for use in systems of base>10
num=[]
i=0
for i in range(ord('0'),ord('9')+1,1):
    num.append(chr(i))
for i in range(ord('A'),ord('Z')+1,1):
    num.append(chr(i))
for i in range(ord('a'),ord('z')+1,1):
    num.append(chr(i))
	
    





x=''
while x!=str('666'):

    #Input number,scroll through character lists, enter position/value of characters into 'conv' list
    x = input("number to be converted?")
    conv=[];maxvalue=0;i=0
    for i in range(len(x)):
        j=0
        while num[j]!=x[i]:
            j+=1
        conv.append(j)
        if j>maxvalue:
            maxvalue=j

    b=0    
    while b<maxvalue:
        b = int(input("base of number being converted?"))
        if b<maxvalue:
            print("something's wrong bra ,,, u got a digitary value higher than your base.")
            print("try again.")
     
    print("conversion base for (",x,")",b," ?")
    c=int(input())


    #First convert input number into base10/decimal 
    dec_conv=0
    e=len(conv)-1
    for j in range(len(conv)):
        dec_conv+=int(conv[j])*(b**e)
        e-=1
    
    #Next convert base10 into conversion base
    c_conv=[]
    div=dec_conv
    while div>0:
        c_conv.append(str(div%c))
        div=div//c
    c_conv=c_conv[::-1]

    #Finally for each numeral value in c_conv, convert into its character representation from the initial 'num' list
    final_conv=''
    for i in range(len(c_conv)):
        final_conv+=num[int(c_conv[i])]
        

    print("(",x,")",b," = (",final_conv,")",c)
    print()

       
       
       
