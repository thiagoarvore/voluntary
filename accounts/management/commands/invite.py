from django.core.management.base import BaseCommand
import pandas as pd
from services.mail import Mail


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        df = pd.read_excel('cadastroRS.xlsx')
        email_list = df['E - mail'].dropna().str.lower().tolist()
        mail = Mail()
        mail.send_invitation_email(email_list=email_list)
