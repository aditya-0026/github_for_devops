a=int(input('enter the no.:'))
if (a<0):
    print('no. is -ve!!')
elif(a>0):
    if(a<=10):
        print("no. is between 0-10")
    elif(a<=30):
        print("no. is between 10-30")
    else:
        print("no. is greater than 30")
else:
    print("no. is zero")
    