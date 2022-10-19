import matplotlib.pyplot as plt
from scipy import pi, sin, cos, arcsin, linspace, sqrt, exp
from matplotlib.pyplot import (plot, show, xlabel, ylabel, title, legend,
                               grid, axis, tight_layout)

n1 = 1.0
n2 = 1.5
n3 = 1.0

ep1 = n1 ** 2
ep2 = n2 ** 2
ep3 = n3 ** 2

d2 = 100
WL = 500
k0 = 2 * pi / WL

t1Deg = linspace(0, 90, 91)
t1 = t1Deg / 180 * pi
t2 = arcsin((n1 / n2) * sin(t1))

s1 = sin(t1)  # sin(t1)
c1 = cos(t1)  # cos(t1)
s2 = n1 / n2 * s1  # sin(t2)
c2 = sqrt(1 - s2**2)  # cos(t2)
s3 = n1 / n3 * s1  # sin(t2)
c3 = sqrt(1 - s3**2)  # cos(t2)

n1z = n1 * c1
n2z = n2 * c2
n3z = n3 * c3

rs12 = (n1z - n2z) / (n1z + n2z)
rs23 = (n2z - n3z) / (n2z + n3z)

rs = (rs12 + rs23 * exp(2 * 1j * d2 * k0 * n2z)) / (
    1 + rs12 * rs23 * exp(2 * 1j * d2 * k0 * n2z))

RsAbs = abs(rs ** 2)


plt.figure(figsize=(8, 6))
# plot(t1Deg, RpAbs, label=r"$R_{12}^{\rm{p}}$", linewidth=3.0,
#      linestyle='dashed')
plot(t1Deg, RsAbs, label=r"$R_{13}^{\rm{s}}$", linewidth=3.0,
     linestyle='solid')

xlabel(r"$\theta_1$(deg.)", fontsize=20)
ylabel("Reflectivity", fontsize=20)
title("Reflectivity", fontsize=18)
legend(fontsize=20, loc='lower right')
grid(True)

axis([0.0, 90, 0, 1.1])

tight_layout()
show()
