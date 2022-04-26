print("Chose Year pars 1 ")
print("Chose Day pars 2 ")
a=int(input("Enter the your choise: "))
if a==1:
    Year=float(input("Enter the Year: "))
    if Year%4==0:
        print("Year ==>",Year)
        print("Total Days in year ==>",Year*366)
        print("Total Week in year ==>",(Year*366)/7)
        print("Total Hour in year  ==>",Year*366*24)
        print("Total Minute in year  ==>",Year*366*24*60)
        print("Total Second in year  ==>",Year*366*24*60*60)
    else:
        print("Year ==>",Year)
        print("Total Days in year ==>",Year*365)
        print("Total Week in year ==>",(Year*365)/7)
        print("Total Hour in year  ==>",Year*365*24)
        print("Total Minute in year  ==>",Year*365*24*60)
        print("Total Second in year  ==>",Year*365*24*60*60)    
elif a==2:
    Day=float(input("Enter the Day: "))
    print("Total Days  ==>",Day)
    print("Total Week ==>",Day/7)
    print("Total Hour ==>",Day*24)
    print("Total Minute ==>",Day*24*60)
    print("Total Second ==>",Day*24*60*60)
else:
    print("chack the number")    
