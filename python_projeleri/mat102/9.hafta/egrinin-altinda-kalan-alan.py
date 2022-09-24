import sympy as smp
x = smp.Symbol('x')
r = 1 - smp.cos(x)  # denklem
smp.integrate(0.5*r**2, (x, 0, 2*smp.pi))

# örnek
