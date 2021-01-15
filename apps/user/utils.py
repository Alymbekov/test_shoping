from django.core.mail import send_mail


def send_activation_mail(email, activation_code):
    print(activation_code)
    subject = 'Активация Аккаунта'
    message = f"""Здравствуйте Уважаемый Пользователь.\n
     Спасибо за регистрацию на нашем сайте.\n
     Для активации Вашего аккаунта пожалуйста перейдите по ссылке: 
     http://127.0.0.1:8000/api/v1/accounts/activate/{activation_code}/
     """

    from_ = 'test@gmail.com'
    emails = [email, ]

    send_mail(subject, message, from_, emails)