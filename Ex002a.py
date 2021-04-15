import control as ctl
import control.matlab as mat
import numpy as np 
import matplotlib.pyplot as plt 

Gca = ctl.tf([2], [1])
Gp = ctl.tf([-10], [1, 10]) # Servo do Profundor 
Gma = ctl.tf([-1, -5], [1, 3.5, 6, 0])  # sistema da aero nave
print("------------------------------------------")
print("G(s) = ", Gca)                               
print("servo profunor = ", Gp)               
print("Modelo Aeronave = ", Gma)       
print("------------------------------------------")

t = np.arange(0, 15, 1)
y = 0.5 * t

# print(t)
# print("y(t) = ", y)
Ls = mat.series(Gca, Gp, Gma)
print("L(s) = ", Ls)

Hss = ctl.tf([1], [1]) 
print("H(s) = ", Hss) 
Ts = ctl.feedback(Ls, Hss)
print("T(s) = ", Ts)

yout, T, Xo = mat.lsim(Ts, y, t, 0)
# print(T)

plt.plot(T, yout, '-b')
plt.plot(t, y, '-r')
plt.grid()
plt.show()

