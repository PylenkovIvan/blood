import numpy as np
import pandas as pd

data_40 = pd.read_csv('results_40.csv', header=None).to_numpy()[0]
data_60 = pd.read_csv('results_60.csv', header=None).to_numpy()[0]
data_80 = pd.read_csv('results_80.csv', header=None).to_numpy()[0]
data_100 = pd.read_csv('results_100.csv', header=None).to_numpy()[0]
data_120 = pd.read_csv('results_120.csv', header=None).to_numpy()[0]
av_40 = round(np.mean(data_40))
av_60 = round(np.mean(data_60))
av_80 = round(np.mean(data_80))
av_100 = round(np.mean(data_100))
av_120 = round(np.mean(data_120))

print(av_40, av_60, av_80, av_100, av_120)