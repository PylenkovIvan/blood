import matplotlib.pyplot as plt
import numpy as np

x = [508, 699, 894, 1074, 1280]
y = [40, 60, 80, 100, 120]
args = np.polyfit(x, y, 1)

plt.plot(x, y, 'o', markersize=4, label='Измерения')
plt.plot(range(508, 1281), np.polyval(args, range(508, 1281)),
         label='P = 0.104*N - 12.83 [мм рт. ст.]')
print(np.polyfit(x, y, 1))

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

plt.title('Калибровочный график зависимости\nдавления от показаний АЦП')
plt.ylabel(r"Давление [мм рт. ст.]")
plt.xlabel(r"Отсчёты АЦП")
plt.legend()

plt.show()
