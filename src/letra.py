import pygame
import time

from interface import console, escrever


# Separa o tempo e o texto de uma linha da letra
def separar_linha(linha):

    tempo, texto = linha.split(
        "]",
        1
    )

    # Remove o [
    tempo = tempo.replace(
        "[",
        ""
    )

    # Separa minutos e segundos
    minutos, segundos = tempo.split(
        ":"
    )

    # Converte tudo para segundos
    tempo_em_segundos = (
        int(minutos) * 60
        + float(segundos)
    )

    return (
        tempo_em_segundos,
        texto.strip()
    )


# Prepara todas as linhas da letra
def preparar_letra(letra):

    linhas = []

    # Percorre cada linha da letra
    for linha in letra.splitlines():

        # Ignora linhas sem tempo
        if "]" not in linha:
            continue

        try:

            tempo, texto = separar_linha(
                linha
            )

            # Guarda somente linhas que possuem texto
            if texto:

                linhas.append(
                    (
                        tempo,
                        texto
                    )
                )

        except Exception:

            # Ignora uma linha que esteja com formato inválido
            continue

    return linhas


# Espera até chegar o momento da próxima frase
def esperar_ate(
    tempo_inicio,
    tempo_frase
):

    tempo_espera = (
        tempo_frase
        - (time.time() - tempo_inicio)
    )

    if tempo_espera > 0:

        time.sleep(
            tempo_espera
        )


# Toca a música junto com a letra
def tocar_letra(letra):

    # Prepara as linhas da letra
    linhas = preparar_letra(
        letra
    )

    if not linhas:

        console.print(
            "\n✗ [bold red]"
            "Não consegui separar as letras."
            "[/bold red]"
        )

        return

    # Mostra quando começa a primeira frase
    primeira_letra = linhas[0][0]

    console.print(
        f"\n🎤 [bold cyan]"
        f"Primeira letra: "
        f"{primeira_letra:.2f}s"
        f"[/bold cyan]"
    )

    # Inicia o pygame
    pygame.mixer.init()

    try:

        # Abre o arquivo de áudio
        pygame.mixer.music.load(
            "audio/musica.mp3"
        )

    except Exception as erro:

        console.print(
            "\n✗ [bold red]"
            "Não consegui abrir o áudio."
            "[/bold red]"
        )

        console.print(
            f"[dim]{erro}[/dim]"
        )

        pygame.mixer.quit()

        return

    console.print(
        "\n🎵 [bold magenta]"
        "Música iniciando..."
        "[/bold magenta]\n"
    )

    # Começa a música
    pygame.mixer.music.play()

    # Guarda o momento em que a música começou
    tempo_inicio = time.time()

    # Percorre todas as frases
    for i, (tempo, texto) in enumerate(
        linhas
    ):

        # Espera chegar o momento da frase
        esperar_ate(
            tempo_inicio,
            tempo
        )

        # Calcula quanto tempo existe até a próxima frase
        if i + 1 < len(linhas):

            proximo_tempo = (
                linhas[i + 1][0]
            )

            tempo_disponivel = (
                proximo_tempo - tempo
            )

        else:

            # Tempo usado para a última frase
            tempo_disponivel = 2

        # Mostra a frase letra por letra
        escrever(
            texto,
            tempo_disponivel
        )

    # Espera a música terminar
    while pygame.mixer.music.get_busy():

        time.sleep(0.2)

    console.print(
        "\n🎵 [bold green]"
        "Música terminou!"
        "[/bold green]"
    )

    # Fecha o pygame
    pygame.mixer.quit()