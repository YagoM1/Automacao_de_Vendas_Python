import pandas as pd
import plotly.express as px

try:
	df = pd.read_excel('vendas_brutas.xlsx')
	
	resumo_produtos = df.groupby('Produto')['Faturamento_Total'].sum().reset_index()
	resumo_produtos = resumo_produtos.sort_values(by='Faturamento_Total', ascending=False)	
	
	print('--- RESUMO DE FATURAMENTO ---')
	print(resumo_produtos.to_string(index=False))
	print(f'\nTotal Geral: R${df["Faturamento_Total"].sum():,.2f}')
	
	fig = px.bar(resumo_produtos, x='Produto', y='Faturamento_Total', title='Faturamento Por Produto (Análise Estratégica)',
	labels={'Faturamento_Total': 'Faturamento (R$)'},
	color='Faturamento_Total',
	template='plotly_dark')
	
	print('\nAbrindo gráfico no navegador...')
	fig.show()
	
except FileNotFoundError:
	print('ERRO: O arquivo "vendas_brutas.xlsx" não foi encontrado! ')
	print('Certifique-se de primeiro rodar o código de Automação primeiro')