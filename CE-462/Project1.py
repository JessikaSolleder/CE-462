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

# Plan view radial calculation, r^2 = x^2 + y^2 (in feet)
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


# Plan view radial calculation, r^2 = x^2 + y^2 (in feet)
r4a = 6.6708
r4b = 9.6177
r4c = 6.6708
r4d = 9.6177


# R @ z2
R2a = math.sqrt(( PL4ax ** 2 ) + ( PL4ay ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft at PL a: ", R2a)

R2b = math.sqrt(( PL4bx ** 2 ) + ( PL4by ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft at PL b: ", R2b)

R2c = math.sqrt(( PL4cx ** 2 ) + ( PL4cy ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft at PL c: ", R2c)

R2d = math.sqrt(( PL4dx ** 2 ) + ( PL4dy ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft at PL d: ", R2d)


# R @ z4
R4a = math.sqrt(( PL4ax ** 2 ) + ( PL4ay ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft at PL a: ", R4a)

R4b = math.sqrt(( PL4bx ** 2 ) + ( PL4by ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft at PL b: ", R4b)

R4c = math.sqrt(( PL4cx ** 2 ) + ( PL4cy ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft at PL c: ", R4c)

R4d = math.sqrt(( PL4dx ** 2 ) + ( PL4dy ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft at PL d: ", R4d)


#R @ z6
R6a = math.sqrt(( PL4ax ** 2 ) + ( PL4ay ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft at PL a: ", R6a)

R6b = math.sqrt(( PL4bx ** 2 ) + ( PL4by ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft at PL b: ", R6b)

R6c = math.sqrt(( PL4cx ** 2 ) + ( PL4cy ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft at PL c: ", R6c)

R6d = math.sqrt(( PL4dx ** 2 ) + ( PL4dy ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft at PL d: ", R6d)


#R @ z8
R8a = math.sqrt(( PL4ax ** 2 ) + ( PL4ay ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft at PL a: ", R8a)

R8b = math.sqrt(( PL4bx ** 2 ) + ( PL4by ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft at PL b: ", R8b)

R8c = math.sqrt(( PL4cx ** 2 ) + ( PL4cy ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft at PL c: ", R8c)

R8d = math.sqrt(( PL4dx ** 2 ) + ( PL4dy ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft at PL d: ", R8d)


# Stress Calculations Scenario 2 - SOMETHING IS WRONG WITH THESE, VALUES ARE TOO LOW

sigma2a = (Q * 3 * z2 * r4a ** 2 * R2a * ( 1 - 2*v))/(3.1415926 * R2a ** 2 * R2a **3 * (R2a + z2))
sigma2b = (Q * 3 * z2 * r4b ** 2 * R2b * ( 1 - 2*v))/(3.1415926 * R2b ** 2 * R2b **3 * (R2b + z2))
sigma2c = (Q * 3 * z2 * r4c ** 2 * R2c * ( 1 - 2*v))/(3.1415926 * R2c ** 2 * R2c **3 * (R2c + z2))
sigma2d = (Q * 3 * z2 * r4d ** 2 * R2d * ( 1 - 2*v))/(3.1415926 * R2d ** 2 * R2d **3 * (R2d + z2))
sigma2abcd = sigma2a + sigma2b + sigma2c + sigma2d
print("The total stress at z = 2ft is: ", sigma2abcd, "psf")


sigma4a = (Q * 3 * z4 * r4a ** 2 * R4a * ( 1 - 2*v))/(3.1415926 * R4a ** 2 * R4a **3 * (R4a + z4))
sigma4b = (Q * 3 * z4 * r4b ** 2 * R4b * ( 1 - 2*v))/(3.1415926 * R4b ** 2 * R4b **3 * (R4b + z4))
sigma4c = (Q * 3 * z4 * r4c ** 2 * R4c * ( 1 - 2*v))/(3.1415926 * R4c ** 2 * R4c **3 * (R4c + z4))
sigma4d = (Q * 3 * z4 * r4d ** 2 * R4d * ( 1 - 2*v))/(3.1415926 * R4d ** 2 * R4d **3 * (R4d + z4))
sigma4abcd = sigma4a + sigma4b + sigma4c + sigma4d
print("The total stress at z = 4ft is: ", sigma4abcd, "psf")

sigma6a = (Q * 3 * z6 * r4a ** 2 * R6a * ( 1 - 2*v))/(3.1415926 * R6a ** 2 * R6a **3 * (R6a + z6))
sigma6b = (Q * 3 * z6 * r4b ** 2 * R6b * ( 1 - 2*v))/(3.1415926 * R6b ** 2 * R6b **3 * (R6b + z6))
sigma6c = (Q * 3 * z6 * r4c ** 2 * R6c * ( 1 - 2*v))/(3.1415926 * R6c ** 2 * R6c **3 * (R6c + z6))
sigma6d = (Q * 3 * z6 * r4d ** 2 * R6d * ( 1 - 2*v))/(3.1415926 * R6d ** 2 * R6d **3 * (R6d + z6))
sigma6abcd = sigma6a + sigma6b + sigma6c + sigma6d
print("The total stress at z = 6ft is: ", sigma6abcd, "psf")

sigma8a = (Q * 3 * z8 * r4a ** 2 * R8a * ( 1 - 2*v))/(3.1415926 * R8a ** 2 * R8a **3 * (R8a + z8))
sigma8b = (Q * 3 * z8 * r4b ** 2 * R8b * ( 1 - 2*v))/(3.1415926 * R8b ** 2 * R8b **3 * (R8b + z8))
sigma8c = (Q * 3 * z8 * r4c ** 2 * R8c * ( 1 - 2*v))/(3.1415926 * R8c ** 2 * R8c **3 * (R8c + z8))
sigma8d = (Q * 3 * z8 * r4d ** 2 * R8d * ( 1 - 2*v))/(3.1415926 * R8d ** 2 * R8d **3 * (R8d + z8))
sigma8abcd = sigma8a + sigma8b + sigma8c + sigma8d
print("The total stress at z = 8ft is: ", sigma8abcd, "psf")
