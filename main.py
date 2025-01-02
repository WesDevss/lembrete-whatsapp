import schedule
import time
from messenger import enviar_mensagem

def solicitar_detalhes():
    """
    Solicita ao usuário os detalhes da mensagem a ser enviada.
    """
    numero = input("Digite o número (incluindo código do país e área, ex: +55XXXXXXXXXXX): ")
    mensagem = input("Digite a mensagem que deseja enviar: ")
    horario = input("Digite o horário para envio (formato HH:MM, ex: 14:30): ")

    return numero, mensagem, horario

def agendar_mensagem(numero, mensagem, horario):
    """
    Agenda uma mensagem para o horário especificado.
    """
    schedule.every().day.at(horario).do(enviar_mensagem, numero, mensagem)
    print(f"Mensagem agendada para {numero} às {horario}.")

if __name__ == "__main__":
    print("=== Sistema de Agendamento de Mensagens ===")

    while True:
        # Solicitar detalhes da mensagem
        numero, mensagem, horario = solicitar_detalhes()

        # Validar horário
        try:
            horas, minutos = map(int, horario.split(":"))
            if not (0 <= horas < 24 and 0 <= minutos < 60):
                raise ValueError
        except ValueError:
            print("Horário inválido! Use o formato HH:MM (ex: 14:30).")
            continue

        # Agendar mensagem
        agendar_mensagem(numero, mensagem, horario)

        # Perguntar se o usuário quer agendar outra mensagem
        outra = input("Deseja agendar outra mensagem? (s/n): ").lower()
        if outra != "s":
            break

    print("=== Aguardando envio das mensagens agendadas... ===")
    while True:
        schedule.run_pending()
        time.sleep(1)
