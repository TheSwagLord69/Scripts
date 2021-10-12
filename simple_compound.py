def c_interest(a,b,c): #principle, interest, no. of times
    print("\n[*] Compounding "+str(b)+" times with "+str(c)+"% interest, rounded to 3 SF.\n") #debug
    print("$"+str(round(a,3))+" (Principle amount)") #debug
    for i in range(c):
        a = a*b
        print("$"+str(round(a,3)) + " (Compounded "+str(i)+" time(s))") #debug
    return(a)

def main():
    print('Enter principle ($):')
    principle = float(input())

    print('Enter interest per compound (%):')
    interest = float(input())
    oginterest = str(interest)
    interest = ((interest+100)/100)
    
    print('Enter number of times compounded:')
    number = int(input())
    
    finalamount = c_interest(principle, interest, number)
    
    print("\n$" + str(principle) + " became $" + str(round(finalamount,2)) + " after compounded " + str(number) + " times at " + str(oginterest) +"% interest.")
    
if __name__ == "__main__":
    main()
