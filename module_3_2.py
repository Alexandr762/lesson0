def send_email(messege, recipient,sender = "university.help@gmail.com") :
    if '@' not in recipient or not (recipient.endswith('.com') or recipient.endswith('.ru')
                                                           or recipient.endswith('.net')) :
        print(f'Невозможно отправить письмо с адреса{sender} на адрес {recipient} .')
    elif recipient == sender :
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!')
    else:
        print(f'Отправляем письмо от {sender} на адрес {recipient} с сщщбщением : {messege}')

send_email('Hello', 'university.help@gmail.com')
