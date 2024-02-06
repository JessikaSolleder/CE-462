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


# Scenario 3 : 9 PL, Input Values
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
PL = 9
B = 6
A = 36
Q = 4000
v = 0.35
x = 5
z2 = 2
z4 = 4
z6 = 6
z8 = 8

# Retaining wall coordinates
xW = 0
yW = 0

# Scenario 3 coordinates (in feet)
PL9a = (6,2)
PL9ax = 6
PL9ay = 2

PL9b = (6, 0)
PL9bx = 6
PL9by = 0

PL9c = (6, 2)
PL9cx = 6
PL9cy = 2

PL9d = (8, 2)
PL9dx = 8
PL9dy = 2

PL9e = (8, 0)
PL9ex = 8
PL9ey = 0

PL9f = (8, 2)
PL9fx = 8
PL9fy = 2

PL9g = (10, 2)
PL9gx = 10
PL9gy = 2

PL9h = (10, 0)
PL9hx = 10
PL9hy = 0

PL9i = (10, 2)
PL9ix = 10
PL9iy = 2

# Plan view radial calculation, r^2 = x^2 + y^2 (in feet)
r9a = 6.324555
r9b = 6.000000
r9c = 6.324555
r9d = 8.246211
r9e = 8
r9f = 8.246211
r9g = 10.198039
r9h = 10
r9i = 10.198039

#############################################################
# R @ z2
#############################################################

R2a9 = math.sqrt(( PL9ax ** 2 ) + ( PL9ay ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft at PL a: ", R2a9)

R2b9 = math.sqrt(( PL9bx ** 2 ) + ( PL9by ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft at PL b: ", R2b9)

R2c9 = math.sqrt(( PL9cx ** 2 ) + ( PL9cy ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft at PL c: ", R2c9)

R2d9 = math.sqrt(( PL9dx ** 2 ) + ( PL9dy ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft at PL d: ", R2d9)

R2e9 = math.sqrt(( PL9ex ** 2 ) + ( PL9ey ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft at PL e: ", R2e9)

R2f9 = math.sqrt(( PL9fx ** 2 ) + ( PL9fy ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft at PL f: ", R2f9)

R2g9 = math.sqrt(( PL9gx ** 2 ) + ( PL9gy ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft at PL g: ", R2g9)

R2h9 = math.sqrt(( PL9hx ** 2 ) + ( PL9hy ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft at PL h: ", R2h9)

R2i9 = math.sqrt(( PL9ix ** 2 ) + ( PL9iy ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft at PL i: ", R2i9)

#############################################################
# R @ z4
#############################################################

R4a9 = math.sqrt(( PL9ax ** 2 ) + ( PL9ay ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft at PL a: ", R4a9)

R4b9 = math.sqrt(( PL9bx ** 2 ) + ( PL9by ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft at PL b: ", R4b9)

R4c9 = math.sqrt(( PL9cx ** 2 ) + ( PL9cy ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft at PL c: ", R4c9)

R4d9 = math.sqrt(( PL9dx ** 2 ) + ( PL9dy ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft at PL d: ", R4d9)

R4e9 = math.sqrt(( PL9ex ** 2 ) + ( PL9ey ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft at PL e: ", R4e9)

R4f9 = math.sqrt(( PL9fx ** 2 ) + ( PL9fy ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft at PL f: ", R4f9)

R4g9 = math.sqrt(( PL9gx ** 2 ) + ( PL9gy ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft at PL g: ", R4g9)

R4h9 = math.sqrt(( PL9hx ** 2 ) + ( PL9hy ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 4ft at PL h: ", R4h9)

R4i9 = math.sqrt(( PL9ix ** 2 ) + ( PL9iy ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft at PL i: ", R4i9)

#############################################################
#R @ z6
#############################################################

R6a9 = math.sqrt(( PL9ax ** 2 ) + ( PL9ay ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft at PL a: ", R6a9)

R6b9 = math.sqrt(( PL9bx ** 2 ) + ( PL9by ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft at PL b: ", R6b9)

R6c9 = math.sqrt(( PL9cx ** 2 ) + ( PL9cy ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft at PL c: ", R6c9)

R6d9 = math.sqrt(( PL9dx ** 2 ) + ( PL9dy ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft at PL d: ", R6d9)

R6e9 = math.sqrt(( PL9ex ** 2 ) + ( PL9ey ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft at PL e: ", R6e9)

R6f9 = math.sqrt(( PL9fx ** 2 ) + ( PL9fy ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft at PL f: ", R6f9)

R6g9 = math.sqrt(( PL9gx ** 2 ) + ( PL9gy ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft at PL g: ", R6g9)

R6h9 = math.sqrt(( PL9hx ** 2 ) + ( PL9hy ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft at PL h: ", R6h9)

R6i9 = math.sqrt(( PL9ix ** 2 ) + ( PL9iy ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 4ft at PL i: ", R6i9)

#############################################################
#R @ z8
#############################################################

R8a9 = math.sqrt(( PL9ax ** 2 ) + ( PL9ay ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft at PL a: ", R8a9)

R8b9 = math.sqrt(( PL9bx ** 2 ) + ( PL9by ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft at PL b: ", R8b9)

R8c9 = math.sqrt(( PL9cx ** 2 ) + ( PL9cy ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft at PL c: ", R8c9)

R8d9 = math.sqrt(( PL9dx ** 2 ) + ( PL9dy ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft at PL d: ", R8d9)

R8e9 = math.sqrt(( PL9ex ** 2 ) + ( PL9ey ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft at PL e: ", R8e9)

R8f9 = math.sqrt(( PL9fx ** 2 ) + ( PL9fy ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft at PL f: ", R8f9)

R8g9 = math.sqrt(( PL9gx ** 2 ) + ( PL9gy ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft at PL g: ", R8g9)

R8h9 = math.sqrt(( PL9hx ** 2 ) + ( PL9hy ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft at PL h: ", R8h9)

R8i9 = math.sqrt(( PL9ix ** 2 ) + ( PL9iy ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft at PL i: ", R8i9)


# Stress Calculations Scenario 3 - SOMETHING IS WRONG WITH THESE, VALUES ARE TOO LOW

sigma2a9 = (Q * 3 * z2 * r9a ** 2 * R2a9 * ( 1 - 2*v))/(3.1415926 * R2a9 ** 2 * R2a9 **3 * (R2a9 + z2))
sigma2b9 = (Q * 3 * z2 * r9b ** 2 * R2b9 * ( 1 - 2*v))/(3.1415926 * R2b9 ** 2 * R2b9 **3 * (R2b9 + z2))
sigma2c9 = (Q * 3 * z2 * r9c ** 2 * R2c9 * ( 1 - 2*v))/(3.1415926 * R2c9 ** 2 * R2c9 **3 * (R2c9 + z2))
sigma2d9 = (Q * 3 * z2 * r9d ** 2 * R2d9 * ( 1 - 2*v))/(3.1415926 * R2d9 ** 2 * R2d9 **3 * (R2d9 + z2))
sigma2e9 = (Q * 3 * z2 * r9e ** 2 * R2e9 * ( 1 - 2*v))/(3.1415926 * R2e9 ** 2 * R2e9 **3 * (R2e9 + z2))
sigma2f9 = (Q * 3 * z2 * r9f ** 2 * R2f9 * ( 1 - 2*v))/(3.1415926 * R2f9 ** 2 * R2f9 **3 * (R2f9 + z2))
sigma2g9 = (Q * 3 * z2 * r9g ** 2 * R2g9 * ( 1 - 2*v))/(3.1415926 * R2g9 ** 2 * R2g9 **3 * (R2g9 + z2))
sigma2h9 = (Q * 3 * z2 * r9h ** 2 * R2h9 * ( 1 - 2*v))/(3.1415926 * R2h9 ** 2 * R2h9 **3 * (R2h9 + z2))
sigma2i9 = (Q * 3 * z2 * r9i ** 2 * R2i9 * ( 1 - 2*v))/(3.1415926 * R2i9 ** 2 * R2i9 **3 * (R2i9 + z2))
sigma2abcdefghi9 = sigma2a9 + sigma2b9 + sigma2c9 + sigma2d9 + sigma2e9 + sigma2f9 + sigma2g9 + sigma2h9 + sigma2i9
print("The total stress at z = 2ft is: ", sigma2abcdefghi9, "psf")



