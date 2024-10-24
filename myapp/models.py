from django.db import models

# Create your models here.

# class user(models.Model):
#     user_id=models.IntegerField(primary_key=True)
#     user_name=models.CharField(max_length=100)
#     user_age=models.IntegerField()
#     date=models.DateField(null=True)    

# class book(models.Model):
#     book_id=models.IntegerField(primary_key=True)
#     book_name=models.CharField(max_length=200)
#     author=models.CharField(max_length=100)

# class employee(models.Model):
#     emp_id=models.IntegerField(primary_key=True)  
#     emp_name=models.CharField(max_length=100)
#     emp_age=models.IntegerField()

# class product(models.Model):
#     product_name=models.CharField(max_length=200)
#     product_description=models.TextField()
#     product_price=models.DecimalField(max_digits=100,decimal_places=2)
#     product_stock_quantity=models.IntegerField()  
#     product_created_at=models.DateTimeField(auto_now_add=True)  

# class customer1model(models.Model):
#     first_name=models.CharField(max_length=500)
#     last_name=models.CharField(max_length=500)
#     email=models.EmailField(unique=True)
#     phone_number=models.CharField(max_length=15)
#     address=models.TextField()
#     date_of_birth=models.DateField()   

# class userproduct(models.Model):
#     user_id=models.IntegerField(primary_key=True)
#     user_name=models.CharField(max_length=200)
#     user_age=models.IntegerField()
#     def __str__(self):
#         return self.user_name
# class productuser(models.Model):
#     p_id=models.IntegerField(primary_key=True)
#     p_name=models.CharField(max_length=100)
#     user_p=models.ForeignKey(userproduct,on_delete=models.CASCADE)  

# class publishermodel(models.Model):
#     pb_name=models.CharField(max_length=500)
#     pb_address=models.CharField(max_length=500)
#     pb_email=models.EmailField(unique=True)
#     def __str__(self):
#         return self.pb_name
# class bookpbmodel(models.Model):
#     bpb_title=models.CharField(max_length=500)
#     bpb_publication_date=models.DateField()
#     bpb_isbn=models.CharField(max_length=13,unique=True)
#     bpb_publisher=models.ForeignKey(publishermodel,on_delete=models.CASCADE)
#     def __str__(self):
#         return self.bpb_title


class Cours(models.Model):
    course_name=models.CharField(max_length=100)
    course_code=models.CharField(max_length=100,unique=True)
    date=models.DateField()  
    def __str__(self):
        return self.course_name 

class Student(models.Model):   
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)  
    phone_number=models.CharField(max_length=15)
    courses=models.ForeignKey(Cours,on_delete=models.CASCADE)

class Organizer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    contact_email=models.EmailField(unique=True)
    phone_nimber=models.CharField(max_length=15)
class Event(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    date=models.DateTimeField()
    location=models.CharField(max_length=225)





    

    
    