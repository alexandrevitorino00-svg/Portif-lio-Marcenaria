from fpdf import FPDF

def gerar_pdf(orcamento):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200,10, txt="Orçamento Marcenaria", ln=True)

    pdf.cell(200,10, txt=f"Cliente ID: {orcamento.cliente_id}", ln=True)

    pdf.cell(200,10, txt=f"Largura: {orcamento.largura}", ln=True)

    pdf.cell(200,10, txt=f"Altura: {orcamento.altura}", ln=True)

    pdf.cell(200,10, txt=f"Profundidade: {orcamento.profundidade}", ln=True)

    pdf.cell(200,10, txt=f"Preço final: R$ {orcamento.preco_final}", ln=True)

    caminho = f"orcamento_{orcamento.id}.pdf"

    pdf.output(caminho)

    return caminho