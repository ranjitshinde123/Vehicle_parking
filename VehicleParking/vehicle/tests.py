from django.test import TestCase

# Create your tests here.
import speech_recognition as sr


from datetime import datetime, timedelta

a=datetime.now().date()
b=a-timedelta(7)
print(b)