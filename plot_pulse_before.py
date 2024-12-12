import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('results_before_2.csv', header=None).to_numpy()[0][34842:85605:]

y = 0.104 * data - 12.83
x = [(i + 34842) * 0.00028879 for i in range(len(y))]
args = np.polyfit(x, y, 1)
print(args)
plt.plot(x, y - np.polyval(args, x), label='Пульс - 86 уд./мин')

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
plt.title('Артериальное давление\nдо физической нагрузки')
plt.ylabel(r"Давление [мм рт. ст.]")
plt.xlabel(r"Время [с]")
plt.legend()

plt.show()
