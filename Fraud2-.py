import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# Simulação de dados fictícios
clientes = ['Cliente A', 'Cliente B', 'Cliente C', 'Cliente D', 'Cliente E', 'Cliente F']
transacoes = pd.DataFrame({
    'Cliente_origem': np.random.choice(clientes, 100),
    'Cliente_destino': np.random.choice(clientes, 100),
    'Valor': np.random.uniform(1000, 100000, 100),
    'Data': pd.date_range(start='2022-01-01', end='2022-04-10', freq='D')
})

# Criar um gráfico de rede interativo
fig = make_subplots(rows=1, cols=1,
                    subplot_titles=['Rede de Transações Dinâmica'],
                    specs=[[{'type': 'scatter'}]])

# Adicionar as arestas da rede (transações)
edge_trace = go.Scatter(
    x=[],
    y=[],
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

# Adicionar os nós da rede (clientes)
node_trace = go.Scatter(
    x=[],
    y=[],
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='YlGnBu',
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        )
    )
)

# Adicionar frames para animação
frames = [go.Frame(data=[edge_trace, node_trace],
                   name=str(date)) for date in transacoes['Data'].unique()]

for date in transacoes['Data'].unique():
    subset = transacoes[transacoes['Data'] <= date]

    # Adicionar as arestas
    edge_x = []
    edge_y = []
    for edge in subset.itertuples():
        edge_x.extend([subset.loc[edge.Index, 'Cliente_origem'], subset.loc[edge.Index, 'Cliente_destino'], None])
        edge_y.extend([None, None, None])

    # Adicionar os nós
    node_x = subset['Cliente_origem'].tolist() + subset['Cliente_destino'].tolist()
    node_y = subset['Cliente_destino'].tolist() + subset['Cliente_origem'].tolist()

    edge_trace['x'] = edge_x
    edge_trace['y'] = edge_y
    node_trace['x'] = node_x
    node_trace['y'] = node_y

    fig.add_trace(edge_trace)
    fig.add_trace(node_trace)

# Atualizar layout
fig.update_layout(
    showlegend=False,
    hovermode='closest',
    margin=dict(b=0, l=0, r=0, t=0),
)

# Adicionar botões de animação
fig.frames = frames
fig.update_layout(updatemenus=[{
    'type': 'buttons',
    'showactive': False,
    'buttons': [{
        'label': 'Play',
        'method': 'animate',
        'args': [None, dict(frame=dict(duration=500, redraw=True), fromcurrent=True)],
    }, {
        'label': 'Pause',
        'method': 'animate',
        'args': [[None], dict(frame=dict(duration=0, redraw=True), mode='immediate')],
    }],
}])

# Exibir o gráfico
fig.show()
