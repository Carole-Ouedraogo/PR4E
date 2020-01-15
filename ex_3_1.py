
'''3.1 Write a program to prompt the user for hours and rate per hour
using input to compute gross pay.
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate
for all hours worked above 40 hours. Use 45 hours and a rate of
10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to a number.
Do not worry about error checking the user input -
Assume the user types numbers properly.'''

xh = input("Enter Hours:")
xr = input("Enter Rate:")
fh = float(xh)
fr = float(xr)
# print(fh, fr)
if fh > 40 :
    # print("Overtime")
    reg = fr*fh
    otp = (fh-40) *(fr*1.5)
    # print(reg, otp)
    xp = reg + otp
else :
    # print("Regular")
    xp = fr*fh
print ("Pay:", xp)
