import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma

n = np.linspace(1, 21, 100)

# Compute the complexities
O_1 = np.ones_like(n)
O_log_n = np.log(n)
O_n = n
O_n_log_n = n * np.log(n)
O_n_squared = n**2
O_exp_n = np.exp(n)

# make all the curves start at 1
O_1 += 1 - O_1[0]
O_log_n += 1 - O_log_n[0]
O_n += 1 - O_n[0]
O_n_log_n += 1 - O_n_log_n[0]
O_n_squared += 1 - O_n_squared[0]
O_exp_n += 1 - O_exp_n[0]


# Plotting
plt.figure(figsize=(10, 6))

plt.plot(n, O_1, lw=3)
plt.plot(n, O_log_n, lw=3)
plt.plot(n, O_n, lw=3)
plt.plot(n, O_n_log_n, lw=3)
plt.plot(n, O_n_squared, lw=3)
plt.plot(n, O_exp_n, lw=3)

# add text to the curves to label them
plt.text(21, -4.5, "$O(1)$", fontsize=16, ha="right")
plt.text(21, 6.5, "$O(\log n)$", fontsize=16, ha="right")
plt.text(21, 24, "$O(n)$", fontsize=16, ha="right")
plt.text(21, 67.5, "$O(n\log n)$", fontsize=16, ha="right")
plt.text(9, 90, "$O(n^2)$", fontsize=16, ha="right")
plt.text(4, 90, "$O(e^n)$", fontsize=16, ha="right")


font_size = 16
plt.xlabel("Problem size $n$", fontdict={"fontsize": font_size})
plt.ylabel("Time/Space Complexity", fontdict={"fontsize": font_size})
plt.title("Computational Complexity Classes", fontdict={"fontsize": font_size})
plt.grid(True, which="both", ls="--")
plt.ylim(0, 100)
plt.xticks([])
plt.yticks([])
plt.tight_layout()

plt.savefig("./problem_classes.png")
