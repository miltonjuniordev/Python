from plyer import notification
from datetime import datetime

def alerta (nivel, base, local):
    dataAtual = str(datetime.now())

    if nivel == 1: notification.notify(
        title = f'ALERT: A base {base} está offline.',
        message = f'Urgente verificar o servidor {local}, a base {base} está offline. \n {dataAtual}',
        app_name = 'notification',
        timeout = 10
    )
    elif nivel == 2: notification.notify(
        title = f'ALERT: A base {base} está offline.',
        message = f'Urgente verificar o servidor {local}, a base {base} está offline. \n {dataAtual}',
        app_name = 'notification',
        timeout = 10
    )
    elif nivel == 3: notification.notify(
        title = f'ALERT: A base {base} está offline.',
        message = f'Urgente verificar o servidor {local}, a base {base} está offline. \n {dataAtual}',
        app_name = 'notification',
        timeout = 10
    )

alerta(nivel = 3, base = 'USUÁRIO', local = './LOCALHOST')