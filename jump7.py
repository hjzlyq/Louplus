n = 1
while n <= 100:
    if n % 7 == 0 or n % 10 == 7 or n // 10 == 7:
        n = n + 1
        continue
    print(n)
    n += 1
    
   
