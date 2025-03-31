import tabula
import pandas as pd
import zipfile

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

lista_tabelas = tabula.read_pdf(
    url,
    pages='all',
    lattice=True,
    stream=False,
    guess=False,
    multiple_tables=True,
    pandas_options={'header': None}
)

dfs_processados = []
for df in lista_tabelas:
    df = df.dropna(how='all')
    df = df[~df.iloc[:, 0].astype(str).str.contains('PROCEDIMENTO', case=False, na=False)]
    
    if len(df.columns) >= 12:
        colunas_corretas = [
            "Procedimento", "RN(Alteração)", "Vigência", "OD", "AMB", 
            "HCO", "HSO", "REF", "PAC", "DUT", "Subgrupo", "Grupo", "Capítulo"
        ]
        df.columns = colunas_corretas[:len(df.columns)]
        dfs_processados.append(df)

df_combinado = pd.concat(dfs_processados, ignore_index=True)
df_combinado = df_combinado.fillna('')

csv_path = 'procedimentos.csv'
with open(csv_path, 'w', encoding='utf-8-sig') as f:
    f.write(' ;  '.join(df_combinado.columns) + '\n')
    
    for _, row in df_combinado.iterrows():
        line = ' ;  '.join(str(value) for value in row)
        f.write(line + '\n')

zip_path = 'Teste_Augusto_Ramos.zip'
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_path)

print(f"Arquivo CSV formatado salvo em: {csv_path}")
print(f"Arquivo ZIP gerado em: {zip_path}")