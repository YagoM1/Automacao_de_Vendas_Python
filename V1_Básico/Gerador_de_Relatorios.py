from fpdf import FPDF
import pandas as pd

def gerar_pdf_relatorio():
    try:
        
        df = pd.read_excel('vendas_brutas.xlsx')
        total_vendas = float(df['Faturamento_Total'].sum())
        
        
        resumo = df.groupby('Produto')['Faturamento_Total'].sum()
        melhor_produto = str(resumo.idxmax())

        
        pdf = FPDF()
        pdf.add_page()
        
        
        pdf.set_font("helvetica", "B", 16)

        
        pdf.cell(0, 10, text="RELATÓRIO ESTRATÉGICO DE VENDAS", center=True, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(10)

        
        pdf.set_font("helvetica", size=12)
        
        
        texto_total = f"Faturamento Total no Periodo: R$ {total_vendas:,.2f}"
        texto_produto = f"Produto com Maior Receita: {melhor_produto}"
        
        pdf.cell(0, 10, text=texto_total, new_x="LMARGIN", new_y="NEXT")
        pdf.cell(0, 10, text=texto_produto, new_x="LMARGIN", new_y="NEXT")
        
        pdf.ln(10)
        pdf.set_font("helvetica", "I", 10)
        pdf.multi_cell(0, 10, text="Este relatorio foi gerado automaticamente via script Python para otimizacao de processos internos.")

        
        pdf.output("Relatorio_Final.pdf")
        print("Sucesso! O arquivo 'Relatorio_Final.pdf' foi criado na sua pasta.")

    except Exception as e:
        print(f"Erro ao gerar o pdf: {e}")

if __name__ == "__main__":
    gerar_pdf_relatorio()
