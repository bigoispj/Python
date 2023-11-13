from collections import deque

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def inverter_arvore(raiz):
    if raiz is None:
        return None

    fila = deque([raiz])

    while fila:
        no_atual = fila.popleft()
        # Trocar as subárvores esquerda e direita
        no_atual.esquerda, no_atual.direita = no_atual.direita, no_atual.esquerda

        # Adicionar as subárvores à fila se existirem
        if no_atual.esquerda:
            fila.append(no_atual.esquerda)
        if no_atual.direita:
            fila.append(no_atual.direita)

# Função para imprimir a árvore em ordem de largura
def imprimir_arvore(raiz):
    if raiz is None:
        return

    fila = deque([raiz])

    while fila:
        no_atual = fila.popleft()
        print(no_atual.valor, end=" ")

        if no_atual.esquerda:
            fila.append(no_atual.esquerda)
        if no_atual.direita:
            fila.append(no_atual.direita)

# Exemplo de uso
raiz = No(1)
raiz.esquerda = No(2)
raiz.direita = No(3)
raiz.esquerda.esquerda = No(4)
raiz.esquerda.direita = No(5)

print("Árvore original:")
imprimir_arvore(raiz)

# Inverter a árvore
inverter_arvore(raiz)

print("\nÁrvore invertida:")
imprimir_arvore(raiz)
