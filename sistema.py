import spacy
from transformers import pipeline

# Carregar o modelo de PLN do spaCy para português
nlp = spacy.load("pt_core_news_sm")

# Carregar o modelo de resposta automática do Hugging Face (Transformers)
qa_pipeline = pipeline("question-answering", model="pierreguillou/bert-base-cased-squad-v1")

# Função para processar comandos do usuário
def entender_comando(comando):
    doc = nlp(comando)
    entidades = [(ent.text, ent.label_) for ent in doc.ents]
    print("Entidades encontradas:", entidades)
    return doc

# Função para gerar resposta automática
def responder_pergunta(pergunta, contexto):
    resposta = qa_pipeline(question=pergunta, context=contexto)
    return resposta['answer']

# Função principal do assistente
def assistente_virtual():
    print("Olá, eu sou seu assistente virtual! Como posso ajudar hoje?")
    while True:
        comando = input("Você: ")
        if comando.lower() in ["sair", "exit", "quit"]:
            print("Assistente: Até logo!")
            break
        elif "quem é" in comando or "o que é" in comando:
            contexto = "Albert Einstein foi um físico teórico alemão, conhecido por desenvolver a teoria da relatividade."
            resposta = responder_pergunta(comando, contexto)
            print(f"Assistente: {resposta}")
        else:
            entender_comando(comando)

# Executar o assistente
assistente_virtual()
