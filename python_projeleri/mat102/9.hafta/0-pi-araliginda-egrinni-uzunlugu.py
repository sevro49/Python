import sympy as smp
x = smp.Symbol('x')
r = 1 + smp.cos(x)
smp.integrate(smp.sqrt(r**2 + smp.diff(r, x)**2), (x, 0, smp.pi)).n()

# eğer smp.pi yi 2 ile çarparsam 0 ile 2pi arasındaki eğrinin uzunluğunu bulmuş oluruz.
