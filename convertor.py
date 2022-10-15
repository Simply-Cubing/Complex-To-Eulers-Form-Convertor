import cmath
num = complex(input("Number -> "))
costheta = cmath.acos(num)
sintheta = cmath.acos(num)
polar = f"""

e^(j{costheta}+{sintheta})"""


print(f"""

Polar -> {polar}""")