import pandas as pd # biblioteca de analise de dados
import numpy as np # biblioteca numérica
import matplotlib.pyplot as plt # biblioteca para criar gráficos
import seaborn as sns # biblioteca de funções estatísticas, como graficos mais robustos 

# quando usamos o seabor, que é nossa biblioteca de estatística, podemos usar ela
# na criação de gráficos


sns.set_theme(style='whitegrid') # configurar o visual dos gráficos pelo seaborn

df_shoes = pd.read_csv("shoes_sales_dataset.csv")


# bloco de funções

# função 1 - ver_dados
def ver_dados():
  # o usuario escolhe quantos dados ele quer ver
  resposta = int(input('Informe quantas linhas de dados você quer ver'))
  return df_shoes.head(resposta)

# função 2 - Medidas de tendência
# média - moda - mediana
def medidas_tendencia():
  # para as medidas de tendencia, temos funções prontas para cada uma delas
  # mean() - média
  # median() - mediana
  # mode()[0] - moda

  # calculos de média
  media_precos = df_shoes['Price_USD'].mean()
  media_qtd_produtos = df_shoes['Units_Sold'].mean()
  media_total_vendas = df_shoes['Revenue_USD'].mean()

  # calculos de moda
  moda_cor_primeiro = df_shoes['Color'].mode()[0]
  moda_marca = df_shoes['Brand'].mode()[0]

  # calculo de mediana
  mediana_precos = df_shoes['Price_USD'].median()
  mediana_qtd_produtos = df_shoes['Units_Sold'].median()
  mediana_total_vendas = df_shoes['Revenue_USD'].median()

  return (print(f'A média de preços dos produtos foi de {media_precos:.2f} \n'
  f'A quantidade média de produtos vendidos foi de {media_qtd_produtos:.2f} \n'
  f'A média do total de vendas foi de {media_total_vendas:.2f}\n'
  f'O produto com a maior moda é {moda_cor_primeiro} \n'
  f'A marca com a maior moda é {moda_marca} \n'
  f'A mediana dos preços é de {mediana_precos:.2f} \n'
  f'A mediana da quantidade de produtos vendidos é de {mediana_qtd_produtos:.2f} \n'
  f'A mediana do valor total das vendas foi de {mediana_total_vendas:.2f}'))

def dispersao_variabilidade():
  plt.figure(figsize=(8,5))
  # para tratarmos o tamanho da img

  # o matplotlib, de manira simples ou facil, nao faz bloxplot
  # mas o seaborn faz
  sns.boxplot(y=df_shoes['Revenue_USD'], color='skyblue')
  plt.title('Distribuição da recita')
  plt.savefig('tabela_dispersao_variabilidade.jpg', dpi=300, bbox_inches='tight')

def histograma():
  plt.figure(figsize=(8,5))
  sns.histplot(df_shoes['Price_USD'], kde=True, color='red', bins=30)
  plt.savefig('tabela_histograma.jpg', dpi=300, bbox_inches='tight')

def dispersao():
  # precisamos de dois pontos para analise
  plt.figure(figsize=(8,5))
  # o sns.scatterplot(data=DATAFRAME, x='CAMPO X', y='CAMPO Y')
  sns.scatterplot(data=df_shoes, x='Price_USD', y='Revenue_USD')
  plt.savefig('tabela_dispersao.jpg', dpi=300, bbox_inches='tight')

def pizza():
  # 1 - preparar
  dados_pizza = df_shoes['Sales_Channel'].value_counts()
  # le dado por dado e mostra suas quantidades

  # 2 - escolher o layout de cores para os setores (cor de cada fatia)
  cores = sns.color_palette('pastel')

  # 3 - criar o grafico
  plt.figure(figsize=(8,5))
  #plt.pie(os dados, autopct='casas decimais, startangle = angulo de incio, color)
  plt.pie(dados_pizza, # de onde vem
          labels=dados_pizza.index, # titulo de cada fatia
          autopct='%1.1f%%', # como mostrar o número
          startangle=140, # angulo de inicio
          colors=cores) # cores
  plt.savefig('tabela_pizza.jpg', dpi=300, bbox_inches='tight')

medidas_tendencia()
dispersao_variabilidade()
histograma()
dispersao()
pizza()