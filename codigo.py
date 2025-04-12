# lendo base de dados
import pandas as pd 
from IPython.display import display

# lendo base
tabela = pd.read_csv("cancelamentos_sample.csv")
tabela = tabela.drop(columns="CustomerID")

display(tabela)
display(tabela.info())

tabela = tabela.dropna()
display(tabela.info())

display(tabela["cancelou"].value_counts())
display(tabela["cancelou"].value_counts(normalize=True))

# gráficos
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"  # garante que os gráficos abram

for coluna in tabela.columns:              
    grafico = px.histogram(
        tabela,
        x=coluna,
        color="cancelou",
        text_auto=True,
        color_discrete_map={
            "Sim": "#D8BFD8",
            "Não": "#98FB98"  
        }
    )
    grafico.show()

# refinamento
tabela = tabela[tabela["ligacoes_callcenter"]<=4]
tabela = tabela[tabela["dias_atraso"]<=20]
tabela = tabela[tabela["duracao_contrato"]!="Monthly"]

display(tabela["cancelou"].value_counts(normalize=True))
