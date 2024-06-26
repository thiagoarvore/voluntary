from accounts.models import Profile
from services.mail import Mail
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        no_register = [person.user.email for person in Profile.objects.filter(crp__isnull=True, age__isnull=True)]
        no_training_users_emails = [person.user.email for person in Profile.objects.filter(trained=False, e_psi__isnull=False)]
        no_e_psi_user_emails = [person.user.email for person in Profile.objects.filter(trained=True, e_psi__isnull=True)]
        no_training_no_e_psi_users_emails = [person.user.email for person in Profile.objects.filter(trained=False, e_psi__isnull=True)]

        # no_register_msg = '''Olá, vimos que você tentou se cadastrar em nossa plataforma e não concluiu o processo. Encontrou alguma dificuldade. Precisa de ajuda?'''
        # no_training_msg = '''Vimos que você ainda não possui treinamento para atendimento em Emergências e Desastres.
        #                     Seguem os links para alguns treinamentos específicos, assim que completar algum, volte para concluir sua inscrição como terapeuta.
        #                     Ficaremos muito felizes por fazer parte de nosso time!'''
        # no_e_psi_msg = '''Vimos que você ainda não incluiu o link do seu e-Psi.
        #                     Caso tenha alguma dúvida sobre como proceder, segue um passo a passo.
        #                     Assim que terminar essa etapa, volte para concluir sua inscrição como terapeuta.
        #                     Ficaremos muito felizes por fazer parte de nosso time! '''

        e_mail_service = Mail()
        template = 'email_templates/no_register_mail.html'
        e_mail_service.send_help_mail_register_not_complete([user_mail for user_mail in no_register], template)
        e_mail_service.send_help_mail_register_not_complete(['thiagoarvore@gmail.com'], template)

        e_mail_service = Mail()
        template = 'email_templates/no_training_mail.html'
        e_mail_service.send_help_mail_register_not_complete([user_email for user_email in no_training_users_emails], template)
        e_mail_service.send_help_mail_register_not_complete(['thiagoarvore@gmail.com'], template)

        e_mail_service = Mail()
        template = 'email_templates/no_e_psi_mail.html'
        e_mail_service.send_help_mail_register_not_complete([user_email for user_email in no_e_psi_user_emails], template)
        e_mail_service.send_help_mail_register_not_complete(['thiagoarvore@gmail.com'], template)

        e_mail_service = Mail()
        template = 'email_templates/no_e_psi_training_mail.html'
        e_mail_service.send_help_mail_register_not_complete([user_email for user_email in no_training_no_e_psi_users_emails], template)
        e_mail_service.send_help_mail_register_not_complete(['thiagoarvore@gmail.com'], template)
