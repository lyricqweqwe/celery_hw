import time

from celery import shared_task
from django.core.mail import send_mail

from celery_hw import settings


@shared_task
def send_mailqq():
    send_mail(subject='标题',
              message='内容',
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=['1079084384@qq.com'],
              fail_silently=True
              )
    print(1)