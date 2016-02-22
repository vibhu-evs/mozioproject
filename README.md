Mozio App
===================================================================

1. Dev tools Installations
	* sudo apt-get install build-essential python-dev libevent-dev libxml2-dev libmysqlclient-dev python-setuptools python-pip libpq-dev libxslt1-dev

2. Install Mysql
    * sudo apt-get install mysql-server
    * mysql -u root -p
    * create database moziodb;
    * sudo service mysql start
    * sudo service mysql stop

3. Install Mongodb

    * sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
    * echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/  apt/sources.list.d/mongodb-org-3.2.list
    * sudo apt-get update
    * sudo apt-get install -y mongodb-org

   
4. Install Virtualenv
    * pip install virtualenv

5. Virtualenv Setup
    * virtualenv env
    * source bin/activate
    * deactivate

6. Install requirements
    * pip install -r requirements.txt 

7. create tables
   * python manage.py migrate

8. Start Django test server
   * python manage.py runserver 8000
   
9. Test django app
    * python manage.py test apps.apis.providerapi


    

### **Provider Api**


#### **POST**

    http://api_host/provider/

##### **Descrpition**

    Create Provider 
    Permission None
    Authentication None

*Request*

    #!shell
    curl -X POST -H "Content-Type: application/json" -H "Cache-Control: no-cache" -d '{
      "name": "test",
      "email": "test@test.com",
      "phone_no": "99657477",
      "language": "en",
      "currency": "USD"
    }' "http://127.0.0.1:8000/api/provider/"

####  **Response**

```
#!json
{
  "provider": {
    "id": 5,
    "name": "test",
    "email": "test@test.com",
    "phone_no": "99657477",
    "language": "en",
    "currency": "USD",
    "is_active": true,
    "created": "2016-02-22T17:13:14.464879Z"
  }
}
```


#### **Provider Detail**

        http://api_host/provider/<provider_id>/      
        Permission None
        Authentication None
         
#### **Get **

##### **Descrpition**
     Provider Detail of particular provider_id

*Request*
    
    #!shell
    curl -X GET -H "Content-Type: application/json" -H "Cache-Control: no-cache" -H "Postman-Token: c3701be6-3698-9034-548f-2e502671c019" "http://127.0.0.1:8000/api/provider/1"

*Response*

```
#!json
{
  "data": {
    "id": 1,
    "name": "test123",
    "email": "test123@test.com",
    "phone_no": "99657477",
    "language": "en",
    "currency": "USD",
    "is_active": true,
    "created": "2016-02-22T12:12:22.068009Z"
  }
}
```

#### **PUT**

    http://api_host/<provider_id>/
    Permission None
    Authentication None

##### **Descrpition**

    Update Provider Detail of particular **provider_id**

*Request*

    #!shell
    curl -X PUT -H "Content-Type: application/json" -H "Cache-Control: no-cache" -H "Postman-Token: b09fd373-faca-fe8f-62d0-529a6fc49828" -d '{    
      "name": "test123",
      "email": "test123@test.com",
      "phone_no": "99657477",
      "language": "en",
      "currency": "USD"
    }' "http://127.0.0.1:8000/api/provider/1"


#### **Response**

```
#!json
{
  "provider": {
    "id": 1,
    "name": "test123",
    "email": "test123@test.com",
    "phone_no": "99657477",
    "language": "en",
    "currency": "USD",
    "is_active": true,
    "created": "2016-02-22T12:12:22.068009Z"
  }
}
```


#### **DELETE**

    http://api_host/<provider_id>
    Permission None
    Authentication None

##### **Descrpition**

    Delete Provider

*Request*

    #!shell
    curl -X DELETE -H "Content-Type: application/json" -H "Cache-Control: no-cache" -H "Postman-Token: 5cadf2f9-a282-a514-ca7f-69fc58628344" "http://127.0.0.1:8000/api/provider/1"


#### **Response**

```
#!json

```


#### **POST**

    http://api_host/provider/<provider_id>/servicearea/

##### **Descrpition**

    Create Provider Service area
    Permission None
    Authentication None

*Request*

    #!shell
    curl -X POST -H "Content-Type: application/json" -H "Cache-Control: no-cache" -H "Postman-Token: 1f943250-24b0-3a45-6c27-f2ca7223bfd5" -d '{
    "polygon":[ [[12.84528,77.696],[12.82084,77.67368],[12.85427,77.66235],[12.84528,77.696]] ],
    "name":"electronic city, Bangalore",
    "price":100
    }
    ' "http://127.0.0.1:8000/api/provider/7/servicearea/"

####  **Response**

```
#!json
{
    "data": {
        "id": "56cb43583ffc1564dd501c71",
        "provider_id": "7",
        "polygon": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        12.84528,
                        77.696
                    ],
                    [
                        12.82084,
                        77.67368
                    ],
                    [
                        12.85427,
                        77.66235
                    ],
                    [
                        12.84528,
                        77.696
                    ]
                ]
            ]
        },
        "name": "electronic city, Bangalore",
        "price": "100",
        "is_active": true
    }
}
```


#### **Provider Service Area List**

        http://api_host/provider/<provider_id>/servicearea      
        Permission None
        Authentication None
         
#### **Get **

##### **Descrpition**
     Service area list of particular provider_id

*Request*
    
    #!shell
    curl -X GET -H "Content-Type: application/json" -H "Cache-Control: no-cache" -H "Postman-Token: af9ad46f-7201-4b44-85c7-14a0cff22edf" "http://127.0.0.1:8000/api/provider/7/servicearea/"


*Response*

```
#!json
{
    "results": [
        {
            "id": "56cb43583ffc1564dd501c71",
            "provider_id": "7",
            "polygon": {
                "type": "Polygon",
                "coordinates": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                12.84528,
                                77.696
                            ],
                            [
                                12.82084,
                                77.67368
                            ],
                            [
                                12.85427,
                                77.66235
                            ],
                            [
                                12.84528,
                                77.696
                            ]
                        ]
                    ]
                }
            },
            "name": "electronic city, Bangalore",
            "price": "100",
            "is_active": true
        },
        {
            "id": "56cb43a13ffc1564dd501c72",
            "provider_id": "7",
            "polygon": {
                "type": "Polygon",
                "coordinates": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                12.84528,
                                77.696
                            ],
                            [
                                12.82084,
                                77.67368
                            ],
                            [
                                12.85427,
                                77.66235
                            ],
                            [
                                12.84528,
                                77.696
                            ]
                        ]
                    ]
                }
            },
            "name": "Koramangala, Bangalore",
            "price": "100",
            "is_active": true
        }
    ]
}
```





#### **Service Area Detail**

        http://api_host/service/area/<area_id>   
        Permission None
        Authentication None
         
#### **Get **

##### **Descrpition**
     Service Area Detail of particular area_id

*Request*
    
    #!shell
    curl -X GET -H "Authorization: Token 101d44d5e1a7ffec5414f339bad1eef67ad43b29" -H "Content-Type: application/json" -H "Cache-Control: no-cache" -H "Postman-Token: 279bbff7-8b70-bef0-1713-5f168e9aa859" "http://127.0.0.1:8000/api/service/area/56cb43a13ffc1564dd501c72"


*Response*

```
#!json
{
    "id": "56cb43a13ffc1564dd501c72",
    "provider_id": "7",
    "polygon": {
        "type": "Polygon",
        "coordinates": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        12.84528,
                        77.696
                    ],
                    [
                        12.82084,
                        77.67368
                    ],
                    [
                        12.85427,
                        77.66235
                    ],
                    [
                        12.84528,
                        77.696
                    ]
                ]
            ]
        }
    },
    "name": "Koramangala, Bangalore",
    "price": "100",
    "is_active": true
}
```

#### **PUT**

        http://api_host/service/area/<area_id>     
        Permission None
        Authentication None

##### **Descrpition**

    Update Service Area Detail of particular area_id

*Request*

    #!shell
    curl -X PUT -H "Authorization: Token 101d44d5e1a7ffec5414f339bad1eef67ad43b29" -H "Content-Type: application/json" -H "Cache-Control: no-cache" -H "Postman-Token: cab4dd00-bc28-65fd-c875-b38781f1c9bb" -d '{
  
  "provider_id": "7",
  "polygon": [
        [
          [
            12.84528,
            77.696
          ],
          [
            12.82084,
            77.67368
          ],
          [
            12.85427,
            77.66235
          ],
          [
            12.84528,
            77.696
          ]
        ]
      ],
  "name":"test",
  "price":100
}' "http://127.0.0.1:8000/api/service/area/56cb43a13ffc1564dd501c72"


#### **Response**

```
#!json
{
    "id": "56cb43a13ffc1564dd501c72",
    "provider_id": "7",
    "polygon": {
        "type": "Polygon",
        "coordinates": [
            [
                [
                    12.84528,
                    77.696
                ],
                [
                    12.82084,
                    77.67368
                ],
                [
                    12.85427,
                    77.66235
                ],
                [
                    12.84528,
                    77.696
                ]
            ]
        ]
    },
    "name": "test",
    "price": "100",
    "is_active": true
}
```



#### **DELETE**

    http://api_host/service/area/<area_id>      
    Permission None
    Authentication None

##### **Descrpition**

    Delete Service Area

*Request*

    #!shell
    curl -X DELETE -H "Authorization: Token 101d44d5e1a7ffec5414f339bad1eef67ad43b29" -H "Content-Type: application/json" -H "Cache-Control: no-cache" -H "Postman-Token: af92e268-b1cb-624c-072d-872ff22bd5aa" -d '' "http://127.0.0.1:8000/api/service/area/56cb43a13ffc1564dd501c72"


#### **Response**

```
#!json

```


#### **Service Area Search**

        http://api_host/api/search?point=[lat,lng]
        Permission None
        Authentication None
         
#### **Get **

##### **Descrpition**
     Search Service area

*Request*
    
    #!shell
    curl -X GET -H "Cache-Control: no-cache" -H "Postman-Token: f928e013-7eb6-1639-655a-f7978e5a0ac9" "http://127.0.0.1:8000/api/search?point=[12.75689,77.82715]&point=[12.70934,77.41276]&point=[13.08847,77.31903]&point=[13.17458,77.81788]&point=[12.75689,77.82715]"


*Response*

```
#!json
{
    "results": {
        "polygon": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        12.75689,
                        77.82715
                    ],
                    [
                        12.70934,
                        77.41276
                    ],
                    [
                        13.08847,
                        77.31903
                    ],
                    [
                        13.17458,
                        77.81788
                    ],
                    [
                        12.75689,
                        77.82715
                    ]
                ]
            ]
        }
    }
}
```



