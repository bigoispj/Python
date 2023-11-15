import numpy as np
import matplotlib.pyplot as plt

# Função para simular o impacto de um imposto sobre transações financeiras
def impacto_imposto(transacoes, taxa_imposto):
    transacoes_taxadas = transacoes * (1 - taxa_imposto)
    receita_tributaria = np.sum(transacoes * taxa_imposto)
    return transacoes_taxadas, receita_tributaria

# Parâmetros iniciais
np.random.seed(42)
transacoes_anuais = np.random.normal(1000000, 50000, 10)  # Transações financeiras anuais em um mercado fictício

# Simulação sem imposto
transacoes_sem_imposto = transacoes_anuais
receita_sem_imposto = 0

# Simulação com imposto de 5%
transacoes_com_imposto, receita_com_imposto = impacto_imposto(transacoes_anuais, 0.05)

# Análise econômica - Gráfico de barras comparativo
labels = ['Ano 1', 'Ano 2', 'Ano 3', 'Ano 4', 'Ano 5', 'Ano 6', 'Ano 7', 'Ano 8', 'Ano 9', 'Ano 10']
width = 0.35
fig, ax = plt.subplots(figsize=(10, 6))

rects1 = ax.bar(np.arange(len(labels)) - width/2, transacoes_sem_imposto, width, label='Sem Imposto')
rects2 = ax.bar(np.arange(len(labels)) + width/2, transacoes_com_imposto, width, label='Com Imposto')

ax.set_xlabel('Anos')
ax.set_ylabel('Transações Financeiras')
ax.set_title('Impacto de um Imposto sobre Transações Financeiras')
ax.set_xticks(np.arange(len(labels)))
ax.set_xticklabels(labels)
ax.legend()

# Adicionar rótulos de valor nas barras
def autolabel(rects, receitas):
    for i, rect in enumerate(rects):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., height,
                f'{int(height)}\n(${receitas[i]:,.0f})',
                ha='center', va='bottom', color='black')

autolabel(rects1, [0] * len(labels))
autolabel(rects2, receita_com_imposto)

plt.show()
