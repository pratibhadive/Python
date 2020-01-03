from flask import Flask, request #import main Flask class and request object
import math

app = Flask(__name__) #create the Flask app
def power(x, y) :

    if (y == 0) :
        return 1
    elif (y % 2 == 0) :
        return(power(x, y // 2) *
               power(x, y // 2))
    else :
        return(x * power(x, y // 2) *
                power(x, y // 2))

def sieveOfEratosthenes(n, isPrime) : 
      
    isPrime[0] = isPrime[1] = False
    for i in range(2, n+1) : 
        isPrime[i] = True
          
    p=2
    while(p * p <= n) : 
          
        if (isPrime[p] == True) : 
              
            i=p*2
            while(i <= n) : 
                isPrime[i] = False
                i = i + p 
                  
        p = p + 1
def leftTruPrime(n) : 
    temp = n 
    cnt = 0
  
    while (temp != 0) : 
          
        cnt=cnt + 1 
          
        temp1 = temp % 10;  
        if (temp1 == 0) : 
            return False 
          
        temp = temp // 10
  
    isPrime = [None] * (n + 1) 
    sieveOfEratosthenes(n, isPrime) 
  
    for i in range(cnt, 0, -1) : 
      
        mod = power(10, i) 
  
        if (isPrime[n % mod] != True) :  
              
            return False 
              
    return True 
  
def rightTruPrime(n) :
    isPrime=[None] * (n+1)
    sieveOfEratosthenes(n, isPrime)

    while (n != 0) :
        if (isPrime[n]) :
            n = n // 10
        else :
            return False

    return True
@app.route('/<int:n>', methods=['GET'])
def left(n):
    n = abs(int(n))
    if (leftTruPrime(n) and rightTruPrime(n)) : 
        print(n, "is left truncatable prime") 
        return '''<h1>{} is a Prime Number</h1>'''.format(n)
    else : 
        print(n, "is not left truncatable prime") 
        return '''<h1>{} is a NOT Prime Number</h1>'''.format(n)

app.run()

