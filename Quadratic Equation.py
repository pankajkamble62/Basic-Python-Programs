
import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
# Calculating the discriminant  
d = (b**2) - (4*a*c)  
  
Root1 = (-b-cmath.sqrt(d))/(2*a)  
Root2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(Root1,Root2))   