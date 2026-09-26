import yt_dlp

from interface import mensagem, console


# Procura e baixa o áudio da música
def baixar_audio(
    artista,
    musica,
    duracao_api
):

    mensagem(
        "Procurando o áudio..."
    )

    # Pesquisa a música no YouTube
    busca = (
        f"ytsearch5:{artista} {musica}"
    )

    opcoes_busca = {

        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
        "extract_flat": True,
        "force_ipv4": True,
    }

    try:

        # Faz a pesquisa usando o yt-dlp
        with yt_dlp.YoutubeDL(
            opcoes_busca
        ) as ydl:

            resultado = ydl.extract_info(
                busca,
                download=False
            )

    except Exception as erro:

        console.print(
            "\n✗ [bold red]"
            "Não consegui pesquisar o áudio."
            "[/bold red]"
        )

        console.print(
            f"[dim]{erro}[/dim]"
        )

        return False

    # Pega os vídeos encontrados
    entradas = resultado.get(
        "entries",
        []
    )

    if not entradas:

        console.print(
            "\n✗ [bold red]"
            "Nenhum áudio encontrado."
            "[/bold red]"
        )

        return False

    # Começa sem nenhum vídeo escolhido
    melhor_video = None

    # Guarda a menor diferença de duração
    menor_diferenca = float("inf")

    console.print(
        "\n[dim]Versões encontradas:[/dim]"
    )

    # Analisa os vídeos encontrados
    for video in entradas:

        duracao = video.get(
            "duration"
        )

        titulo_video = video.get(
            "title",
            ""
        )

        if duracao is None:
            continue

        console.print(
            f"[dim]• {titulo_video} "
            f"({duracao:.0f}s)[/dim]"
        )

        # Compara a duração do vídeo com a duração da API
        diferenca = abs(
            duracao - duracao_api
        )

        # Guarda o vídeo mais próximo
        if diferenca < menor_diferenca:

            menor_diferenca = diferenca

            melhor_video = video

    # Se não encontrou duração, usa o primeiro
    if melhor_video is None:

        melhor_video = entradas[0]

    # Pega o endereço do vídeo
    video_url = melhor_video.get(
        "webpage_url"
    )

    # Se não tiver o endereço, monta usando o ID
    if not video_url:

        video_id = melhor_video.get(
            "id"
        )

        video_url = (
            "https://www.youtube.com/watch?v="
            + video_id
        )

    console.print(
        f"\n🎧 [dim]Versão escolhida: "
        f"{melhor_video.get('title', '')}"
        f"[/dim]"
    )

    # Configura o download
    opcoes_download = {

        "format":
            "bestaudio[ext=m4a]/"
            "bestaudio[ext=webm]/"
            "bestaudio/best",

        # Nome e localização do arquivo
        "outtmpl":
            "audio/musica.%(ext)s",

        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
        "noprogress": True,
        "force_ipv4": True,

        # Número de tentativas
        "retries": 3,
        "fragment_retries": 3,

        # Converte o áudio para MP3
        "postprocessors": [

            {
                "key":
                    "FFmpegExtractAudio",

                "preferredcodec":
                    "mp3",

                "preferredquality":
                    "192",
            }
        ],
    }

    try:

        # Faz o download
        with yt_dlp.YoutubeDL(
            opcoes_download
        ) as ydl:

            ydl.download([
                video_url
            ])

    except Exception as erro:

        console.print(
            "\n✗ [bold red]"
            "Erro ao baixar o áudio."
            "[/bold red]"
        )

        console.print(
            f"[dim]{erro}[/dim]"
        )

        return False

    console.print(
        "\n✓ [bold green]"
        "Áudio baixado!"
        "[/bold green]"
    )

    return True