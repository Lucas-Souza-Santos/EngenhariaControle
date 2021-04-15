import control as con
import control.matlab as ctl
import numpy as np 
import matplotlib.pyplot as plt

controlador = ctl.tf([0.1, 5], [1, 0])
missilDinamica = ctl.tf([100, 100], [1, 2, 100])

print("Controlador = ", controlador)
print("Dinâmica do Missil = ", missilDinamica)

Ls = ctl.series(controlador, missilDinamica)
print("L(s) = ", Ls)

Hss = ctl.tf([1], [1])

Ts = ctl.feedback(Ls, Hss, sign=-1)
print("T(s) = ", Ts)


yout, T = ctl.step(Ts, 3, 0)
info = con.step_info(Ts, 3)
print(info)

plt.plot(T, yout, '-k')
plt.show()