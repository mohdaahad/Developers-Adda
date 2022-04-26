from datetime import datetime
today = datetime.now()
d1 = today.strftime("%d/%m/%Y %H:%M:%S")
print("Now date and time:", d1)
k=0
l=0
d1=int(today.strftime("%Y"))
d2=int(today.strftime("%m"))
d3=int(today.strftime("%d"))
d4=int(today.strftime("%H"))
d5=int(today.strftime("%M"))
d6=int(today.strftime("%S"))
for a in range(1,d1+1):
    if a%4==0:
        k=k+1
for i in range(1,d2):
    if 1==i:
        l=l+31
    elif 2==i:
        l=l+28
    elif 3==i:
        l=l+31
    elif 4==i:
        l=l+30        
    elif 5==i:
        l=l+31    
    elif 6==i:
        l=l+30    
    elif 7==i:
        l=l+31        
    elif 8==i:
        l=l+31
    elif 9==i:
        l=l+30
    elif 10==i:
        l=l+31
    elif 11==i:
        l=l+30
    elif 12==i:
        l=l+31

day=(d1-1)*365+k+d3-1+l
week=(day)/7
hour=(day)*(24+d4)
minuts=(hour)*(60+d5)
second=(minuts)*(60+d6)
print("Year ==>",d1)
print("Day ==>",day)
print("Week ==>",week)
print("Hour ==>",hour)
print("Minuts ==>",minuts)
print("Second ==>",second)
c=0
while day>0:
    day=day//10
    c=c+1
print("diget in day",c)    



