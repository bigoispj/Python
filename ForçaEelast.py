import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Função para simular o comportamento elástico do material
def modelo_elastico(forca_aplicada):
    elasticidade = 200  # Coeficiente de elasticidade fictício
    return elasticidade * forca_aplicada

# Gerar dados fictícios
np.random.seed(42)
forcas = np.random.uniform(0, 10, 100)
deformacoes = modelo_elastico(forcas) + np.random.normal(0, 5, 100)

# Criar um DataFrame com os dados
import pandas as pd
dados = pd.DataFrame({'Força Aplicada': forcas, 'Deformação': deformacoes})

# Configurar o estilo do Seaborn
sns.set(style="whitegrid")

# Criar um gráfico de dispersão com linha de regressão
plt.figure(figsize=(10, 6))
sns.regplot(x='Força Aplicada', y='Deformação', data=dados, scatter_kws={'s': 50}, line_kws={'color': 'red'})

# Adicionar título e rótulos aos eixos
plt.title('Relação Força vs. Deformação em um Material Elástico', fontsize=16)
plt.xlabel('Força Aplicada (N)', fontsize=14)
plt.ylabel('Deformação (mm)', fontsize=14)

# Exibir o gráfico
plt.show()
