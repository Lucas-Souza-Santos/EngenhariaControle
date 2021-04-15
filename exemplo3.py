import control.matlab as ctl
import matplotlib.pyplot as plt 
import numpy as np 

num = np.array([1, 1])
den = np.array([3, 9, 0, 0])

GH = ctl.tf(num, den)
print(GH)
print("Zeros: ", ctl.zero(GH))
print("Plos: ", ctl.pole(GH))


rlist, klist = ctl.rlocus(GH, PrintGain=True, grid=True)
plt.grid()
print(plt.show())

