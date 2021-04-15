import control.matlab as ctl
import numpy as np 
import matplotlib.pyplot as plt 

Gca = ctl.tf([2, 1], [1, 0])
Gp = ctl.tf([-10], [1, 10]) # Servo do Profundor 
Gma = ctl.tf([-1, -5], [1, 3.5, 6, 0])  # sistema da aero nave


t = np.arange(0, 17, 1)
y = 0.5 * t


Ls = ctl.series(Gca, Gp, Gma)
print("L(s) = ", Ls)

Hss = ctl.tf([1], [1])
print("H(s) = ", Hss)

Ts = ctl.feedback(Ls, Hss, sign=-1)
print("T(s) = ", Ts)

yout, T, Xo = ctl.lsim(Ts, y, t, 0)

plt.plot(T, yout, '-k')
plt.plot(t, y, '-r')
plt.grid()
plt.show()
