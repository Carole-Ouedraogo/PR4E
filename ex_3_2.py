xh = input("Enter Hours:")
xr = input("Enter Rate:")
try:
fh = float(xh)
fr = float(xr)
except:
    print("Error, please enter numeric input")
quit()
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
