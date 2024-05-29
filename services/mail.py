from django.core.mail import send_mail


class Mail:
    def __init__(self):
        self.__from_mail = 'noreply.rededobem@gmail.com'

    def send(self, data):
        schedule = data['schedule']
        therapist = data['therapist']
        therapist_whatsapp = data['therapist_whatsapp']
        therapist_email = data['therapist_email']
        patient = data['patient']
        patient_email = data['patient_email']
        send_mail(
            subject='Você tem uma nova consulta marcada!',
            message=f'Você agendou uma consulta com {therapist}: {schedule}. Agora você pode entrar em contato pelo whatsapp: {therapist_whatsapp} e combinar como vocês conversarão. Lembre-se de mandar uma mensagem com antecedência, se possível, se apresentando.',
            from_email=self.__from_mail,
            recipient_list=[patient_email]
        )
        send_mail(
            'Você tem uma nova consulta marcada!',
            f'{patient} agendou uma consulta com você: data.{schedule}. Aguarde o contato do paciente para combinar como vocês conversarão. Caso o paciente não entre em contato, o atendimento não ocorra ou por qualquer motivo o atendimento se encerre, não se esqueça de reabrir o horário para outros pacientes na plataforme Rede do Bem.',
            from_email=self.__from_mail,
            recipient_list=[therapist_email]
        )
