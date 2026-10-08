import numpy as np
import pandas as pd


a = np.array([3, 1, 4, 1, 5])
print(a * 2, a + 10, a ** 2)
print(a.mean(), a.min(), a.max(), a.sum())
M = np.arange(12).reshape(3, 4)
print(M, M.shape)
print('строка 0:', M[0]); print('столбец 1:', M[:, 1]); print('элемент:', M[2, 3])
print(M.T.shape)
print(M.mean(axis=0))  # 4 числа
print(M.mean(axis=1))  # 3 числа
A = np.array([[1, 2, 3], [4, 5, 6]])    # (2, 3)
w = np.array([[1], [0], [-1]])          # (3, 1)
print(A @ w)                            # (2, 1)
print(A + np.array([10, 20, 30]))
rng = np.random.default_rng(0)
X = rng.normal(size=(100, 5))
w = np.array([0.5, -1.0, 2.0, 0.0, 1.5]); b = 0.3
y = X @ w + b
print(X.shape, w.shape, y.shape, y[:5])
print("Задача:6")
df = pd.read_csv('data/titanic.csv')
col = [c for c in df.columns if c.lower() == 'age'][0]
age = np.array(df[col].dropna())
print('numpy:', age.mean(), age.min(), age.max())
print('pandas:', df[col].mean(), df[col].min(), df[col].max)
# Домашнее задание
rng = np.random.default_rng(0)
X = rng.normal(size=(1000, 8))
w = rng.normal(size=8)         
b = 0.3
y = X @ w + b                 

print(X.shape, w.shape, y.shape)
print(y[:5])