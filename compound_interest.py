principle=0
rate=0
time=0

while principle<=0:
    principle=float(input("Enter principle Amount: "))
    if principle<0:
        print("Principle amount cannot be less than zero")
    else:
        break

while rate<=0:
    rate=float(input("Enter interest rate: "))
    if rate<0:
        print("Rate cannot be less than zero")
    else:
        break

while time<=0:
    time=float(input("Enter time in  years: "))
    if time<0:
        print("Time cannot be less than zero")
    else:
        break
        
total= principle*pow((1+rate/100),time)
print(f"Balance after {time} year/s is: ${total:2f}")
        

        
    