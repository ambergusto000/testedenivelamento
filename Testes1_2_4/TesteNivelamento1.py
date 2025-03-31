import requests
from bs4 import BeautifulSoup
import os
import zipfile
import re

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
soup = BeautifulSoup(requests.get(url).text, 'html.parser')

anexos = [(link.text.strip(), "https://www.gov.br" + link['href'] if not link['href'].startswith('http') else link['href'])
          for link in soup.find_all('a', href=True) if re.search(r'\bAnexo\s+(I|II)\b', link.text.strip(), re.IGNORECASE)]

if not anexos:
    exit()

os.makedirs("anexos", exist_ok=True)

arquivos_baixados = []
for nome, link in anexos:
    pdf_response = requests.get(link, stream=True)
    if pdf_response.status_code == 200 and 'pdf' in pdf_response.headers.get('Content-Type', ''):
        nome_arquivo = os.path.join("anexos", re.sub(r'[^\w\-_\.]', '_', nome) + ".pdf")
        with open(nome_arquivo, 'wb') as f:
            f.write(pdf_response.content)
        arquivos_baixados.append(nome_arquivo)

if arquivos_baixados:
    with zipfile.ZipFile("anexos_compactados.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in arquivos_baixados:
            zipf.write(arquivo, os.path.join("anexos", os.path.basename(arquivo)))
            
#agora é só mover o arquivo zip para a área de trabalho e extrair que está pronto!