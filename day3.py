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
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill=0
if size == "S" : bill+=15
elif size == "M" : bill+=20
else : bill+=25
if add_pepperoni=="Y":
    if size=="s":bill+=2
    else:bill+=3
print(f"{bill}")
#6
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
cs=name1+name2
lcs=cs.lower()
t=lcs.count("t")
r=lcs.count("r")
u=lcs.count("u")
e=lcs.count("e")
truee=t+r+u+e
l=lcs.count("l")
o=lcs.count("o")
v=lcs.count("v")
e=lcs.count("e")
love=l+o+v+e
ls=int(str(truee)+str(love))
print(ls)
if ls<10 or ls>90 : print("\n high")
elif 40<=ls and 50>=ls : print("\n noice")
else: print("\n waste")
