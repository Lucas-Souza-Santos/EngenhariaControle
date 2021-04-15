# Importantando  as bibliotecas 
from os import system
import control as ctl
import matplotlib.pyplot as plt 
import numpy as np 

def CriarLinha():
    print(70 * "=")

# Criando a função de transferência em malha aberta 
system("Clear")
km = 1.6 
M = 1
fv = 0.2
Wn = np.sqrt(km/M)
eta = (fv/M)/(2 * Wn)

CriarLinha()
print("Wn e eta = ", [Wn, eta])
CriarLinha()

Tsim = 10
numerador = [1.]
denominador = [M, fv, km]
P_s = ctl.tf(numerador, denominador)
print("Função de tranferência = ", P_s)
CriarLinha()

# Controlador PID
Ki = 2 * Wn
Kp = 10 * Wn
Kd = 1 * Wn
C_s = ctl.tf([Kd, Kp, Ki], [1., 0.])
print("PID = ", C_s)
CriarLinha()

# Sensor unitário 
H_s = ctl.tf([1.], [1.])
print("Sensor = ", H_s)

# função de transferência de malha fechada 
G1_s = ctl.feedback(ctl.series(C_s, P_s), H_s, sign=-1)
print("Funçaõ de transferência de Malha Feixada = ", G1_s)

# Calculo da Resposta ao degrau 
T, yout = ctl.step_response(P_s, Tsim)
T_mf, yout_mf = ctl.step_response(G1_s, Tsim)

# Calcular o degrau unitário
T2 = np.linspace(-1, Tsim, 10000)
degrau = np.ones_like(T2)
degrau[T2 < 0] = 0

#plotar os resultados
# plt.plot(T, yout, 'b-')
plt.plot(T_mf, yout_mf, 'k-')
plt.plot(T2, degrau, 'r-')
plt.grid()
print(plt.show())