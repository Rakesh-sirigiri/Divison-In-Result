a = int(input("enter marks out of 300"))
b = a/300*100
print("percentage is:",b,"%")
if(a>300):
    print("you entered in wrong value")
elif a>60:
    print("your divison is first")
elif(a>50 and a<53):
    print("your divison is second")
elif(a>33 and a<50):
    print("your divison is third")
else:
    print("fail")
