
def send_email(message, recipient, *, sender='university.help@gmail.com'):
    avail = ('.ru', '.com', '.net')
    verif = True
    if sender.endswith(avail) and recipient.endswith(avail) and '@' in sender and recipient:
        verif = True
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender != 'university.help@gmail.com' and sender.endswith(avail) and recipient.endswith(avail) and '@' in sender and recipient:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Забрали подарок на третью годовщину?', 'urban.teacher@gmail.com', sender='noreply.news@e-mail.hoyoverse.com')
send_email('Задание проверено. Python введение', 'urban.student@mail.pu', sender='urban.teacher@mail.ru')
send_email('Пожалуйста заберите ваши новые "AirPods"', 'urban.student@mail.ru', sender='urban.everybodywin@mail.net')
send_email('Это сообщение для проверки связи', 'leonid1976@gmail.com')