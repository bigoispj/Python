import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Função para simular dados de vibração
def simular_vibracao(tempo):
    frequencia_natural = 1.5
    amplitude = 2.0
    fase = 0.5
    ruido = np.random.normal(0, 0.2, len(tempo))
    
    vibracao = amplitude * np.sin(2 * np.pi * frequencia_natural * tempo + fase) + ruido
    return vibracao

# Gerar dados fictícios de vibração ao longo do tempo
tempo = np.linspace(0, 10, 1000)
dados_vibracao = simular_vibracao(tempo)

# Criar um DataFrame com os dados
dados = pd.DataFrame({'Tempo': tempo, 'Vibração': dados_vibracao})

# Configurar o estilo do Seaborn
sns.set(style="darkgrid")

# Criar subplots para visualizações múltiplas
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Gráfico de linha para a vibração ao longo do tempo
sns.lineplot(x='Tempo', y='Vibração', data=dados, ax=ax1)
ax1.set_title('Vibração ao Longo do Tempo')
ax1.set_ylabel('Amplitude de Vibração')

# Histograma da distribuição da vibração
sns.histplot(dados['Vibração'], bins=30, kde=True, ax=ax2)
ax2.set_title('Distribuição da Vibração')
ax2.set_xlabel('Amplitude de Vibração')
ax2.set_ylabel('Frequência')

# Ajustes de layout
plt.tight_layout()

# Exibir os gráficos
plt.show()
