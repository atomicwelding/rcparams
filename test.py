import rcparams
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure()
plt.plot(x, y, label="sin(x)", color=rcparams.named_colors['pink'])
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
