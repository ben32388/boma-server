import os
import time

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import default_token_generator
from django.db import models
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)


    def send_password_set_email(self):
        subject = loader.render_to_string('email/set-password-subject.txt')
        subject = ''.join(subject.splitlines())

        body = loader.render_to_string('email/set-password-content.html', {
            'uid': urlsafe_base64_encode(force_bytes(self.pk)),
            'token': default_token_generator.make_token(self),
            'user': self,
        })

        self.email_user(subject, body)

    def send_password_reset_email(self):
        subject = loader.render_to_string('email/reset-password-subject.txt')
        subject = ''.join(subject.splitlines())

        body = loader.render_to_string('email/reset-password-content.html', {
            'uid': urlsafe_base64_encode(force_bytes(self.pk)),
            'token': default_token_generator.make_token(self),
            'user': self,
        })

        self.email_user(subject, body)

