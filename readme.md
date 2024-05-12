Create directory for media files:
1) Go to settings.py and add :
    - MEDIA_URL = "directory name"
    - MEDIA_ROOT = BASE_DIR/'directory name'
2) Go to urls.py and add :
    - from django.conf.urls.static import static
    - from django.conf import settings
    2.1)
    - urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


Add home page:
1) App directory
   - Create folder with name templates inside create folder with app name inside create html file
   - In views.py create class or function 
Project directory
   - In urls.py import views from app:  from app_name import views and add path in urlpatterns
2) OOP concept:
    - APP directory
      - in views.py create class
      - in urls.py create path 'views.MenuList.as_view()' - when we use class instead function use code like this where MenuList class name 


Open in web page our table from db:
1) App directory
   - In views.py import model from .models: from .models import model_name
   - In class or function add create object which add model with all properties : object_variable = model_name.objects.all()
     - If you do not want to show all information in one page, or you want to sort by date: model_name.objects.order_by('-date')[:5]
   - Add object to render converting it to dictionary format: {'object_name' : object_name}
2) If you want to add more information to template from views use get_context_data concept :  
   - def get_context_data(self):
         context = {'meals': 'Pizza'} - where concept accept dict which we show in template
         return context


Connect app urls with our main site:
1) Project directory:
   -  add app site path using include: path('', include('app name.urls'))
2) App directory:
   - create urls.py 
     - import path from project and views from app
     - add path in urlpatterns
   - in views.py create function or class
   - then create templates/app name/file_name.html


Django Model:
1) App directory:
   -  Create model in models.py 
   -  Make migrations
   -  In admin.py add import model and register it
    1.1) If you want to choice multiple value use 'choices'
     - meal_type = models.CharField(max_length=200,choices=MEAL_TYPE)
     - and create tuples like: MEAL_TYPE = (
                                              ('main_dishes(backend using name)', 'Main dishes(interface using name)')
                                              ('starters', 'Starters')    
                                            )
    1.2) If your model name is Post or Item anyone . django automatically create variable same name that model but in lowercase like post or item and you can use it in template like {{ item.name }}

Add static files:
1) App directory :
   - static directory
     - app_name directory
       - move from folder in pc to app_name directory 
   - in html file before img tags add {% load static %}
   - in html file add tag <img src="{% static 'app_name_dir/file_name' %}">


Create independent page which open by click , it can be article page, or any product in marketplace :
1) App directory where we can click to link :
   1.1) First stage of logic we can open object and our page is working, but we need to write number of object in url manually  
      - in urls.py add path where we can change url of page like this: <int:object_id>/ - it means that url accepts the number of object which we want to open bu click
      - in views.py define function, our function have to arguments request ande number of object (object_id), and last parameter of render we add dictionary {"id":object_id}
      - add html file 
   1.2) Second stage of logic show correct html page add after click if object is not find return error 404 page
      - in views.py , import get_objector_404 and earlier defining function before return add object_name = get_objector_404(Model/class_name, pk=object_id), pk - personal key 
        - in render change dictionary to {"object_name": object_name}
   1.3) Third stage of logic automatically following to correct link by click
      - in main html (file where we have all object maybe all article or all products) file wrap clickable object to a tag and in add url to href: href={% url 'app_name:name, which we use in path' object.id %}, we use real app name because if we have html file with same system do not understand which we want to open that s why using app name we can except this problem 
      - in urls.py add app_name = 'real app_name'


Create registration and login/out user page:
1) Project directory
   - in urls.py create path for Auth example: sighnup/
   - in urls.py create a path for the page to which the user will be redirected after registration example:current/
   - in urls.py create a path for logout 
   - in urls.py create a path for home 
   - in urls.py create a path for login 
2) App directory
   - in views.py define function or create class for your path
     - from django.contrib.auth.forms import UserCreationForm - a special form that makes it easy to create a new user in your application
       - render(request,'page_name.html', {'key_name': UserCreationForm()})
     - from django.contrib.auth.forms import AuthenticationForm - is used to allow a user to log in to their account in page
     - from django.shortcuts import redirect - for sending user to another page
     - from django.contrib.auth.models import User - for creating user
     - from django.db import IntegrityError - if user try to register same in DB which register by another user before
     - from django.contrib.auth import login - is a function that allows the user to log on to the site
       - after log on and log out redirect user to another page
     - from django.contrib.auth import logout - is a function that allows the user to log out to the site
       - after log on and log out redirect user to another page
     - from django.contrib.auth import authenticate - compare user input with data from DB
   - create template/app_name/base.html and extend all pages
     - add all construction which you want too in all site
       - user status, signup, login, logout buttons 
   - show in all pages that user is authenticated
     - user.is_authenticated - this concept check user is authenticated or not 
   - create signup page 
     - add form with POST method 
     - use jinja for call key_name : {{ key_name.as_p }}, (as_p word like <br>)
     - add button using type submit
     - add {% csrf_token %} inside form tag anywhere
   - create home page which redirected user after registration
   - create login page


Create custom form:
1) Project directory
    - in urls.py create path
2) App directory
   - create forms.py
     - from django.forms import ModelForm
     - from .models import model_name - on the basis of which the form will be created
     - create class with form name
       - create nested class Meta, add model = model_name, fields - which you want to use in form
   - in views.py define function or create class
     - from .forms import clas_name
       - if you have custom form tags in html page you can connect them with your function in views.py using their 'name' attribute example: 'name' = forms.cleaned_data['name']  
         - form = class_name(request.POST)
           action_name = form.save(commit=False)
           action_name.user = request.user - connect action to one user in DB
           action_name.save() - save in DB
           return redirect('page_adress') - redırect to new page


Show and update custom form:
1) Project directory
   - create path for view detail of todo
2) App directory
   - in views.py define function
     - from django.shortcuts import get_object_or_404 - find todo
     - write to conditions 
       - GET - if you only want to see form_object
       - POST - if you want to update form_object


Complete or delete object:
1) Project directory
   - create path but this path do not create new html file it is only redirect too all object list
2) App directory
   - Define function
     - Find object
     - If you want to complete use save()
     - If you want to delete use delete()
3) If you want to complete objects
   - create path
   - define function in app directory in views.py


Limitations for unregistered users:
1) Project directory
   - in settings.py create LOGIN_URL = 'add_path' 
2) App directory
   - from django.contrib.auth.decorators import login_required  - in views.py
   - @login_required - before views add this code


EMAIL SENDING WITH DJANGO:
1) Project directory
   - in settings.py configure for gmail
     - EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
     - EMAIL_HOST = 'smtp.gmail.com'
     - EMAIL_PORT = '587'
     - EMAIL_USE_TLS = True
     - EMAIL_HOST_USER = 'MAIL ACCOUNT'
     - EMAIL_HOST_PASSWORD = 'MAIL PASSWORD GENERATE WITH APP'
2) App directory
    - in views.py
      - from django.core.mail import EmailMessage
      - message_body = f'Add message body'
      - email_message = EmailMessage('Subject message', message_body, to=[email] - field in model)
      - email_message.send()


Customize admin panel object view:
1) App directory
   - create class and inherit from admin.ModelAdmin    
     - list_display = () - show columns
     - search_fields = () - search area
     - list_filter = () - filter in the right side
     - ordering = () - sorting
     - readonly_fields = ()


Django magic methods :
1) If you want automatically define 's' and the end of word in html (singularize and pluralize) use syntax : {{ dictionary_name_in_function.count|pluralize }}
2) If you want to change date format from html file using jinja : {{ variable_name.date|'format which you want' }}
3) If you want to truncate length of text which you want to show use: {{variable_name.description|truncatechars:chars_number }}
4) If you want to use html tags from admin panel when you write text use : {{ variable_name.description|safe }}
5) If you want to change name of model which we show in admin panel:
     - in models.py add self function and in return use which field you want to show  in admin panel
6) If you want to check which path is rendering from html page use : {% if request.path == '/your path/' %} output {% endif %}