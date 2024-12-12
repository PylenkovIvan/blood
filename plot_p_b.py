import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('results_before_2.csv', header=None).to_numpy()[0][23000:160000:]

y = 0.104 * data - 12.83
x = [(i + 23000) * 0.00028879 for i in range(len(y))]
print(np.where(np.isclose(y, 110., atol=0.1))[0][0],
      np.where(np.isclose(y, 77., atol=0.1))[0][0])

plt.plot(x, y, label='Давление - 110/77 [мм рт. ст.]')
plt.plot(x[np.where(np.isclose(y, 110., atol=0.1))[0][0]], 110, 'o', label='Systole')
plt.plot(x[np.where(np.isclose(y, 77., atol=0.1))[0][0]], 77, 'o', label='Diastole')

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

plt.xlim([np.min(x) * 0.95, np.max(x) * 1.02])
plt.ylim([np.min(y) * 0.95, np.max(y) * 1.02])

plt.title('Артериальное давление\nдо физической нагрузки')
plt.ylabel(r"Давление [мм рт. ст.]")
plt.xlabel(r"Время [с]")
plt.legend()

plt.show()
