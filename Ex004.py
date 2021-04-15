import control as con 
import control.matlab as ctl
import numpy as np

k = np.arange(1, 5.1, 0.1, dtype=float)

Gc = ctl.tf([1, -2, 4], [1, 4, 2])
Hss = ctl.tf([1], [1])


for x in k:
    Ts = ctl.feedback(ctl.series(x, Gc), Hss, sign=-1)
    if ctl.pole(Ts)[0].real < 0:
        print("------- Sistema estável ------")
        print(f"Polos  K = {round(x, 2)}", ctl.pole(Ts), " Sistema estável")

