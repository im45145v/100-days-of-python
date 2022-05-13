#1
a=input("2 digit num")
x=int(a[0])+int(a[1])
print(x)
#2
w=input("weight in kg")
h=input("height in m")
print(int(int(w)/(float(h)**2)))
#3
age=int(input("your current age"))
#max age is 90 years
y=90-age
d,w,m=y*365,y*52,y*12
print(f"years ={y},months={m},weeks={w},days={d}")
#4
print("welcome to our tip calc")
cost=int(input("how much does it cost $"))
tipp=int(input("how much % tip u wanna give"))
peps=int(input("how many peps split it"))
bill=round(((cost+(cost*tipp)/100)/peps),2)
print(f"each should pay {bill}")
