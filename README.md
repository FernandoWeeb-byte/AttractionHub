# AttractionHub

### API USER
* Register `http://127.0.0.1:8000/auth/register/`
    -  POST:
    ```js
    {
      "name": "Giulia Maia",
      "email": "gmaia@gmail.com",
      "username": "gmaia",
      "password": "12345abc"
    }
    ```
    
* Login `http://127.0.0.1:8000/auth/login/`
    -  POST:
    ```js
    {
      "email": "tyes@gmail.com",
      "password": "12345abc"
    }
    ```
    
* Logout `http://127.0.0.1:8000/auth/logout/`
    - GET:
    `No Body`
    
* Logged (Check if user is logged in) `http://127.0.0.1:8000/auth/user/`
    - GET:
    `No Body`
 
### API ATTRACTIONS_USER

* Add attraction to list `http://127.0.0.1:8000/list/attraction/`
    -  POST:
    ```js
    {
      "title": "My Next Life as a Villainess: All Routes Lead to Doom!",
      "desc": "Most people would prefer being the protagonist of a world full of adventure, ....",
      "rating": "PG-13 - Teens 13 or older",
      "genre": ['Comedy', 'Drama', 'Fantasy', 'Romance'],
      "attractionType": "TV",
      "urlImg" "https://cdn.myanimelist.net/images/anime/1483/107061.jpg"
    }
     ```
* Update attraction from list `http://127.0.0.1:8000/list/attraction/(id_attraction)/`
    -  PUT:
    ```js
    {
      "score": 10,
      "status": "Watching"
    }
    ```
* Delete attraction from list `http://127.0.0.1:8000/list/attraction/(id_attraction)/`
    -  DELETE:
    `
    No body
    `
