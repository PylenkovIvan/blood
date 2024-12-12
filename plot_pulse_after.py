import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('results_after_2.csv', header=None).to_numpy()[0][23478:101974:]

y = 0.104 * data - 12.83
x = [(i + 23478) * 0.00028879 for i in range(len(y))]
args = np.polyfit(x, y, 1)

plt.plot(x, y - np.polyval(args, x), label='Пульс - 95')

plt.ticklabel_format(style='sci',
                     axis='both',
                     scilimits=(0, 0),
                     useMathText=True)

plt.minorticks_on()

plt.grid(visible=True,
         which='major',
         linestyle='-',
         linewidth=1.5,
         color='0.7')
plt.grid(visible=True,
         which='minor',
         linestyle='-',
         linewidth=1,
         color='0.8')

plt.xlim([np.min(x), np.max(x)])
plt.ylim([np.min(y - np.polyval(args, x)), np.max(y - np.polyval(args, x))])
print(abs(np.min(x) - np.max(x)))
plt.title('Артериальное давление\nпосле физической нагрузки')
plt.ylabel(r"Давление [мм рт. ст.]")
plt.xlabel(r"Время [с]")
plt.legend()

plt.show()
