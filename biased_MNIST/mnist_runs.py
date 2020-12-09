import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

data = pd.read_csv('atml_mnist.csv')
print(data.columns)

ax = data.plot(x='Rho', y=['REBIAS', 'VANILLA'], figsize=(10,5), grid=True)
ax.set_xlabel("Rho")
ax.set_ylabel("Final Val. Accuracy")
ax.set_title("Rebias vs Vanilla over different Rho")
#data.plot(x = 'Rho', y = 'REBIAS', figsize=(10,5), grid=True, kind = 'scatter')
#data.plot(x = 'Rho', y = 'VANILLA', figsize=(10,5), grid=True, kind = 'scatter')

plt.show()
print(data)