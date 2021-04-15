# Engenharia de Controle 
Prática do curso de engenharia de controle em python
## Simulação de sistemas de controle usando a linguagem em Python
### Foi usado o modulo numpy para simular vetores e matrizes
import numpy as np
#### np.array([])
#### np.linspace(start, stop,step)
#### np.arange(start, stop, step, dtype=float) 
### Foi usado o modulo matplotlib.pyplot para simular os gráficos
import matplotlib.pyplot as plt
#### plt.plot(entrada, saída)
#### plt.plot()
## Usando o modulo control.matlab para simular sistemas de controles com comandos do matlab
import control.matlab as ctl
import control as con

#### Criando função de transferência com o comando: 
ctl.tf(num, den)
#### Criando uma função de transferência em série com o comando 
ctl.series(Gc, Gs)
#### Criando a funçaõ de transferência de malha fechada
Hs função de transferência de realimentação
ctl.feedback(Ls, Hs, sign=-1)
