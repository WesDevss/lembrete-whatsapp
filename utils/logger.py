from datetime import datetime

def log_envio(numero, mensagem, status):
    try:
        with open("data/logs.txt", "a", encoding="utf-8") as arquivo_log:
            horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            arquivo_log.write(f"{horario} | Número: {numero} | Mensagem: {mensagem} | Status: {status}\n")
    except Exception as e:
        print(f"Erro ao gravar no log: {e}")

if __name__ == "__main__":
    numero = input("Digite o número (com DDD e código do país): ")
    mensagem = input("Digite a mensagem: ")

    enviar_mensagem(numero, mensagem)