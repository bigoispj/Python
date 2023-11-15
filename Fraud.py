import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import networkx as nx
import matplotlib.pyplot as plt

# Simulação de dados fictícios
np.random.seed(42)
clientes = ['Cliente A', 'Cliente B', 'Cliente C', 'Cliente D', 'Cliente E', 'Cliente F']
transacoes = pd.DataFrame({
    'Cliente': np.random.choice(clientes, 100),
    'Valor': np.random.uniform(1000, 100000, 100),
    'Data': pd.date_range(start='2022-01-01', end='2022-04-10', freq='D')
})

# Função para criar um gráfico de rede com a biblioteca NetworkX
def criar_grafo_relacionamento(df):
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge('Banco', row['Cliente'], weight=row['Valor'])
    return G

# Função para detectar anomalias usando Isolation Forest
def detectar_anomalias_isolation_forest(df):
    modelo = IsolationForest(contamination=0.05)
    df['Anomalia'] = modelo.fit_predict(df[['Valor']])
    return df

# Função para realizar análise de entidade e relacionamento (AED)
def analise_aed(df):
    clientes_unicos = df['Cliente'].unique()
    matriz_relacionamento = pd.DataFrame(index=clientes_unicos, columns=clientes_unicos, data=0)

    for cliente in clientes_unicos:
        transacoes_cliente = df[df['Cliente'] == cliente]
        for _, row in transacoes_cliente.iterrows():
            matriz_relacionamento.loc[cliente, row['Cliente']] += row['Valor']

    return matriz_relacionamento

# Função para realizar a detecção de clusters usando DBSCAN
def detectar_clusters(matriz_relacionamento):
    X = StandardScaler().fit_transform(matriz_relacionamento)
    modelo_dbscan = DBSCAN(eps=0.8, min_samples=1)
    matriz_relacionamento['Cluster'] = modelo_dbscan.fit_predict(X)
    return matriz_relacionamento

# Função principal
def main():
    # Simular a detecção de anomalias nas transações
    transacoes_anomalias = detectar_anomalias_isolation_forest(transacoes)

    # Criar e visualizar um gráfico de rede de entidades
    grafo_relacionamento = criar_grafo_relacionamento(transacoes_anomalias)
    nx.draw(grafo_relacionamento, with_labels=True, font_weight='bold')
    plt.show()

    # Realizar análise de entidade e relacionamento (AED)
    matriz_relacionamento = analise_aed(transacoes)

    # Detectar clusters na matriz de relacionamento
    matriz_relacionamento = detectar_clusters(matriz_relacionamento)

    # Exibir resultados
    print("Matriz de Relacionamento:")
    print(matriz_relacionamento)

if __name__ == "__main__":
    main()
