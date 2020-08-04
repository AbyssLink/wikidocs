# Python 金融数据分析

课程链接 🔗：[Python and Statistics for Financial Analysis](https://www.coursera.org/learn/python-statistics-financial-analysis/home/welcome)

### Python 在金融数据中的使用方式

| 组织     | 模型                           | 实例                                                                         | 对象       |
| -------- | ------------------------------ | ---------------------------------------------------------------------------- | ---------- |
| 投资银行 | 预测收益模型<br />评估风险模型 | 搜寻财经新闻，挖掘出用户的意见和观点；<br />获取社交媒体数据，改善模型的性能 | 定量分析师 |
| 消费银行 | 客户行为模型<br />推荐模型     | 客户行为模型用于降低贷款风险；<br />推荐模型用于预测用户行为                 | 数据科学家 |

### 一个基于信号量的简单的交易策略

移动平均（Moving Average, **MA**）是一种分析时间序列的工具，可抚平短期波动，反应长期趋势或周期。

简单移动平均（simple moving average, **SMA**）是 n 个数值的算术平均值：

$$
SMA = \frac{p_1 + p_2 + ··· + p_n}{n}
$$

DataFrame 有内建方法来计算任意天数的简单移动平均:

```python
fb = pd.DataFrame.from_csv('../data/facebook.csv')
# import FaceBook's stock data, add two columns - MA10 and MA50
fb['MA10'] = fb['Close'].rolling(10).mean()
fb['MA50'] = fb['Close'].rolling(50).mean()
```

![moving-average](https://raw.githubusercontent.com/AbyssLink/pic/master/figure-moving-average.jpg)

**信号量**：

短期的移动平均称为**快速信号**（Fast Signal），反映近期股价变化。

长期的移动平均称为**缓慢信号**（Slow Signal），反映长期股价变化。

**简单策略**：

如果 MA10 大于 MA50，就认为股价会在接下来的几天内上涨，我们购买并持有一股股票，即多头一股股票（one share of stock）

```python
# 增加一个新列 "Shares", 若 MA > MA50，意味着 1 (多头该股票)，否则意味着 0（什么也不做）
fb['Shares'] = [1 if fb.loc[ei, 'MA10']>fb.loc[ei, 'MA50'] else 0 for ei in fb.index]

# 增加一个新列 "Profit"，fb 表中的行若 Shares = 1, 则 profit 是该股明天的收盘价 - 今天的收盘价。否则 profit 为 0
fb['Close1'] = fb['Close'].shift(-1)
fb['Profit'] = [fb.loc[ei, 'Close1'] - fb.loc[ei, 'Close'] if fb.loc[ei, 'Shares']==1 else 0 for ei in fb.index]

# 使用 .cumsum() 计算该期间累计的财富
fb['wealth'] = fb['Profit'].cumsum()
fb.tail()

# 绘制 wealth 图形以显示该时期内 profit 的增长
fb['wealth'].plot()
plt.title('Total money you win is {}'.format(fb.loc[fb.index[-2], 'wealth']))
```

![profit-grow](https://raw.githubusercontent.com/AbyssLink/pic/master/figure-profit-grow.jpg)

### 随机变量及 Python 模拟

DataFrame 模拟骰子游戏：

```Python
# 模拟滚动骰子 50 次
dice = pd.DataFrame([1, 2, 3, 4, 5, 6])
trial = 50
results = [dice.sample(2, replace=True).sum().loc[0] for i in range(trial)]

# 按频率汇总点数总和的结果
freq = pd.DataFrame(results)[0].value_counts()
sort_freq = freq.sort_index()
# 使用相对频率，以缩放频率便于比较来自不同试验次数的结果
relative_freq = sort_freq/trial
print(relative_freq)

# output
2     0.06
3     0.10
···
11    0.08
12    0.06
Name: 0, dtype: float64
```

- 离散随机变量
- 连续随机变量

### 均值（mean）与方差 （variance）

假设我们有一个公平的骰子（所有面出现的概率均相等），那么我们可以得到随机变量的分布：

```python
X_distri = pd.DataFrame(index=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
X_distri['Prob'] = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
X_distri['Prob'] = X_distri['Prob']/36
X_distri
```

输出分布的均值和方差。 均值和方差可用于描述分布。

```python
mean = pd.Series(X_distri.index * X_distri['Prob']).sum()
var = pd.Series(((X_distri.index - mean)**2)*X_distri['Prob']).sum()
print(mean, var)

# output
7.0 5.83333333333
```

经验均值与方差

```python
# 计算结果的均值和方差（具有足够多的试验次数，如20000次）
trial = 20000
results = [die.sample(2, replace=True).sum().loc[0] for i in range(trial)]
results = pd.Series(results)
print(results.mean(), results.var())

# output
6.97645 5.82188649182
```

### 股票收益模型

计算对数收益分布

```python
# 计算 Microsoft 的每日收益的对数值
ms['LogReturn'] = np.log(ms['Close']).shift(-1) - np.log(ms['Close'])

from scipy.stats import norm
mu = ms['LogReturn'].mean()
sigma = ms['LogReturn'].std(ddof=1)

density = pd.DataFrame()
density['x'] = np.arange(ms['LogReturn'].min()-0.01, ms['LogReturn'].max()+0.01, 0.001)
density['pdf'] = norm.pdf(density['x'], mu, sigma)

# 绘制直方图以显示 Microsoft 股票的对数收益分布。你可以看到它非常接近正态分布
ms['LogReturn'].hist(bins=50, figsize=(15, 8))
plt.plot(density['x'], density['pdf'], color='red')
plt.show()
```

![](https://raw.githubusercontent.com/AbyssLink/pic/master/microsoft-log-return-distribution.png)

计算股票价格在某段时间内下跌超过一定百分比的可能性

```python
# Microsoft 的股价一天之内下跌超过 5％ 的可能性
prob_return1 = norm.cdf(-0.05, mu, sigma)
print('The Probability is ', prob_return1)

# 在 220 天内股价下降 40％ 以上
mu220 = 220*mu
sigma220 = (220**0.5) * sigma
drop40 = norm.cdf(-0.4, mu220, sigma220)
print('The probability is ', drop40)
```

### 计算风险价值

**风险价值**（Value at Risk，**VaR**），指资产在给定的**置信区间**内由于市场价格变动导致的最大预期损失的数值。

```python
# 风险价值 (VaR)
VaR = norm.ppf(0.05, mu, sigma)
print('Single day value at risk ', VaR)
```

### 抽样（Sampling）

抽样（Sampling）是一种推论统计方法，它从目标总体（Population）中抽取一部分个体作为样本（Sample），通过观察样本的属性，依据所获得的数据对总体的数量特征得出具有一定可靠性的估计判断，从而达到对总体的认识。
