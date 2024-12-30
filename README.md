## Ollama Embeddings Demo

Este repositório demonstra o uso de embeddings gerados com o modelo Ollama utilizando a biblioteca `langchain_ollama`. O exemplo converte uma frase em vetores de embeddings e exibe o tamanho do vetor e um resumo dos 6 primeiros valores.

### 1. Requisitos

Certifique-se de ter os seguintes itens instalados:
- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)
- Ollama instalado no sistema.(Acesse o site oficial: Ollama.com e siga as instruções para instalação no seu sistema operacional.)

### 2º Baixe o modelo Ollama:
Acesse o repositório do modelo: Hugging Face
Este script utiliza o modelo "hf.co/mixedbread-ai/mxbai-embed-large-v1:latest."

### 3. Configuração do Ambiente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/DamiaoNetto/ollama-embedding-demo.git
   cd ollama-embedding-demo

### 4º Instale as dependências:
    pip install -r requirements.txt


### 5º Execute o script:

Certifique-se de estar no diretório do projeto e execute:
    python ava_embeddings.py

*O script realiza as seguintes etapas:*
    1- Define uma frase.
    2- Usa o modelo mxbai-embed-large para gerar um vetor de embeddings dessa frase.
    3- Exibe o tamanho do vetor gerado (1024 valores) e os primeiros 6 valores.
