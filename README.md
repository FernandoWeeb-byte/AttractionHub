# AttractionHub

### API USER
* Register `http://127.0.0.1:8000/api/register/`
    -  POST:
    ```js
    {
      "name": "Giulia Maia",
      "email": "gmaia@gmail.com",
      "username": "gmaia",
      "password": "12345abc"
    }
    ```
    
* Login `http://127.0.0.1:8000/api/login/`
    -  POST:
    ```js
    {
      "email": "tyes@gmail.com",
      "password": "12345abc"
    }
    ```
    
* Logout `http://127.0.0.1:8000/api/logout/`
    - GET:
    `No Body`
    
* Logged (Check if user is logged in) `http://127.0.0.1:8000/api/user/`
    - GET:
    `No Body`
 
