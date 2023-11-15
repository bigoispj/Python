import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
from scipy.stats import skew, kurtosis

# Simular dados de teste de durabilidade do motor
np.random.seed(123)
num_amostras = 500
vida_ultima = np.random.gamma(8, scale=10, size=num_amostras)
temperatura_operacao = np.random.normal(80, 5, size=num_amostras)
falha = np.random.choice([0, 1], size=num_amostras, p=[0.9, 0.1])

# Criar DataFrame com os dados simulados
dados_motor = pd.DataFrame({'Vida Útil (horas)': vida_ultima, 'Temperatura de Operação (C)': temperatura_operacao, 'Falha': falha})

# Configurar o estilo do Seaborn
sns.set(style="whitegrid")

# Gráfico conjunto (pair plot) para visualizar relações entre variáveis
sns.pairplot(dados_motor, hue="Falha", diag_kind="kde", markers=["o", "s"], palette="husl")
plt.suptitle('Pair Plot - Relações entre Variáveis', y=1.02)
plt.show()

# Correlação entre variáveis
correlacao = dados_motor.corr()

# Mapa de calor para visualizar correlações
plt.figure(figsize=(10, 8))
sns.heatmap(correlacao, annot=True, cmap="coolwarm", fmt=".2f")
plt.title('Mapa de Calor - Correlação entre Variáveis')
plt.show()

# Estatísticas descritivas e distribuição da vida útil
media_vida = dados_motor['Vida Útil (horas)'].mean()
mediana_vida = dados_motor['Vida Útil (horas)'].median()
skewness_vida = skew(dados_motor['Vida Útil (horas)'])
kurtosis_vida = kurtosis(dados_motor['Vida Útil (horas)'])

# Histograma e curva de ajuste para a vida útil
plt.figure(figsize=(12, 6))
sns.histplot(dados_motor['Vida Útil (horas)'], bins=30, kde=True, color='skyblue', stat="density")
plt.title('Distribuição da Vida Útil do Motor')
plt.xlabel('Vida Útil (horas)')
plt.ylabel('Densidade')

# Adicionar curva de ajuste (PDF) à distribuição
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, media_vida, dados_motor['Vida Útil (horas)'].std())
plt.plot(x, p, 'k', linewidth=2)

# Adicionar estatísticas descritivas ao gráfico
plt.text(xmax - 10, 0.02, f'Média: {media_vida:.2f}\nMediana: {mediana_vida:.2f}\nSkewness: {skewness_vida:.2f}\nKurtosis: {kurtosis_vida:.2f}', 
         verticalalignment='bottom', horizontalalignment='right', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))

plt.show()
