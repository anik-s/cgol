# CGOL with OAuth2 and Docker



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




#### POST /grids/
##### Sample payload
```
{
"x": 4,
"y": 4,
"data": "[ [0, 1, 0, 0], [0, 1, 0, 1], [1, 0, 1, 0], [1, 1, 1, 0] ]"
}
```

#### PUT /grids/{id}/
##### Sample payload
```
{
"x": 4,
"y": 4,
"data": "[ [0, 1, 0, 0], [0, 1, 0, 1], [1, 0, 1, 0], [1, 1, 1, 0] ]"
}
```

#### GET /grids/
##### Sample response:
```
[
{
"id": 1,
"x": 4,
"y": 4,
"data": "[ [0, 1, 0, 0], [0, 1, 0, 1], [1, 0, 1, 0], [1, 1, 1, 0] ]"
},
{
"id": 2,
"x": 4,
"y": 4,
"data": "[ [0, 1, 0, 0], [0, 1, 0, 1], [1, 0, 1, 0], [1, 1, 1, 0] ]"
}
]
```

#### GET /grids/{id}/
##### Sample response
```
{
"id": 1,
"x": 4,
"y": 4,
"data": "[ [0, 1, 0, 0], [0, 1, 0, 1], [1, 0, 1, 0], [1, 1, 1, 0] ]"
}
```

#### GET /grids/{id}/?after=1,2
##### Sample Response
```
{
"id": 1,
"x": 4,
"y": 4,
"data":[
{
"grid":[[0, 0, 1, 0 ], [1, 1, 0, 0 ], [1, 0, 0,…],
"age": "1"
},
{
"grid":[[0, 1, 0, 0 ], [1, 1, 1, 0 ], [1, 0, 1,…],
"age": "2"
}
]
}
```
