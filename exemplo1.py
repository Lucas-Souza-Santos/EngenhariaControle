import control as ctl
import matplotlib.pyplot as plt
import numpy as np

# Contruindo a função de transferência do sistema
R = 1
C = 1
Tsim = 10
numerador = [1.]
denominador = [R * C, 1.]
H = ctl.tf(numerador, denominador)
print('FT malha aberta = ', H)

# calcular a resposta ao degrau 
T, yout = ctl.step_response(H, Tsim)
plt.plot(T, yout, 'b-')
# print(plt.show())

# calcular um degrau unitário 
T2 = np.linspace(-1, 10, 1000)
degrau = np.ones_like(T2)
degrau[T2 < 0]  = 0
plt.plot(T2, degrau, 'r-')
plt.grid()
print(plt.show())
