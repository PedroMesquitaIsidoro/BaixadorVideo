from pytube import YouTube
import os

def baixar_video(url, pasta_destino, escolha_qualidade):
    try:
        # Cria um objeto YouTube com a URL do vídeo
        video = YouTube(url)
        
        # Obtém todas as opções de qualidade disponíveis
        opcoes_qualidade = video.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc()
        
        # Lista as opções de qualidade disponíveis
        print("Opções de qualidade disponíveis:")
        for i, opcao in enumerate(opcoes_qualidade):
            print(f"{i + 1}. {opcao.resolution}")
        
        # Obtém a escolha do usuário
        escolha = int(input("Escolha a qualidade (digite o número correspondente): "))
        stream = opcoes_qualidade[escolha - 1]
        
        # Define o caminho completo do arquivo de destino
        caminho_destino = os.path.join(pasta_destino, video.title + ".mp4")
        
        # Baixa o vídeo
        print(f"Baixando: {video.title}...")
        stream.download(output_path=pasta_destino, filename=video.title)
        print(f"Download concluído! O vídeo foi salvo em: {caminho_destino}")
        
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

# Obtém a URL do usuário
url = input("Digite a URL do vídeo do YouTube: ")

# Define o caminho da pasta de destino
pasta_destino = '/home/pedro/games/Baixador'

# Obtém a escolha de qualidade do usuário
escolha_qualidade = 0
while escolha_qualidade not in range(1, 6):
    try:
        escolha_qualidade = int(input("Escolha a qualidade desejada (de 1 a 5, sendo 1 a melhor qualidade): "))
    except ValueError:
        print("Por favor, digite um número de 1 a 5.")

# Chama a função para baixar o vídeo na pasta de destino com a qualidade escolhida
baixar_video(url, pasta_destino, escolha_qualidade)
