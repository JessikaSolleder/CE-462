#############################################################
# Scenario 1 : 1 Point Load
#############################################################
# # Input Values: # #
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
Q1 = 360000
v = 0.35
x = 5
z2 = 2
z4 = 4
z6 = 6
z8 = 8

# # Retaining wall coordinates # #
xW = 0
yW = 0

# # Scenario 1 coordinates (in feet) # #
PL1 = (8,0)
PL1x = 8
PL1y = 0

# # Plan view radial calculation, r^2 = x^2 + y^2 (in feet) # #
r = 8

#############################################################
# R @ z2
#############################################################

R2 = math.sqrt(( PL1x ** 2 ) + ( PL1y ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft: ", R2)

#############################################################
# R @ z4
#############################################################

R4 = math.sqrt(( PL1x ** 2 ) + ( PL1y ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft: ", R4)

#############################################################
# R @ z6
#############################################################

R6 = math.sqrt(( PL1x ** 2 ) + ( PL1y ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft: ", R6)

#############################################################
# R @ z8
#############################################################

R8 = math.sqrt(( PL1x ** 2 ) + ( PL1y ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft: ", R8)

# # Stress Calculations Scenario 1 # #

sigma2 = (Q1 * 3 * z2 * r ** 2 * R2 * ( 1 - 2*v))/(3.1415926 * R2 ** 2 * R2 **3 * (R2 + z2))
print("The stress at z = 2ft is: ", sigma2, "psf")

sigma4 = (Q1 * 3 * z4 * r ** 2 * R4 * ( 1 - 2*v))/(3.1415926 * R4 ** 2 * R4 **3 * (R4 + z4))
print("The stress at z = 4ft is: ", sigma4, "psf")

sigma6 = (Q1 * 3 * z6 * r ** 2 * R6 * ( 1 - 2*v))/(3.1415926 * R6 ** 2 * R6 **3 * (R6 + z6))
print("The stress at z = 6ft is: ", sigma6, "psf")

sigma8 = (Q1 * 3 * z8 * r ** 2 * R8 * ( 1 - 2*v))/(3.1415926 * R8 ** 2 * R8 **3 * (R8 + z8))
print("The stress at z = 8ft is: ", sigma8, "psf")

import matplotlib.pyplot as plt

# Extract sigma and z values from the code
sigma = [sigma2, sigma4, sigma6, sigma8]
z = [z2, z4, z6, z8]

# Configure the plot
plt.figure(figsize=(8, 6))
plt.plot(sigma, z, marker='o', color='b', linestyle='-', label='Sigma vs. z')
plt.xlabel('Sigma (psf)')
plt.ylabel('Depth (ft)')
plt.title('Stress vs. Depth for Scenario 1')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

#############################################################
# Scenario 2 : 4 Point Loads
#############################################################
# # Input Values: # #
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
Q2 = 90000
v = 0.35
x = 5
z2 = 2
z4 = 4
z6 = 6
z8 = 8

# # Retaining wall coordinates # #
xW = 0
yW = 0

# # Scenario 2 coordinates (in feet) # #
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

# # Plan view radial calculation, r^2 = x^2 + y^2 (in feet) # #
r4a = 6.6708
r4b = 9.6177
r4c = 6.6708
r4d = 9.6177

#############################################################
# R @ z2
#############################################################

R2a = math.sqrt(( PL4ax ** 2 ) + ( PL4ay ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft at PL a: ", R2a)

R2b = math.sqrt(( PL4bx ** 2 ) + ( PL4by ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft at PL b: ", R2b)

R2c = math.sqrt(( PL4cx ** 2 ) + ( PL4cy ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft at PL c: ", R2c)

R2d = math.sqrt(( PL4dx ** 2 ) + ( PL4dy ** 2 ) + (z2 ** 2))
print("Radial Calculation for z = 2ft at PL d: ", R2d)

#############################################################
# R @ z4
#############################################################

R4a = math.sqrt(( PL4ax ** 2 ) + ( PL4ay ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft at PL a: ", R4a)

R4b = math.sqrt(( PL4bx ** 2 ) + ( PL4by ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft at PL b: ", R4b)

R4c = math.sqrt(( PL4cx ** 2 ) + ( PL4cy ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft at PL c: ", R4c)

R4d = math.sqrt(( PL4dx ** 2 ) + ( PL4dy ** 2 ) + (z4 ** 2))
print("Radial Calculation for z = 4ft at PL d: ", R4d)

#############################################################
# R @ z6
#############################################################

R6a = math.sqrt(( PL4ax ** 2 ) + ( PL4ay ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft at PL a: ", R6a)

R6b = math.sqrt(( PL4bx ** 2 ) + ( PL4by ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft at PL b: ", R6b)

R6c = math.sqrt(( PL4cx ** 2 ) + ( PL4cy ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft at PL c: ", R6c)

R6d = math.sqrt(( PL4dx ** 2 ) + ( PL4dy ** 2 ) + (z6 ** 2))
print("Radial Calculation for z = 6ft at PL d: ", R6d)

#############################################################
# R @ z8
#############################################################

R8a = math.sqrt(( PL4ax ** 2 ) + ( PL4ay ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft at PL a: ", R8a)

R8b = math.sqrt(( PL4bx ** 2 ) + ( PL4by ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft at PL b: ", R8b)

R8c = math.sqrt(( PL4cx ** 2 ) + ( PL4cy ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft at PL c: ", R8c)

R8d = math.sqrt(( PL4dx ** 2 ) + ( PL4dy ** 2 ) + (z8 ** 2))
print("Radial Calculation for z = 8ft at PL d: ", R8d)


# # Stress Calculations Scenario 2 # #

sigma2a = (Q2 * 3 * z2 * r4a ** 2 * R2a * ( 1 - 2*v))/(3.1415926 * R2a ** 2 * R2a **3 * (R2a + z2))
sigma2b = (Q2 * 3 * z2 * r4b ** 2 * R2b * ( 1 - 2*v))/(3.1415926 * R2b ** 2 * R2b **3 * (R2b + z2))
sigma2c = (Q2 * 3 * z2 * r4c ** 2 * R2c * ( 1 - 2*v))/(3.1415926 * R2c ** 2 * R2c **3 * (R2c + z2))
sigma2d = (Q2 * 3 * z2 * r4d ** 2 * R2d * ( 1 - 2*v))/(3.1415926 * R2d ** 2 * R2d **3 * (R2d + z2))
sigma2abcd = sigma2a + sigma2b + sigma2c + sigma2d
print("The total stress at z = 2ft is: ", sigma2abcd, "psf")


sigma4a = (Q2 * 3 * z4 * r4a ** 2 * R4a * ( 1 - 2*v))/(3.1415926 * R4a ** 2 * R4a **3 * (R4a + z4))
sigma4b = (Q2 * 3 * z4 * r4b ** 2 * R4b * ( 1 - 2*v))/(3.1415926 * R4b ** 2 * R4b **3 * (R4b + z4))
sigma4c = (Q2 * 3 * z4 * r4c ** 2 * R4c * ( 1 - 2*v))/(3.1415926 * R4c ** 2 * R4c **3 * (R4c + z4))
sigma4d = (Q2 * 3 * z4 * r4d ** 2 * R4d * ( 1 - 2*v))/(3.1415926 * R4d ** 2 * R4d **3 * (R4d + z4))
sigma4abcd = sigma4a + sigma4b + sigma4c + sigma4d
print("The total stress at z = 4ft is: ", sigma4abcd, "psf")

sigma6a = (Q2 * 3 * z6 * r4a ** 2 * R6a * ( 1 - 2*v))/(3.1415926 * R6a ** 2 * R6a **3 * (R6a + z6))
sigma6b = (Q2 * 3 * z6 * r4b ** 2 * R6b * ( 1 - 2*v))/(3.1415926 * R6b ** 2 * R6b **3 * (R6b + z6))
sigma6c = (Q2 * 3 * z6 * r4c ** 2 * R6c * ( 1 - 2*v))/(3.1415926 * R6c ** 2 * R6c **3 * (R6c + z6))
sigma6d = (Q2 * 3 * z6 * r4d ** 2 * R6d * ( 1 - 2*v))/(3.1415926 * R6d ** 2 * R6d **3 * (R6d + z6))
sigma6abcd = sigma6a + sigma6b + sigma6c + sigma6d
print("The total stress at z = 6ft is: ", sigma6abcd, "psf")

sigma8a = (Q2 * 3 * z8 * r4a ** 2 * R8a * ( 1 - 2*v))/(3.1415926 * R8a ** 2 * R8a **3 * (R8a + z8))
sigma8b = (Q2 * 3 * z8 * r4b ** 2 * R8b * ( 1 - 2*v))/(3.1415926 * R8b ** 2 * R8b **3 * (R8b + z8))
sigma8c = (Q2 * 3 * z8 * r4c ** 2 * R8c * ( 1 - 2*v))/(3.1415926 * R8c ** 2 * R8c **3 * (R8c + z8))
sigma8d = (Q2 * 3 * z8 * r4d ** 2 * R8d * ( 1 - 2*v))/(3.1415926 * R8d ** 2 * R8d **3 * (R8d + z8))
sigma8abcd = sigma8a + sigma8b + sigma8c + sigma8d
print("The total stress at z = 8ft is: ", sigma8abcd, "psf")


#############################################################
# Scenario 3 : 9 Point Loads
#############################################################
# # Input Values: # #
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
Q3 = 40000
v = 0.35
x = 5
z2 = 2
z4 = 4
z6 = 6
z8 = 8

# # Retaining wall coordinates # #
xW = 0
yW = 0

# # Scenario 3 coordinates (in feet) # #
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

# # Plan view radial calculation, r^2 = x^2 + y^2 (in feet) # #
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
# R @ z6
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
# R @ z8
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


# # Stress Calculations Scenario 3 # #

sigma2a9 = (Q3 * 3 * z2 * r9a ** 2 * R2a9 * ( 1 - 2*v))/(3.1415926 * R2a9 ** 2 * R2a9 **3 * (R2a9 + z2))
sigma2b9 = (Q3 * 3 * z2 * r9b ** 2 * R2b9 * ( 1 - 2*v))/(3.1415926 * R2b9 ** 2 * R2b9 **3 * (R2b9 + z2))
sigma2c9 = (Q3 * 3 * z2 * r9c ** 2 * R2c9 * ( 1 - 2*v))/(3.1415926 * R2c9 ** 2 * R2c9 **3 * (R2c9 + z2))
sigma2d9 = (Q3 * 3 * z2 * r9d ** 2 * R2d9 * ( 1 - 2*v))/(3.1415926 * R2d9 ** 2 * R2d9 **3 * (R2d9 + z2))
sigma2e9 = (Q3 * 3 * z2 * r9e ** 2 * R2e9 * ( 1 - 2*v))/(3.1415926 * R2e9 ** 2 * R2e9 **3 * (R2e9 + z2))
sigma2f9 = (Q3 * 3 * z2 * r9f ** 2 * R2f9 * ( 1 - 2*v))/(3.1415926 * R2f9 ** 2 * R2f9 **3 * (R2f9 + z2))
sigma2g9 = (Q3 * 3 * z2 * r9g ** 2 * R2g9 * ( 1 - 2*v))/(3.1415926 * R2g9 ** 2 * R2g9 **3 * (R2g9 + z2))
sigma2h9 = (Q3 * 3 * z2 * r9h ** 2 * R2h9 * ( 1 - 2*v))/(3.1415926 * R2h9 ** 2 * R2h9 **3 * (R2h9 + z2))
sigma2i9 = (Q3 * 3 * z2 * r9i ** 2 * R2i9 * ( 1 - 2*v))/(3.1415926 * R2i9 ** 2 * R2i9 **3 * (R2i9 + z2))
sigma2abcdefghi9 = sigma2a9 + sigma2b9 + sigma2c9 + sigma2d9 + sigma2e9 + sigma2f9 + sigma2g9 + sigma2h9 + sigma2i9
print("The total stress at z = 2ft is: ", sigma2abcdefghi9, "psf")

sigma4a9 = (Q3 * 3 * z4 * r9a ** 2 * R4a9 * ( 1 - 2*v))/(3.1415926 * R4a9 ** 2 * R4a9 **3 * (R4a9 + z4))
sigma4b9 = (Q3 * 3 * z4 * r9b ** 2 * R4b9 * ( 1 - 2*v))/(3.1415926 * R4b9 ** 2 * R4b9 **3 * (R4b9 + z4))
sigma4c9 = (Q3 * 3 * z4 * r9c ** 2 * R4c9 * ( 1 - 2*v))/(3.1415926 * R4c9 ** 2 * R4c9 **3 * (R4c9 + z4))
sigma4d9 = (Q3 * 3 * z4 * r9d ** 2 * R4d9 * ( 1 - 2*v))/(3.1415926 * R4d9 ** 2 * R4d9 **3 * (R4d9 + z4))
sigma4e9 = (Q3 * 3 * z4 * r9e ** 2 * R4e9 * ( 1 - 2*v))/(3.1415926 * R4e9 ** 2 * R4e9 **3 * (R4e9 + z4))
sigma4f9 = (Q3 * 3 * z4 * r9f ** 2 * R4f9 * ( 1 - 2*v))/(3.1415926 * R4f9 ** 2 * R4f9 **3 * (R4f9 + z4))
sigma4g9 = (Q3 * 3 * z4 * r9g ** 2 * R4g9 * ( 1 - 2*v))/(3.1415926 * R4g9 ** 2 * R4g9 **3 * (R4g9 + z4))
sigma4h9 = (Q3 * 3 * z4 * r9h ** 2 * R4h9 * ( 1 - 2*v))/(3.1415926 * R4h9 ** 2 * R4h9 **3 * (R4h9 + z4))
sigma4i9 = (Q3 * 3 * z4 * r9i ** 2 * R4i9 * ( 1 - 2*v))/(3.1415926 * R4i9 ** 2 * R4i9 **3 * (R4i9 + z4))
sigma4abcdefghi9 = sigma4a9 + sigma4b9 + sigma4c9 + sigma4d9 + sigma4e9 + sigma4f9 + sigma4g9 + sigma4h9 + sigma4i9
print("The total stress at z = 4ft is: ", sigma4abcdefghi9, "psf")

sigma6a9 = (Q3 * 3 * z6 * r9a ** 2 * R6a9 * ( 1 - 2*v))/(3.1415926 * R6a9 ** 2 * R6a9 **3 * (R6a9 + z6))
sigma6b9 = (Q3 * 3 * z6 * r9b ** 2 * R6b9 * ( 1 - 2*v))/(3.1415926 * R6b9 ** 2 * R6b9 **3 * (R6b9 + z6))
sigma6c9 = (Q3 * 3 * z6 * r9c ** 2 * R6c9 * ( 1 - 2*v))/(3.1415926 * R6c9 ** 2 * R6c9 **3 * (R6c9 + z6))
sigma6d9 = (Q3 * 3 * z6 * r9d ** 2 * R6d9 * ( 1 - 2*v))/(3.1415926 * R6d9 ** 2 * R6d9 **3 * (R6d9 + z6))
sigma6e9 = (Q3 * 3 * z6 * r9e ** 2 * R6e9 * ( 1 - 2*v))/(3.1415926 * R6e9 ** 2 * R6e9 **3 * (R6e9 + z6))
sigma6f9 = (Q3 * 3 * z6 * r9f ** 2 * R6f9 * ( 1 - 2*v))/(3.1415926 * R6f9 ** 2 * R6f9 **3 * (R6f9 + z6))
sigma6g9 = (Q3 * 3 * z6 * r9g ** 2 * R6g9 * ( 1 - 2*v))/(3.1415926 * R6g9 ** 2 * R6g9 **3 * (R6g9 + z6))
sigma6h9 = (Q3 * 3 * z6 * r9h ** 2 * R6h9 * ( 1 - 2*v))/(3.1415926 * R6h9 ** 2 * R6h9 **3 * (R6h9 + z6))
sigma6i9 = (Q3 * 3 * z6 * r9i ** 2 * R6i9 * ( 1 - 2*v))/(3.1415926 * R6i9 ** 2 * R6i9 **3 * (R6i9 + z6))
sigma6abcdefghi9 = sigma6a9 + sigma6b9 + sigma6c9 + sigma6d9 + sigma6e9 + sigma6f9 + sigma6g9 + sigma6h9 + sigma6i9
print("The total stress at z = 6ft is: ", sigma6abcdefghi9, "psf")

sigma8a9 = (Q3 * 3 * z8 * r9a ** 2 * R8a9 * ( 1 - 2*v))/(3.1415926 * R8a9 ** 2 * R8a9 **3 * (R8a9 + z8))
sigma8b9 = (Q3 * 3 * z8 * r9b ** 2 * R8b9 * ( 1 - 2*v))/(3.1415926 * R8b9 ** 2 * R8b9 **3 * (R8b9 + z8))
sigma8c9 = (Q3 * 3 * z8 * r9c ** 2 * R8c9 * ( 1 - 2*v))/(3.1415926 * R8c9 ** 2 * R8c9 **3 * (R8c9 + z8))
sigma8d9 = (Q3 * 3 * z8 * r9d ** 2 * R8d9 * ( 1 - 2*v))/(3.1415926 * R8d9 ** 2 * R8d9 **3 * (R8d9 + z8))
sigma8e9 = (Q3 * 3 * z8 * r9e ** 2 * R8e9 * ( 1 - 2*v))/(3.1415926 * R8e9 ** 2 * R8e9 **3 * (R8e9 + z8))
sigma8f9 = (Q3 * 3 * z8 * r9f ** 2 * R8f9 * ( 1 - 2*v))/(3.1415926 * R8f9 ** 2 * R8f9 **3 * (R8f9 + z8))
sigma8g9 = (Q3 * 3 * z8 * r9g ** 2 * R8g9 * ( 1 - 2*v))/(3.1415926 * R8g9 ** 2 * R8g9 **3 * (R8g9 + z8))
sigma8h9 = (Q3 * 3 * z8 * r9h ** 2 * R8h9 * ( 1 - 2*v))/(3.1415926 * R8h9 ** 2 * R8h9 **3 * (R8h9 + z8))
sigma8i9 = (Q3 * 3 * z8 * r9i ** 2 * R8i9 * ( 1 - 2*v))/(3.1415926 * R8i9 ** 2 * R8i9 **3 * (R8i9 + z8))
sigma8abcdefghi9 = sigma8a9 + sigma8b9 + sigma8c9 + sigma8d9 + sigma8e9 + sigma8f9 + sigma8g9 + sigma8h9 + sigma8i9
print("The total stress at z = 8ft is: ", sigma8abcdefghi9, "psf")


import matplotlib.pyplot as plt

# Extract sigma and z values from the code
sigma = [sigma2a9, sigma4a9, sigma6a9, sigma8a9,  
         sigma2b9, sigma4b9, sigma6b9, sigma8b9,  
         sigma2c9, sigma4c9, sigma6c9, sigma8c9,
         sigma2d9, sigma4d9, sigma6d9, sigma8d9,
         sigma2e9, sigma4e9, sigma6e9, sigma8e9,
         sigma2f9, sigma4f9, sigma6f9, sigma8f9,
         sigma2g9, sigma4g9, sigma6g9, sigma8g9,
         sigma2h9, sigma4g9, sigma6g9, sigma8g9,
         sigma2i9, sigma4i9, sigma6i9, sigma8i9,
         
         ]
z = [z2, z4, z6, z8] * 9  # Repeat z values for each point load

# Configure the plot
plt.figure(figsize=(10, 6))  # Adjust figure size if needed
plt.plot(sigma, z, marker='o', color='b', linestyle='-', label='Sigma vs. z')
plt.xlabel('Sigma (psf)')
plt.ylabel('Depth (ft)')
plt.title('Sigma vs. z for Scenario 3')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

