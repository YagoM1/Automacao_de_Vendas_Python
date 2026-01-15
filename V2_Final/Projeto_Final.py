import pandas as pd
import plotly.express as px
import requests
from fpdf import FPDF
from dash import Dash, html, dcc
import numpy as np


def gerar_dados():
    n_linhas = 1000
    dados = {
        'Produto': np.random.choice(['Monitor', 'Laptop', 'Teclado', 'Mouse', 'Headset'], n_linhas),
        'Quantidade': np.random.randint(1, 10, n_linhas),
        'Preco_Unitario': np.random.uniform(50, 2000, n_linhas)
    }
    df = pd.DataFrame(dados)
    df['Faturamento_Total'] = df['Quantidade'] * df['Preco_Unitario']
    df.to_excel('vendas_brutas.xlsx', index=False)
    return df


def buscar_dolar():
    try:
        url = "https://economia.awesomeapi.com.br/last/USD-BRL"
        r = requests.get(url).json()
        return float(r['USDBRL']['bid'])
    except:
        return 5.50


def gerar_relatorio(df, cotacao):
    total_brl = df['Faturamento_Total'].sum()
    total_usd = total_brl / cotacao
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(0, 10, text="RELATORIO EXECUTIVO DE VENDAS", center=True, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    
    pdf.set_font("helvetica", size=12)
    pdf.cell(0, 10, text=f"Total em Reais: R$ {total_brl:,.2f}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, text=f"Cotacao USD: R$ {cotacao:.2f}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, text=f"Total em Dolar: U$ {total_usd:,.2f}", new_x="LMARGIN", new_y="NEXT")
    pdf.output("Relatorio_Final_Profissional.pdf")


df_vendas = gerar_dados()
dolar_hoje = buscar_dolar()
gerar_relatorio(df_vendas, dolar_hoje)


app = Dash(__name__)
fig = px.bar(df_vendas.groupby('Produto')['Faturamento_Total'].sum().reset_index(), 
             x='Produto', y='Faturamento_Total', title="Performance por Produto", template="plotly_dark")

app.layout = html.Div([
    html.H1("Dashboard de Vendas Automático"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    print("PDF Gerado! Dashboard em: http://127.0.0.1:8050")
    app.run_server(debug=False, port=8050)
