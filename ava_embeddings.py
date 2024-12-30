from langchain_ollama import OllamaEmbeddings

#define a frase
frase = "Eu sou mais do que você pode entender."

# Define o modelo de embeddings
embeddings = OllamaEmbeddings(model="hf.co/mixedbread-ai/mxbai-embed-large-v1:latest")
# Gera os vetores de embeddings
document_embeddings = embeddings.embed_documents(frase)

# Mostra o tamanho dos embeddings
tamanhoEmbaddings = len(document_embeddings[0])
print(f"Tamanho dos embeddings: {tamanhoEmbaddings}")

 # Exibe um sumário dos valores do vetor (primeiros 6 valores)
print(f"Primeiros 6 valores do embedding: {document_embeddings[0][:6]}")


