import sys

a=int(sys.argv[1]) 
b=int(sys.argv[2])
c=int(sys.argv[3])
m=(a+b+c)/3
s=a**2+b**2+c**2
print('Median (%d,%d,%d): %g' % (a,b,c,m)) 
print('Square sum (%d,%d,%d): %d' % (a,b,c,s))