# 📊 Sistema Automatizado de Análise e Relatórios de Vendas

Este projeto foi desenvolvido seguindo as diretrizes de "Sair do Básico com Python", focando em resolver problemas reais de empresas através de automação e análise de dados.

## 🚀 O que o projeto faz?
O sistema simula um fluxo de trabalho empresarial completo dividido em três etapas:
1. **Automação de Dados:** Gera uma base de dados realista com 1.000 registros de vendas em Excel.
2. **Análise de Dados:** Processa os dados brutos usando Pandas para identificar o faturamento total e os produtos de melhor performance, gerando um gráfico interativo com Plotly.
3. **Entrega de Resultados:** Gera automaticamente um relatório executivo em PDF com os principais insights para tomada de decisão.

## 🛠️ Tecnologias Utilizadas
* **Python 3**
* **Pandas**: Manipulação e tratamento de dados.
* **Plotly**: Visualização de dados interativa.
* **FPDF2**: Geração de relatórios em PDF.
* **Openpyxl**: Integração com arquivos Excel.

## 📁 Estrutura do Projeto
* `passo1_automacao.py`: Script de geração de dados brutos.
* `passo2_analise.py`: Script de inteligência de dados e gráficos.
* `passo3_relatorio.py`: Script de fechamento e geração de PDF.