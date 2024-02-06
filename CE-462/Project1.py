# Scenario 1 : 1 PL, Input Values
# q = stress on the footing (psf)
# PL = number of point loads acting on the footing
# B = Width of footing (ft)
# L = Length of footing (ft)
# A = Area of footing (sqr. ft)
# Q = Force at each point load acting on the footing (lb)
# v = Poisson's ratio
# x = Distance of wall from front of footing
# z2 - z8 = Various depths of soil (ft)

import math
 
q = 10000
PL = 1
B = 6
A = 36
Q = 36000
v = 0.35
x = 5
z2 = 2
z4 = 4
z6 = 6
z8 = 8

# Retaining wall coordinates
xW = 0
yW = 0

# Scenario 1 coordinates (in feet)
PL1 = (8,0)
PL1x = 8
PL1y = 0

# Plan view radial calculation, r^2 = x^2 + y^2 + z^2
r = 8

# R @ z2
R2 = math.sqrt(( PL1x ** 2 ) + ( PL1y ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft: ", R2)

R4 = math.sqrt(( PL1x ** 2 ) + ( PL1y ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft: ", R4)

R6 = math.sqrt(( PL1x ** 2 ) + ( PL1y ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft: ", R6)

R8 = math.sqrt(( PL1x ** 2 ) + ( PL1y ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft: ", R8)

# Stress Calculations Scenario 1 - SOMETHING IS WRONG WITH THESE, VALUES ARE TOO LOW, off by factor of 10

sigma2 = (Q * 3 * z2 * r ** 2 * R2 * ( 1 - 2*v))/(3.1415926 * R2 ** 2 * R2 **3 * (R2 + z2))
print("The stress at z = 2ft is: ", sigma2, "psf")

sigma4 = (Q * 3 * z4 * r ** 2 * R4 * ( 1 - 2*v))/(3.1415926 * R4 ** 2 * R4 **3 * (R4 + z4))
print("The stress at z = 4ft is: ", sigma4, "psf")

sigma6 = (Q * 3 * z6 * r ** 2 * R6 * ( 1 - 2*v))/(3.1415926 * R6 ** 2 * R6 **3 * (R6 + z6))
print("The stress at z = 6ft is: ", sigma6, "psf")

sigma8 = (Q * 3 * z8 * r ** 2 * R8 * ( 1 - 2*v))/(3.1415926 * R8 ** 2 * R8 **3 * (R8 + z8))
print("The stress at z = 8ft is: ", sigma8, "psf")


# Scenario 2 : 4 PL, Input Values
# q = stress on the footing (psf)
# PL = number of point loads acting on the footing
# B = Width of footing (ft)
# L = Length of footing (ft)
# A = Area of footing (sqr. ft)
# Q = Force at each point load acting on the footing (lb)
# v = Poisson's ratio
# x = Distance of wall from front of footing
# z2 - z8 = Various depths of soil (ft)

import math
 
q = 10000
PL = 4
B = 6
A = 36
Q = 9000
v = 0.35
x = 5
z2 = 2
z4 = 4
z6 = 6
z8 = 8

# Retaining wall coordinates
xW = 0
yW = 0

# Scenario 2 coordinates (in feet)
PL4a = (6.5,1.5)
PL4ax = 6.5
PL4ay = 1.5

PL4b = (9.5, 1.5)
PL4bx = 9.5
PL4by = 1.5

PL4c = (6.5, 1.5)
PL4cx = 9.5
PL4cy = 1.5

PL4d = (9.5, 1.5)
PL4dx = 9.5
PL4dy = 1.5


# Plan view radial calculation, R^2 = x^2 + y^2 + z^2
R = 8

# R @ z2
R2 = math.sqrt(( PL1x ** 2 ) + ( PL1y ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft: ", R2)

R4 = math.sqrt(( PL1x ** 2 ) + ( PL1y ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft: ", R4)

R6 = math.sqrt(( PL1x ** 2 ) + ( PL1y ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft: ", R6)

R8 = math.sqrt(( PL1x ** 2 ) + ( PL1y ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft: ", R8)

# Stress Calculations Scenario 1 - SOMETHING IS WRONG WITH THESE, VALUES ARE TOO LOW, off by factor of 10

sigma2 = (Q * 3 * z2 * 8 ** 2 * R2 * ( 1 - 2*v))/(3.1415926 * R2 ** 2 * R2 **3 * (R2 + z2))
print("The stress at z = 2ft is: ", sigma2, "psf")

sigma4 = (Q * 3 * z4 * 8 ** 2 * R4 * ( 1 - 2*v))/(3.1415926 * R4 ** 2 * R4 **3 * (R4 + z4))
print("The stress at z = 4ft is: ", sigma4, "psf")

sigma6 = (Q * 3 * z6 * 8 ** 2 * R6 * ( 1 - 2*v))/(3.1415926 * R6 ** 2 * R6 **3 * (R6 + z6))
print("The stress at z = 6ft is: ", sigma6, "psf")

sigma8 = (Q * 3 * z8 * 8 ** 2 * R8 * ( 1 - 2*v))/(3.1415926 * R8 ** 2 * R8 **3 * (R8 + z8))
print("The stress at z = 8ft is: ", sigma8, "psf")


