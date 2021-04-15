import control as ctl
import matplotlib.pyplot as plt 
import numpy as np 

# Função de transferência do sistema 
numG = np.array([25])
denG = np.array([1, 5, 0])
Ls = ctl.tf(numG, denG)
print("L(s) = ", Ls)

# malha de realimentação
numH = np.array([1])
denH = np.array([1])
Hs = ctl.tf(numH, denH)
print("H(s) = ", Hs)

# Função de transferência de malha fechada
Ts = ctl.feedback(ctl.series(Ls, 1), Hs, sign=-1)
print("Função de transferência do sistema em malha fechada", Ts)
print("Zeros: ", ctl.zero(Ts))
print("Polos: ", ctl.pole(Ts))

# Calculo da Resposta ao degrau
Tsim = 3 
T, yout = ctl.step_response(Ts, Tsim)
infomation = ctl.step_info(Ts)
print("Informações: ", infomation)

# Calcular o degrau unitário
T2 = np.linspace(-1, Tsim, 1000)
degrau = np.ones_like(T2)
degrau[T2 < 0] = 0

#plotar os resultados
plt.plot(T, yout, 'k-')
plt.plot(T2, degrau, 'r-')
plt.grid()
print(plt.show())
