import  os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE','celery_hw.settings')
# 实例化
app = Celery('celery_hw',broker='redis://127.0.0.1:6379/2')

# 加载celery配置文件
app.config_from_object('django.conf.settings',namespace='CELERY')

# 自动注册app中tasks文件
app.autodiscover_tasks()


CELERYD_MAX_TASKS_PER_CHILD = 40

# 开启debug
@app.task(bind=True)
def debug_task(self):
    print(111)
