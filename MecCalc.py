import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy.constants import G, pi

# Função para calcular posição em órbita circular
def calcular_trajetoria_circular(tempo, raio, velocidade_angular):
    x = raio * np.cos(velocidade_angular * tempo)
    y = raio * np.sin(velocidade_angular * tempo)
    return x, y

# Parâmetros orbitais para dois corpos
raio_terra = 6371  # raio médio da Terra em quilômetros
altura_orbita1 = 300  # altitude em quilômetros
altura_orbita2 = 800  # altitude em quilômetros
velocidade_orbita1 = np.sqrt(G * (5.972e24) / (raio_terra + altura_orbita1) * 1e9)  # velocidade orbital em metros por segundo
velocidade_orbita2 = np.sqrt(G * (5.972e24) / (raio_terra + altura_orbita2) * 1e9)  # velocidade orbital em metros por segundo

# Tempo de simulação em segundos
tempo = np.linspace(0, 2 * pi * (raio_terra + altura_orbita1) / velocidade_orbita1, 1000)

# Calcular trajetórias orbitais
x_orbita1, y_orbita1 = calcular_trajetoria_circular(tempo, raio_terra + altura_orbita1, velocidade_orbita1 / (raio_terra + altura_orbita1))
x_orbita2, y_orbita2 = calcular_trajetoria_circular(tempo, raio_terra + altura_orbita2, velocidade_orbita2 / (raio_terra + altura_orbita2))

# Criar DataFrame com os dados simulados
dados_orbitais = pd.DataFrame({'Tempo': tempo, 'X Orbita 1': x_orbita1, 'Y Orbita 1': y_orbita1, 'X Orbita 2': x_orbita2, 'Y Orbita 2': y_orbita2})

# Configurar o estilo do Seaborn
sns.set(style="darkgrid")

# Criar gráfico de dispersão para visualizar as trajetórias orbitais
plt.figure(figsize=(10, 8))
sns.lineplot(x='X Orbita 1', y='Y Orbita 1', data=dados_orbitais, label='Órbita 1')
sns.lineplot(x='X Orbita 2', y='Y Orbita 2', data=dados_orbitais, label='Órbita 2')
plt.title('Trajetórias Orbitais Circulares ao Redor da Terra')
plt.xlabel('Posição X (km)')
plt.ylabel('Posição Y (km)')
plt.legend()
plt.show()
