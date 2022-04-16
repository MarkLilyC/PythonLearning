# `seaborn-boxplot`

最简单的一个实例

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


plt.figure(dpi=150)
L = [3,2,1,0,4]
sns.boxplot(L)
plt.show()
```

![Figure_1](A:\github\pythonlearn\seaborn\img\Figure_1.png)

一个简单实例

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


# 显示正负号与中文不显示问题
plt.rcParams['axes.unicode_minus'] = False
sns.set_style('darkgrid', {'font.sans-serif':['SimHei', 'Arial']})

# 去除部分warning
import warnings
warnings.filterwarnings('ignore')
# 参数
plt.figure(dpi=150)
# 导入数据
tips = sns.load_dataset('tips')
print(tips)
sns.boxplot(x='day',y='tip',data=tips)
plt.show()

```

![image-20220416224726337](C:\Users\26676\AppData\Roaming\Typora\typora-user-images\image-20220416224726337.png)

内部需要的数据形式：

```bash
     total_bill   tip     sex smoker   day    time  size
0         16.99  1.01  Female     No   Sun  Dinner     2
1         10.34  1.66    Male     No   Sun  Dinner     3
2         21.01  3.50    Male     No   Sun  Dinner     3
3         23.68  3.31    Male     No   Sun  Dinner     2
4         24.59  3.61  Female     No   Sun  Dinner     4
..          ...   ...     ...    ...   ...     ...   ...
239       29.03  5.92    Male     No   Sat  Dinner     3
240       27.18  2.00  Female    Yes   Sat  Dinner     2
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2
```

## 参数

**`x`** ：横坐标

* 在一般的折线图中`x`一般表示的连续性变量，如时间等

* 但在箱线图中，横坐标更多是数据的分类，如上图中的`sex` `smoker` `day`等

**`y`**：纵坐标

* 一般表示具体想比较的数值。如上表中的`tip`

通过调整`x y`的数据改变图的方向

```python
sns.boxplot(x='sex',y='tip',hue='smoker',data=tips, order=['Female','Male'], palette='Set2',saturation=0.4)
```

![image-20220416230330369](C:\Users\26676\AppData\Roaming\Typora\typora-user-images\image-20220416230330369.png)

```python
sns.boxplot(y='sex',x='tip',hue='smoker',data=tips, order=['Female','Male'], palette='Set2',saturation=0.4)
```

![image-20220416230412747](C:\Users\26676\AppData\Roaming\Typora\typora-user-images\image-20220416230412747.png)

## `hue`-两个分类变量分组绘制

**`hue`**：分类变量

* 用于对某一分类标准下的进一步分类
* 如上表中，在基础分类`day`的基础上，可进一步利用`sex`或者`smoker`进一步分类

```python
sns.boxplot(x='day',y='tip',hue = 'sex', data=tips)
```

![image-20220416224801032](C:\Users\26676\AppData\Roaming\Typora\typora-user-images\image-20220416224801032.png)

```
sns.boxplot(x='day',y='tip',hue='smoker',data=tips)
```

![image-20220416225639622](C:\Users\26676\AppData\Roaming\Typora\typora-user-images\image-20220416225639622.png)

## `order`-显示顺序

`order`：控制箱体的显示顺序

* 传入一个列表控制当前的箱体显示顺序

* 列表内的元素必须是当前的分类对象`x`的元素

  如当前的`x`的分类依据是`day`，因此传入的`order`必须包含所有的`day`元素，以便让每个箱体都有顺序

  ```python
  sns.boxplot(x='day',y='tip',hue='smoker',data=tips, order=['Sun','Sat','Fri','Thur'])
  ```

  ![image-20220416230051811](C:\Users\26676\AppData\Roaming\Typora\typora-user-images\image-20220416230051811.png)

例子：

```python
sns.boxplot(x='sex',y='tip',hue='smoker',data=tips, order=['Female','Male'])
```

![image-20220416230134879](C:\Users\26676\AppData\Roaming\Typora\typora-user-images\image-20220416230134879.png)



## `palette`-修改颜色

```python
sns.boxplot(x='sex',y='tip',hue='smoker',data=tips, order=['Female','Male'], palette='Set2',saturation=0.4)
```

![image-20220416230228612](C:\Users\26676\AppData\Roaming\Typora\typora-user-images\image-20220416230228612.png)

## `fliersize`-异常点大小

```python
sns.boxplot(x='sex',y='tip',hue='smoker',data=tips, fliersize= 0.5)
```

![image-20220416230613017](C:\Users\26676\AppData\Roaming\Typora\typora-user-images\image-20220416230613017.png)