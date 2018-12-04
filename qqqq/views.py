from django.http import HttpResponse


from .tasks import send_mailqq


def index(request):
    send_mailqq()
    return HttpResponse('发送成功')