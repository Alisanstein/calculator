import math

num1 = float(input("Please Enter A Number: "))
num2 = float(input("Please Enter A Number Again: "))

sum = num1 + num2
mines = num1 - num2
multiply = num1 * num2
idk = num1 / num2
idk2 = num1 ** num2
power = pow(num1, num2)
log = math.log(num1 , num2)
Radical_num1 = math.sqrt(num1)
Radical_num2 = math.sqrt(num2)

print("(+) = " + str(sum))
print("(-) = " + str(mines))
print("(*) = " + str(multiply))
print("(/) = " + str(idk))
print("(power) = " + str(idk2))
print("(log) = " + str(log))
print("(Radical num1) = " + str(Radical_num1))
print("(Radical num2) = " + str(Radical_num2))