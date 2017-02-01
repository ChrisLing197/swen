from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from .models import *
from django.core.urlresolvers import reverse
import datetime

# Create your tests here.

class ExceptionTest(TestCase):
    #these are the relevant tests that we need to check

    def test_appointmentCreatedInFuture(self):  
        admin=User.objects.create_superuser('admin','1800notAreal@email.com','p@ssWord')
        c=Client()
        loggedin=c.login(username=admin.username,password='p@ssWord')
        #create an appointment in the future
        reg2=Appointment(admin,date_scheduled=datetime.datetime.now()+datetime.timedelta(days=1))
        timediff=datetime.datetime.now().day-reg2.date_scheduled.day
        self.assertIs(timediff<0,True)

    def test_Record(self):
        admin=User.objects.create_superuser('admin','1800notAreal@email.com','p@ssWord')
        c=Client()
        loggedin=c.login(username=admin.username,password='p@ssWord')
        #testing record
        reg2=Record(admin, record_type='HR',doctors_note='Every time im running Im feeling like I gotta get away, get away,get away Better know that I wont and I wont ever stop Cause you know that I gotta win everyday,day')
        self.assertEquals(reg2.doctors_note,'Every time im running Im feeling like I gotta get away, get away,get away Better know that I wont and I wont ever stop Cause you know that I gotta win everyday,day')

    def test_Activity(self):  
        admin=User.objects.create_superuser('admin','1800notAreal@email.com','p@ssWord')
        c=Client()
        loggedin=c.login(username=admin.username,password='p@ssWord')
        #testing description
        reg2=Activity(admin, activity_type='RG',description='Ladies and gentlemen, this is Chris and Im your chief flight attendant. On behalf of Captain Chris and the entire crew, welcome aboard SWEN Airlines flight f261-14d, non-stop service from R1 to an A. Our flight time will be 12 minutes.')
        self.assertEquals(reg2.description,'Ladies and gentlemen, this is Chris and Im your chief flight attendant. On behalf of Captain Chris and the entire crew, welcome aboard SWEN Airlines flight f261-14d, non-stop service from R1 to an A. Our flight time will be 12 minutes.')

    def test_ActivityRedirect(self):
        c=Client()
        response=c.get(reverse('system:dashboard'),follow=True)
        admin=User.objects.create_superuser('admin','1800notAreal@email.com','p@ssWord')
        login=c.login(username=admin.username,password='p@ssWord')
        lastUrl,status=response.redirect_chain[-1]
        self.assertRedirects(response,lastUrl,status_code=302,target_status_code=200,host=None,msg_prefix='',fetch_redirect_response=True)

    def test_InvalidLogin(self):
        c=Client()
        response=c.get(reverse('system:dashboard'),follow=True)
        admin=User.objects.create_superuser('admin','1800notAreal@gmail.com','p@ssWord')
        login=c.login(username=admin.username,password='incorrect')
        lastUrl,status=response.redirect_chain[-1]
        #status=302
        self.assertRedirects(response,lastUrl,status_code=302,target_status_code=200,host=None,msg_prefix='',fetch_redirect_response=True)

    def test_message(self):  
        admin=User.objects.create_superuser('admin','1800notAreal@email.com','p@ssWord')
        reciever=User.objects.create_user('reciever','1800notAreal@gmail.com','pass@word@2')
        c=Client()
        loggedin=c.login(username=admin.username,password='p@ssWord')
        #create an appointment in the future
        reg2=Message(admin,reciever,text='The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.')

        self.assertEquals(reg2.text,'The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.')


