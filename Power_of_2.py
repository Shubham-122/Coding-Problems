def power_of_2(n):
    if n<0:
        return 'FaLSE'
    elif n&(n-1)==0:
        return 'TRUE'
    else:
        return 'FALSE'
    
print(power_of_2(16))