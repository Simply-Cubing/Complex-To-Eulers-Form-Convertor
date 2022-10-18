import cmath
print("(Enter Numbers In The Form a+bj")
num = complex(input("Number -> "))
costheta = cmath.acos(num.real)
sintheta = cmath.acos(num.imag)
rcostheta = round(costheta.real,3)
rsintheta = round(sintheta.imag, 3)
if rsintheta == 0:
  polar = f"""
  
e^({rcostheta}i)"""
elif rcostheta == 0:
  polar = f"""
  
e^({rsintheta}i)"""
else:
  polar = f"""

e^(i({rcostheta}+{rsintheta})"""


print(f"""

Polar Form of {num} = {polar}""")
