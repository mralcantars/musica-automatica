Projeto em Python que busca uma música, encontra sua letra sincronizada e reproduz o áudio enquanto exibe a letra no terminal.

Funcionalidades
    - Busca de músicas pela API do LRCLIB
    - Download automático do áudio
    - Letras sincronizadas
    - Exibição das letras no terminal
    - Código organizado em módulos

Tecnologias
    - Python 3.13
    - Requests
    - Rich
    - Pygame
    - yt-dlp
    - FFmpeg
    - LRCLIB

Estrutura
musica_automatica/ 
├── src/ 
│   ├── main.py 
│   ├── interface.py 
│   ├── musica.py 
│   ├── audio.py 
│   └── letra.py 
├── audio/ 
├── .gitignore 
├── README.md 
└── requirements.txt

Como executar
1- Instale as dependências:
    pip install -r requirements.txt

2- Execute o programa:
    python src/main.py

3- Depois informe o artista e a música.

Objetivo
Projeto desenvolvido para praticar Python, APIs, bibliotecas externas, reprodução de áudio e organização de código.