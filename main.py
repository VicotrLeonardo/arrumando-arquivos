import os
# Organizar a pasta de Downloads

audios = ['.mp3', '.wav']
videos = ['.mp4', '.mov', '.avi']
imagens = ['.jpg', '.jpeg', 'png']
documentos = ['.txt', '.log', '.pdf','.pptx', '.odp' , '.docx']
winrar = ['.zip', '.rar']

def pegar_extensao(nomeArquivo):
    index = nomeArquivo.rfind('.')
    return nomeArquivo[index:]


def organizar(diretorio):
    AUDIO_DIR = os.path.join(diretorio, "audios")
    IMAGENS_DIR = os.path.join(diretorio, "imagens")
    DOCUMENTOS_DIR = os.path.join(diretorio, "documentos")
    VIDEOS_DIR = os.path.join(diretorio, "videos")
    WINRAR_DIR = os.path.join(diretorio, "docs_zipados")
    OUTROS_DIR = os.path.join(diretorio, "outros")

    list_dirs = [AUDIO_DIR, IMAGENS_DIR, DOCUMENTOS_DIR, VIDEOS_DIR , WINRAR_DIR, OUTROS_DIR]

    for dir in list_dirs:
        if not os.path.isdir(dir):
             os.mkdir(dir)

    nomes_arquivos = os.listdir(diretorio)
    print(nomes_arquivos)
    nova_pasta = ''
    for arquivo in nomes_arquivos:
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            extensao = str.lower(pegar_extensao(arquivo))
            if extensao in audios:
                nova_pasta = AUDIO_DIR
            elif extensao in videos:
                nova_pasta = VIDEOS_DIR
            elif extensao in imagens:
                nova_pasta = IMAGENS_DIR
            elif extensao in documentos:
                nova_pasta = DOCUMENTOS_DIR
            elif extensao in winrar:
                nova_pasta = WINRAR_DIR
            else:
                nova_pasta = OUTROS_DIR

            velhoCaminho = os.path.join(diretorio, arquivo)
            novoCaminho = os.path.join(nova_pasta, arquivo)
            os.rename(velhoCaminho, novoCaminho)


organizar(r"/Users/novodono/downloads")
