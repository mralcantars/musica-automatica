import requests
import unicodedata

from interface import console


# Remove acentos e deixa o texto em letras minúsculas
def normalizar(texto):

    texto = unicodedata.normalize(
        "NFD",
        texto
    )

    texto = "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    return texto.lower().strip()


# Procura a música na API do LRCLIB
def buscar_musica(artista, musica):

    url = "https://lrclib.net/api/search"

    parametros = {
        "track_name": normalizar(musica),
        "artist_name": normalizar(artista)
    }

    try:

        # Faz a pesquisa na API
        resposta = requests.get(
            url,
            params=parametros
        )

        # Converte a resposta para Python
        dados = resposta.json()

    except Exception:

        # Retorna vazio se acontecer algum erro
        return None

    # Verifica se a resposta é uma lista
    if not isinstance(dados, list):
        return None

    # Verifica se encontrou alguma música
    if len(dados) == 0:
        return None

    # Retorna o primeiro resultado
    return dados[0]


# Pede o artista e a música ao usuário
def escolher_musica():

    while True:

        artista = input(
            "🎤 Artista: "
        ).strip()

        musica = input(
            "🎵 Música: "
        ).strip()

        # Procura a música
        dados = buscar_musica(
            artista,
            musica
        )

        # Verifica se encontrou uma letra sincronizada
        if dados:

            letra = dados.get(
                "syncedLyrics"
            )

            if letra:

                return (
                    artista,
                    musica,
                    dados
                )

        # Caso não encontre, pede novamente
        console.print(
            "\n✗ [bold red]"
            "Música não encontrada."
            "[/bold red]"
        )

        console.print(
            "[dim]Tente novamente.[/dim]\n"
        )