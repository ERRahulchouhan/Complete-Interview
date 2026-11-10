from django.contrib.auth.signals import  user_logged_out, user_logged_in,user_login_failed

from django.contrib.auth.models import User

Methods : 1

def login_success(sender, request, user, **kwargs):
    print("----------------------------")
    print("Logged in signal Run Intro")
    print("sender" , sender)
    print("Request" , request)
    print("User" , user)
    print("user password" , user.password)
    

user_logged_in.connect(login_success, sender=User)




Methods : 2
from django.dispatch import receiver
@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("----------------------------")
    print("Logged in signal Run Intro")
    print("sender" , sender)
    print("Request" , request)
    print("User" , user)
    print("user password" , user.password)
    
    
# Models signal
from django.db.models.signals import (pre_init,pre_save,pre_delete,
    post_init,post_save,post_delete  )

