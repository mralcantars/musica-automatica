from interface import titulo
from musica import escolher_musica
from musica_automatica.src.audio import baixar_audio
from letra import tocar_letra


# Função principal
def main():

    # Mostra o título
    titulo()

    # Pede a música e busca a letra
    artista, musica, dados = (
        escolher_musica()
    )

    # Pega a duração da música
    duracao = dados.get(
        "duration"
    )

    # Baixa o áudio
    sucesso = baixar_audio(
        artista,
        musica,
        duracao
    )

    # Para o programa se o download falhar
    if not sucesso:
        return

    # Toca a música junto com a letra
    tocar_letra(
        dados["syncedLyrics"]
    )


# Inicia o programa
if __name__ == "__main__":
    main()