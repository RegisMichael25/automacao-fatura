import pandas as pd
import re
from datetime import datetime

dados_texto = """9 ago - Uber* Trip - R$ 14,56 26 ago - Eithalanche - R$ 9,50 25 ago - Uber* Trip - R$ 12,62 25 ago - Uber* Trip - R$ 8,85 20 ago - IfdAb Comercio de Ali - R$ 42,88 20 ago - Pg 99 Ride - R$ 14,95 18 ago - Amazonprimebr - R$ 19,90 17 ago - Cafe do Joao - R$ 10,50 17 ago - Uber Trip - R$ 15,15 16 ago - IfdHoly Pizzas Sul Li - R$ 83,17 16 ago - Pg 99 Ride - R$ 9,20 15 ago - Zp Ih Ar Condicionado 1/6 - R$ 110,73 15 ago - Uber Trip - R$ 32,15 14 ago - Eithalanche - R$ 8,00 13 ago - IfdAb Comercio de Ali - R$ 42,88 10 ago - Erivanlemosde 1/2 - R$ 100,00 10 ago - Cafe do Joao - R$ 4,50 09 ago - Ifd*Ifood Club - R$ 12,90 02 ago - Amazon 2/6 - R$ 19,69 02 ago - Amazon 2/6 - R$ 33,11 02 ago - Ingressos Beach Park 4/6 - R$ 28,16 02 ago - Auto Escola Triunfo 3/10 - R$ 151,00 02 ago - Maresol Pratas e Semi 2/3 - R$ 71,66 02 ago - Mercadao Tendtudo Curi 2/2 - R$ 55,33"""

print("\n=== DADOS RECEBIDOS ===")

def processar_dados_financeiros(texto):
    padrao = r'(\d{1,2}\s+ago)\s+-\s+(.+?)\s+-\s+R\$\s+(\d+,\d+)'
    transacoes = re.findall(padrao, texto)
    print(transacoes)
    dados_processados = []
    ano_atual = datetime.now().year
    
    for data_str, descricao, valor_str in transacoes:
        dia = data_str.split()[0]
        data_formatada = f"{dia.zfill(2)}/08/{ano_atual}"
        valor_float = float(valor_str.replace(',', '.'))
        
        dados_processados.append({
            'Data': data_formatada,
            'Descrição': descricao,
            'Valor': valor_float,
            'Valor_Formatado': f"R$ {valor_str}"
        })
    
    return dados_processados

print("\n=== PROCESSANDO DADOS FINANCEIROS ===")
dados_lista = processar_dados_financeiros(dados_texto)
print("\n=== DADOS PROCESSADOS ===")
df = pd.DataFrame(dados_lista)
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

print("\n=== EXPORTANDO PARA EXCEL ===")

caminho_completo = '/home/regis/Documentos/Workspace/projpy/dados/dados_financeiros'
with pd.ExcelWriter(caminho_completo+'.ods', engine='odf') as writer:
    df_export = df[['Data', 'Descrição', 'Valor', 'Valor_Formatado']]
    df_export.to_excel(writer, index=False, sheet_name='Transações')

with pd.ExcelWriter(caminho_completo+'.xlsx', engine='openpyxl') as writer:
    df_export = df[['Data', 'Descrição', 'Valor', 'Valor_Formatado']]
    df_export.to_excel(writer, index=False, sheet_name='Transações')
