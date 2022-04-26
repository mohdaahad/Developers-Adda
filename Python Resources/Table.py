from colorama import Fore, Back, Style,Cursor
import sys


print(Fore.GREEN+ Style.BRIGHT+"********Welcome To Tabel Program*********")
while True:
    try:
        a=int(input(Fore.BLUE+Style.BRIGHT+"Enter the number for chacke the tabel :"))
        if a==0:
            break
    except ValueError:
        print(Fore.RED+"Oops! That was no valid number. Try again.....")    
        sys.exit(0)
    sum=0
    odd=0
    even=0
    oddlist=[]    
    evenlist=[]
    prime=[]
    prime1=0
    noprime=[]

    for i in range(1,11):
        k=a*i
        print(Fore.WHITE+"",k,end=' ')
        sum=sum+k
        if k%2==0:
            even=even+1
            evenlist.append(k)
        else:
            odd=odd+1
            oddlist.append(k)
        if k>1:
            for r in range(2,k):
                if (k%r)==0:
                    noprime.append(k)
                    break
            else:
                prime.append(k)
                prime1=prime1+1
        else:
            prime.append(k)
            prime1=prime1+1
    print("")        
    print( Fore.LIGHTRED_EX +"Sum for tabel ==>", Fore.WHITE+"",sum)    
    print(Fore.WHITE+"Totel even value in tabel  ==>", Fore.WHITE+"",even)
    print(Fore.GREEN  +"Even value ==>",end=' ')
    for e in evenlist:
        print( Fore.WHITE+"",e,end=" ")
    print("")      
    print(Fore.LIGHTMAGENTA_EX +"Totel odd value in tabel ==>",Fore.WHITE+"",odd)
    if odd!=0:
        print(Fore.LIGHTCYAN_EX  +"Odd value ==>",end='')
        for o in oddlist:
          print(Fore.RESET+"", o,end=' ')
        print("")
    print(Fore.GREEN  +"Non-prime Number ==>",end=' ')
    for e in noprime:
        print( Fore.WHITE+"",e,end=" ")
    print("")     
    if prime1!=0:
        print(Fore.LIGHTCYAN_EX  +"Prime Number ==>",end='')
        for o in prime:
          print(Fore.RESET+"", o,end=' ')
        print("")         
    print(Fore.RED+"for exit pars",Fore.WHITE+"0",Fore.RED+"key")
    print(" ") 
    

  
