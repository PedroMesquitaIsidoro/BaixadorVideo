import requests
import os

def baixar_video(url, pasta_destino):
    try:
        # Faz uma solicitação para obter o conteúdo do vídeo
        response = requests.get(url, stream=True)
        
        # Obtém o nome do arquivo do URL
        nome_arquivo = os.path.basename(url)
        
        # Define o caminho completo do arquivo de destino
        caminho_destino = os.path.join(pasta_destino, nome_arquivo)
        
        # Baixa o vídeo
        print(f"Baixando o vídeo...")
        with open(caminho_destino, 'wb') as arquivo:
            for chunk in response.iter_content(chunk_size=8192):
                arquivo.write(chunk)
        
        print(f"Download concluído! O vídeo foi salvo em: {caminho_destino}")
        
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

# Obtém a URL do usuário
url = input("Digite a URL do vídeo: ")

# Define o caminho da pasta de destino
pasta_destino = '/home/pedro/games/BaixadorVideo/videos'

# Chama a função para baixar o vídeo na pasta de destino
baixar_video(url, pasta_destino)
