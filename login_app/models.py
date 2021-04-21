from django.db import models
import re


class UserManager(models.Manager):
    def validator(self,post_data):
        errors = {}
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if len(post_data["first_name"]) < 2:
            errors["first_name"]="First name must be at least two characters long"
        if len(post_data["last_name"]) < 2:
            errors["last_name"]="Last name must be at least two characters long"
            
        if not EMAIL_REGEX.match(post_data['email']):              
            errors['email'] = "Invalid email address!"
            
        # try:
        #     User.objects.get(first_name=post_data["first_name"])
        #     errors["first_name"]="First name already in use"
        # except:
        #     pass
        try:
            User.objects.get(email=post_data["email"])
            errors["email"]="email already in use!!"
        except:
            pass
        
            
        # email_check= User.objects.filter(email=post_data["email"])
        # if email_check:
        #     errors["email"]:"email already in use!!"
        # return errors
            
            
        if len(post_data["password"]) < 8:
            errors["password"]="Password must at least 8 characters"
            
        if len(post_data["password"])!=len(post_data["confirm_password"]):
            errors["password_march"]="Password must must march"
        return errors
        
        # try:
        #     User.objects.get(possword=post_data["password"])
        #     errors["password"]="Password already in use!!"
        # except:
        #     pass
        

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
    
