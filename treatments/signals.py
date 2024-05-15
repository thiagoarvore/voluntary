from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Treatment
from calendars.models import Calendar


@receiver(post_save, sender=Treatment)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        schedule_id = instance.schedule_id
        calendar = Calendar.objects.get(pk=schedule_id)
        calendar.is_active = False
        calendar.save()
        schedule = instance.schedule
        therapist = instance.therapist
        patient = instance.patient
        from_mail = 'noreply.rededobem@gmail.com'
        send_mail(
            subject='Você tem uma nova consulta marcada!',
            message=f'Você agendou uma consulta com {therapist}: {schedule}. Agora você pode entrar em contato pelo whatsapp: {therapist.whatsapp} e combinar como vocês conversarão.',
            from_email=from_mail,
            recipient_list=[str(patient.user.email)]
        )
        send_mail(
            'Você tem uma nova consulta marcada!',
            f'{patient} agendou uma consulta com você: {schedule}. Aguarde o contato do paciente para combinar como vocês conversarão. Caso o paciente não entre em contato, o atendimento não ocorra ou por qualquer motivo o atendimento se encerre, não se esqueça de reabrir o horário para outros pacientes na plataforme Rede do Bem.',
            from_email=from_mail,
            recipient_list=[str(therapist.user.email)]
        )
