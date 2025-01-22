def solution(n, m):
    if n % m == 0 or m % n == 0:
        gcd = min(n, m)
        lcm = max(n, m)
        return([gcd,lcm])
        
    else:
        gcd = 0
        lcm = 0
        result = [i for i in range(1,n+1) if n % i == 0]
        result2 = [i for i in range(1,m+1) if m % i == 0]
        for i in result:
            for j in result2:
                if i == j:
                    gcd = i
        for i in result:
            if i * gcd == n:
                result_lcm = i
        for i in result2:
            if i * gcd == m:
                result2_lcm = i 

        lcm = gcd * result_lcm * result2_lcm
        return([gcd,lcm])