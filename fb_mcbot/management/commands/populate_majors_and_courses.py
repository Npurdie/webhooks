from django.core.management.base import BaseCommand
from fb_mcbot.models import Major, Course

class Command(BaseCommand):
    def handle(self, *args, **options):
        for s in Major.MAJORS:
            major = Major(s[0], Major.FACULTIES[0][0])
            major.save()

        for c in Course.COURSES:
            course = Course(c[0])
            course.save()
