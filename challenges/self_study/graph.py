import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import pandas as pd

msft = pd.read_csv('2021-05-21 stock_data.csv')

fig = plt.figure()
gs = fig.add_gridspec(6, 6)  # grid size
ax1 = fig.add_subplot(gs[0:6, 0:6])  # add plot
