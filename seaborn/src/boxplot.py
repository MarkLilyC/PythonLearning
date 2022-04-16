import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# 显示正负号与中文不显示问题
plt.rcParams['axes.unicode_minus'] = False
sns.set_style('darkgrid', {'font.sans-serif':['SimHei', 'Arial']})
sns.set_theme(style="whitegrid",font='Times New Roman',font_scale=1)

# 去除部分warning
import warnings
warnings.filterwarnings('ignore')
plt.figure(dpi=150)


tips = sns.load_dataset('tips')
sns.boxenplot(x='sex',y='tip',hue='smoker',data=tips, width= 0.5, linewidth= 0.5)
plt.show()