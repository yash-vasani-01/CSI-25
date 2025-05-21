
def print_pattern1(n):
    for i in range(n):
        for j in range(i+1):
            print('* ',end='')   
        print()
        
def print_pattern2(n):
    for i in range(n):
        for k in range(n-i,1,-1):
            print(' ',end='')
        
        for j in range(i+1):
            print('* ',end='')
        
        print()
        
            
            
n=int(input('Enter a No of Row:'))
print('Pattern 1')
print_pattern1(n)

print('pattern 2')
print_pattern2(n)
