# Projeto de Lembrete do WhatsApp

## Descrição

O **Projeto de Lembrete do WhatsApp** é uma solução de automação que permite enviar mensagens no WhatsApp de maneira programada ou imediata. O objetivo principal desse projeto é automatizar o envio de mensagens de lembretes ou qualquer tipo de mensagem em horários específicos, de forma prática e sem a necessidade de interação manual.

### Funcionalidades

1. **Envio de Mensagens Automáticas**:
   O script permite o envio automático de mensagens via WhatsApp para números específicos, com ou sem agendamento.

2. **Agendamento de Mensagens**:
   O usuário pode agendar o envio de uma mensagem para um horário futuro. A automação irá garantir que a mensagem seja enviada exatamente no horário especificado.

3. **Registro de Logs**:
   Todas as mensagens enviadas são registradas em um arquivo de log. O log contém informações sobre a data e hora do envio, número de destino, conteúdo da mensagem e status (sucesso ou erro).

4. **Gestão de Erros**:
   Caso algum erro ocorra durante o envio (por exemplo, número incorreto ou falha na conexão), o erro será registrado no arquivo de log para facilitar o diagnóstico.

---

## Tecnologias Utilizadas

- **Python**: Linguagem de programação usada para desenvolver o script e automatizar o processo.
- **pywhatkit**: Biblioteca Python que permite a automação de tarefas no WhatsApp Web, incluindo o envio de mensagens.
- **datetime**: Biblioteca Python usada para lidar com data e hora, possibilitando o agendamento de mensagens.
- **Arquivos de Log**: Arquivo de texto onde são registrados os detalhes dos envios (número, mensagem, status).

---

## Como Funciona?

1. **Entrada do Usuário**:
   - O script solicita ao usuário que forneça:
     - **Número de Destino**: O número do WhatsApp para o qual a mensagem será enviada, incluindo o código do país e DDD (exemplo: `+55 11 99999-9999`).
     - **Mensagem**: O conteúdo da mensagem que será enviada.
     - **Hora de Envio**: O horário em que a mensagem será enviada. Pode ser um horário agendado ou o envio imediato.

2. **Envio de Mensagem**:
   - O script utiliza a biblioteca **pywhatkit** para enviar a mensagem:
     - Se o horário for agendado, o script espera até o horário especificado e, em seguida, envia a mensagem.
     - Se o envio for imediato, o script envia a mensagem assim que o usuário fornecer as informações.

3. **Log de Envio**:
   - Cada envio de mensagem é registrado no arquivo `logs.txt`, contendo:
     - **Data e Hora**: Quando a mensagem foi enviada.
     - **Número de Destino**: O número do WhatsApp para o qual a mensagem foi enviada.
     - **Conteúdo da Mensagem**: O texto da mensagem.
     - **Status**: Se a mensagem foi enviada com sucesso ou se ocorreu algum erro.

4. **Gestão de Erros**:
   - Caso o envio falhe, o status de erro será registrado no log, incluindo detalhes do erro.

---

## Como Usar

### Passo 1: Clone o Repositório

Clone este repositório para sua máquina local utilizando o comando abaixo:

```bash
git clone https://github.com/seu-usuario/whatsapp-message-automation.git
cd whatsapp-message-automation
