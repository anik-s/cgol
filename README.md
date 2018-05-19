# CGOL with Auth and Docker



##### Create a superuser
`python manage.py createsuperuser`

Client ID and Secret can be generated from the django admin panel (/admin) after logging in as superuser under application creation


##### Login 
```
Method: POST Link: /o/token/
parameters:
client_id: <client_id>
client_secret: <client_secret>
grant_type: password
username: <your-username>
password: <your-password>
```

##### Authentication

```
A header with below inforamtion should be added to authenticate a request
Authentication: Bearer <access_token>

* access_token is achieved after successful login
```

##### Docker commands

```
docker-compose run web python manage.py migrate
docker-compose build
docker-compose up
```