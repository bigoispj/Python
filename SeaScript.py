import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Criando um conjunto de dados fictício com três variáveis
np.random.seed(42)
data_size = 100
variable1 = np.random.normal(0, 1, data_size)
variable2 = np.random.normal(0, 2, data_size)
variable3 = np.random.normal(0, 3, data_size)

# Criando um DataFrame do Pandas
import pandas as pd
df = pd.DataFrame({'Variable1': variable1, 'Variable2': variable2, 'Variable3': variable3})

# Configurando o estilo e contexto do Seaborn para uma apresentação mais elegante
sns.set(style="whitegrid")
sns.set_context("notebook", font_scale=1.2)

# Criando um gráfico de dispersão pairplot com regressões lineares e distribuições marginais
sns.pairplot(df, kind="reg", diag_kind="kde", markers='o', height=2.5)
plt.suptitle("Pairplot com Regressões Lineares e Distribuições Marginais", y=1.02)
plt.show()
