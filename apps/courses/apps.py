from django.apps import AppConfig
from watson import search as watson


class CoursesConfig(AppConfig):
    name = 'courses'

    def ready(self):
        course = self.get_model("Course")
        watson.register(course)
