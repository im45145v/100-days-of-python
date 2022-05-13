#1
num=int(input("enter num "))
if num%2==0:
    print("even")
else:
    print("not even")
#2
age=int(input("your age "))
if age>10:
    h=int(input("how tall are you in cm"))
    if h>136:print("adult")
    elif h>108:print("normal")
    else:print("short")
else:print("kid")
#3
h=float(input("how tall are you in m"))
w=int(input("how weight are you in kg"))
bmi=round(w/h**2)
print(bmi)
if bmi<18.5:
    print("under weight")
elif bmi<25 :
    print("normal weight")
elif bmi<30 :
    print("bit more weight")
elif bmi<35 :
    print("obese")
else:print("lot of obese")
#4
year=int(input("year \t"))
if year%4==0 :
    if year%100==0:
        if year%400==0:print("leap")
        else:print("not leap")
    else:print("leap")
else:print("not leap")
#5
