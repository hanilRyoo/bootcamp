from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = 'polls'

    # def ready(self):
    #     import polls.signals # 앱 시작 시 실행할 초기 설정