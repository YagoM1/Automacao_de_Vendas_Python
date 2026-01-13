import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def gerar_dados_vendas(n_linhas=1000):
    produtos = ['Laptop', 'Mouse', 'Monitor', 'Teclado', 'Headset']
    regioes = ['Norte', 'Sul', 'Leste', 'Oeste']
    
    # Criamos as listas garantindo que todas usem o mesmo n_linhas
    dados = {
        'Data': [datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(n_linhas)],
        'Produto': [np.random.choice(produtos) for _ in range(n_linhas)],
        'Regiao': [np.random.choice(regioes) for _ in range(n_linhas)],
        'Quantidade': np.random.randint(1, 10, size=n_linhas), # Adicionado 'size='
        'Preco_Unitario': np.random.uniform(50, 3000, size=n_linhas).round(2) # Adicionado 'size='
    }
    
    # Criar o DataFrame
    df = pd.DataFrame(dados)
    
    # Cálculo do faturamento
    df['Faturamento_Total'] = df['Quantidade'] * df['Preco_Unitario']
    
    # Salvar
    df.to_excel('vendas_brutas.xlsx', index=False)
    print(f"Sucesso! Arquivo gerado com {len(df)} linhas.")

gerar_dados_vendas(1000)


