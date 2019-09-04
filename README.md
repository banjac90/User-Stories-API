# User-Stories-API
User Stories API that contains a category, Article (book) and Custom User model with JWT authentication

1. Create 3.6.7 Python virtualenv

2. in your virtual env Install Django:
    pip install django
    
3. Install libraries:
   - pip install djangorestframework
   - pip install djangorestframework_simplejwt
   - pip install django-rest-swagger    
   - pip install pyyaml
   - pip install django-rest-passwordreset
    
4. Download zip file and extract it.

5. Copy User-Stories-API-master folder into your virtual env folder. 
   User-Stories-API-master will contain all migrations and database.

6. Run python manage.py runserver

7. Main page is swagger-ui for testing.

8. You can login in admin panel with test admin user email: "banjac90@gmail.com" and password:"!Danijel90"

9. Except Swagger documentation (first page), all other data renders in JSON. Postman or samiliary tool is required for other pages.
   Or you can insert 'rest_framework.renderers.BrowsableAPIRenderer' in 'DEFAULT_RENDERER_CLASSES' in settings.py.
   ```
   'DEFAULT_RENDERER_CLASSES':(
        'rest_framework.renderers.JSONRenderer', 
        'rest_framework.renderers.BrowsableAPIRenderer',        
    )
   ```

10. In Postmans body tag insert: 
    ```
    {"email":"banjac90@gmail.com", "password":"!Danijel90"}
    ```
    and send POST request on url: http://127.0.0.1:8000/api/token
    
11. You will gain JWT access and refresh token
    
12. To access other pages, you need to in Authorization tab select type:'Bearer Token' and insert generated access Token in Token label.
    
13. Access token lasts 30 minutes

14. You can now oprate with app

15. To register with new user you send POST request on http://127.0.0.1:8000/Users/Registration/
    You must provide email, password, first name and last name

