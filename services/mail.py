from django.core.mail import send_mail
from django.template.loader import render_to_string

class Mail:
    def __init__(self):
        self.__from_mail = 'cuidadopsiemrede@gmail.com'

    def send(self, data):
        therapist_email = data['therapist_email']
        patient_email = data['patient_email']
        
        send_mail(
            subject='Você tem uma nova consulta marcada!',
            message='',
            from_email=f'Cuidado Psi em Rede <{self.__from_mail}>',
            recipient_list=[patient_email],
            html_message=render_to_string('patient_email_template.html', data),
            fail_silently=False
        )
        send_mail(
            subject='Você tem uma nova consulta marcada!',
            message='',
            from_email=f'Cuidado Psi em Rede <{self.__from_mail}>',
            recipient_list=[therapist_email],
            html_message=render_to_string('therapist_email_template.html', data),
            fail_silently=False
        )
