import pywhatkit as kit
from datetime import datetime

def enviar_mensagem(numero, mensagem):
    """
    Envia uma mensagem no WhatsApp usando pywhatkit.
    """
    try:
        # Enviar mensagem no WhatsApp
        now = datetime.now()
        hora = now.hour
        minuto = now.minute + 2  # Garantir envio em breve (caso tenha agendado no horário atual)
        kit.sendwhatmsg(numero, mensagem, hora, minuto)

        print(f"[SUCESSO] Mensagem enviada para {numero}: {mensagem}")
    except Exception as e:
        print(f"[ERRO] Não foi possível enviar mensagem para {numero}: {e}")
