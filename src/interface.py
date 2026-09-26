from rich.console import Console
import time

# Cria o console do Rich
console = Console()


# Mostra o título do programa
def titulo():

    console.clear()

    console.print(
        "\n🎵 [bold magenta]MÚSICA AUTOMÁTICA[/bold magenta] 🎵",
        justify="center"
    )

    console.print(
        "[dim]Letras sincronizadas com a música[/dim]\n",
        justify="center"
    )


# Mostra uma mensagem no terminal
def mensagem(texto):

    console.print(
        f"\n[bold cyan]➜[/bold cyan] {texto}"
    )


# Escreve a letra aos poucos
def escrever(texto, tempo_disponivel, cor="yellow"):

    if not texto:
        return

    # Usa parte do tempo disponível para escrever a frase
    tempo_escrita = tempo_disponivel * 0.75

    # Calcula a velocidade de cada letra
    velocidade = tempo_escrita / len(texto)

    # Define uma velocidade mínima
    if velocidade < 0.01:
        velocidade = 0.01

    # Define uma velocidade máxima
    if velocidade > 0.12:
        velocidade = 0.12

    # Escreve cada letra separadamente
    for letra in texto:

        console.print(
            f"[{cor}]{letra}[/]",
            end=""
        )

        time.sleep(velocidade)

    print()