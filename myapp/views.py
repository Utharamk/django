from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
# def fun2(request):
#     return HttpResponse("hi")

# def my(request):
#     return HttpResponse("<h1>Hello</h1>")

# def fun3(request):
#     return render(request,"new.html",{"name":"sunil"})

# def fun4(request):
#     context={
#         'fruits':['apple','banana'],
#     }
#     return render(request,"fruits.html",context)

# def fun5(request):
#     items=[
#         {'name':'sana','age':'21','class':'10'},
#         {'name':'uthara','age':'26','class':'7'},
#         {'name':'malu','age':'10','class':'10'},
#     ]
#     return render(request,"items.html",{'item':items})

# def fun6(request):
#     product_list=[
#         {'name':'Laptop','price':'$9999','stock':'In stock'},
#         {'name':'Smartphone','price':'599.99','stock':'Out of stock'},
#         {'name':'Headphone','price':'149.99','stock':'In stock'},
#     ]
#     return render(request,"product_list.html",{'product':product_list})

# def fun7(request):
#     data=user.objects.all()
#     return render(request,"all.html",{'data1':data})

# def fun8(request):
#     return render(request,"form.html")

# def add_user(request):
#     if request.method =='POST':
#         id=request.POST.get('id')
#         name=request.POST.get('name')
#         age=request.POST.get('age')
#         date=request.POST.get('date')
#         user_obj=user()
#         user_obj.user_id=id
#         user_obj.user_name=name
#         user_obj.user_age=age
#         user_obj.date=date
#         user_obj.save()
#     return render(request,"form.html")

# def fun9(request):
#     if request.method == 'POST':
#         id=request.POST.get('id')
#         title=request.POST.get('title')
#         author=request.POST.get('author')
#         b=book()
#         b.book_id=id
#         b.book_name=title
#         b.author=author
#         b.save()
#     return render(request,'addbook.html')
# def fun10(request):
#     data=book.objects.all()
#     return render(request,'displaybook.html',{'display':data})

# def fun11(request):
#     if request.method == 'POST':
#         id=request.POST.get('id')
#         name=request.POST.get('name')
#         age=request.POST.get('age')
#         e=employee()
#         e.emp_id=id
#         e.emp_name=name
#         e.emp_age=age
#         e.save()
#         return redirect ('v')
#     return render(request,'addemployee.html')
# def fun12(request):
#     b=employee.objects.all()
#     return render(request,'displayemployee.html',{'display':b})

# def funp(request):
#     if request.method =="POST":
#         name=request.POST.get('name')
#         description=request.POST.get('description')
#         price=request.POST.get('price')
#         stock_quantity=request.POST.get('stock_quantity')
#         created_at=request.POST.get('created_at')
#         p=product()
#         p.product_name=name
#         p. product_description=description
#         p.product_price=price
#         p.product_stock_quantity=stock_quantity
#         p.product_created_at=created_at
#         p.save()
#         return redirect('a')
#     return render(request,'addproduct.html')
# def funp1(request):
#    p=product.objects.all()
#    return render(request,'displayproduct.html',{'display':p})
# def delete_emp(request,id):
#     emp=employee.objects.get(emp_id=id)
#     emp.delete()
#     return redirect('v')
# def update_emp(request,id):
#     emp=employee.objects.filter(emp_id=id)
#     if request.method =="POST":
#         id=request.POST.get('id')
#         name=request.POST.get('name')
#         age=request.POST.get('age')
#         e=employee()
#         e.emp_id=id
#         e.emp_name=name
#         e.emp_age=age
#         e.save()
#         return redirect('v')
#     return render(request,'update.html',{'emp1':emp})


# def createcust(request):
#     if request.method == "POST":
#         first_name=request.POST.get('first_name')
#         last_name=request.POST.get('last_name')
#         email=request.POST.get('email')
#         phone_number=request.POST.get('phone_number')
#         address=request.POST.get('address')
#         date_of_birth=request.POST.get('date_of_birth')
#         customer=customer1model()
#         customer.first_name=first_name
#         customer.last_name=last_name
#         customer.email=email
#         customer.phone_number=phone_number
#         customer.address=address
#         customer.date_of_birth=date_of_birth
#         customer.save()
#         return redirect('cust')
#     return render(request,"customer_model.html")
# def cust(request):
#     customers=customer1model.objects.all()
#     return render(request,"customermmodel_table.html",{'cust1':customers})
# def deletecust(request,pk):
#     cust=customer1model.objects.get(pk=pk)
#     cust.delete()
#     return redirect('cust')
# def updatecust(request,pk):
#     cust=customer1model.objects.get(pk=pk)
#     if request.method == "POST":
#         first_name=request.POST.get('first_name')
#         last_name=request.POST.get('last_name')
#         email=request.POST.get('email')
#         phone_number=request.POST.get('phone_number')
#         address=request.POST.get('address')
#         date_of_birth=request.POST.get('date_of_birth')
#         cust.first_name=first_name
#         cust.last_name=last_name
#         cust.email=email
#         cust.phone_number=phone_number
#         cust.address=address
#         cust.date_of_birth=date_of_birth
#         cust.save()
#         return redirect('cust')
#     return render(request,"cust_model_update.html",{'updatekey':cust})


# def bpbcreate(request):
#     pub=publishermodel.objects.all()
#     if request.method == "POST":
#         title=request.POST.get('title')
#         publication_date=request.POST.get('publication_date')
#         isbn=request.POST.get('isbn')
#         publish=bookpbmodel()
#         publish.bpb_title=title
#         publish.bpb_publication_date=publication_date
#         publish.bpb_isbn=isbn
#         publish.bpb_publisher=publishermodel.objects.get(id=request.POST.get('pubf'))
#         publish.save()  
#         return redirect('publ')
#     return render(request,"bookpb_form.html",{'pubb':pub})
# def bpbcreatef(request):
#     publishes=bookpbmodel.objects.all()
#     return render(request,"bppublisher_table.html",{'publishes1':publishes})
# def bpbcreatedlt(request,id):
#     publishes=bookpbmodel.objects.get(id=id)
#     publishes.delete()
#     return redirect('publ')
# def bpbcreateupdate(request,id):
#     pb=publishermodel.objects.all()
#     publishes=bookpbmodel.objects.get(id=id)
#     if request.method == "POST":
#         title=request.POST.get('title')
#         publication_date=request.POST.get('publication_date')
#         isbn=request.POST.get('isbn')
#         publishes.bpb_title=title
#         publishes.bpb_publication_date=publication_date
#         publishes.bpb_isbn=isbn
#         publishes.bpb_publisher=publishermodel.objects.get(id=request.POST.get('id'))
#         publishes.save() 
#         return redirect('publ')
#     return render(request,"bookpb_update.html",{'updatekey1':publishes,'upd':pb,})

def addStudent(request):
    data=Cours.objects.all()
    if request.method == 'POST':
        f_name=request.POST.get('fname')
        l_name=request.POST.get('lname')
        e_mail=request.POST.get('email')
        phone_no=request.POST.get('phone')
        obj=Student()
        obj.first_name=f_name
        obj.last_name=l_name
        obj.email=e_mail
        obj.phone_number=phone_no
        obj.courses=Cours.objects.get(id=request.POST.get('course'))
        obj.save()
        return redirect('displayStudents')
    return render(request,'add_student.html',{'data':data})
def displayStudents(request):
    display=Student.objects.all()
    return render(request,'display_students.html',{'disp':display})
def displaySpecificStudent(request,id):
    data=Student.objects.get(id=id)
    return render(request,'display_specific_student.html',{'specific':data})
def updateStudent(request,id):
    data=Student.objects.get(id=id)
    dataa=Cours.objects.all()
    if request.method == 'POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        data.first_name=fname
        data.last_name=lname
        data.email=email
        data.phone_number=phone
        data.course=Cours.objects.get(id=request.POST.get('course'))
        data.save()
        return redirect('displayStudents')
    return render(request,'update_student.html',{'data':data,'dataa':dataa})
def deleteStudent(request,id):
    dele=Student.objects.get(id=id)
    dele.delete()
    return redirect('displayStudents')


def add_organizer(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('phone')
        obj=Organizer()
        obj.name=name
        obj.email=email
        obj.phone_number=number
        obj.save()
        return redirect('display_organizer')
    return render(request,'em_add_organizer.html')
def add_event(request):
    org_names=Organizer.objects.all()
    if request.method == 'POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        location=request.POST.get('location')
        obj=Event()
        obj.title=title
        obj.date=date
        obj.location=location
        obj.organizer=Organizer.objects.get(id=request.POST.get('org'))
        obj.save()
        return redirect('display_event')
    return render(request,'em_add_event.html',{'org_list':org_names})
def display_organizer(request):
    org=Organizer.objects.all()
    return render(request,'em_display_organizer.html',{'org':org})
def display_event(request):
    eve=Event.objects.all()
    return render(request,'em_display_event.html',{'event':eve})
def update_organizer(request,id):
    obj=Organizer.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('phone')
        obj.name=name
        obj.email=email
        obj.phone_number=number
        obj.save()
        return redirect('display_organizer')
    return render(request,'em_update_organizer.html',{'obj':obj})
def update_event(request,id):
    orgg=Organizer.objects.all()
    obj=Event.objects.get(id=id)
    if request.method == 'POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        location=request.POST.get('location')
        obj.title=title
        obj.date=date
        obj.location=location
        obj.organizer=Organizer.objects.get(id=request.POST.get('org'))
        obj.save()
        return redirect('display_event')
    return render(request,'em_update_event.html',{'obj':obj,'organize':orgg})
def delete_organizer(request,id):
    dlt=Organizer.objects.get(id=id)
    dlt.delete()
    return redirect('display_organizer')
def delete_event(request,id):
    dlt=Event.objects.get(id=id)
    dlt.delete()
    return redirect('display_event')
