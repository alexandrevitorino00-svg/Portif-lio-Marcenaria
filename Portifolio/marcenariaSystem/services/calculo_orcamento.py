def calcular_area(largura, altura, profundidade):

    laterais = 2 * (altura * profundidade)
    topo_base = 2 * (largura * profundidade)
    fundo = largura * altura
    
    return laterais + topo_base + fundo

def calcular_custo(area_total_m2, preco_mdf):

    custo_material = area_total_m2 * preco_mdf
    mao_de_obra = custo_material * 0.5
    lucro = custo_material * 0.3
    
    preco_final = custo_material + mao_de_obra + lucro
    
    return {
        "custo_material": round(custo_material, 2),
        "mao_de_obra": round(mao_de_obra, 2),
        "lucro": round(lucro, 2),
        "preco_final": round(preco_final, 2)
    }

def calcular_orcamento(largura, altura, profundidade, preco_mdf):
    
    area_cm2 = calcular_area(largura, altura, profundidade)
    
    area_m2 = area_cm2 / 10000
    
    custos = calcular_custo(area_m2, preco_mdf)
    
    return {
        "area_m2": round(area_m2, 4),
        "custo_material": custos["custo_material"],
        "mao_de_obra": custos["mao_de_obra"],
        "lucro": custos["lucro"],
        "preco_final": custos["preco_final"]
    }