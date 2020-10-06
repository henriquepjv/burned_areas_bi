# BI with Brazilian burned areas
Flask Login and Registration System through SQLite.
Bussiness inteligence from PowerBI
### Git Clone 
``` git clone git@github.com:henriquepjv/burned_areas_bi.git```
### Change Directory
```cd flask-login```
### Note : Install Python and Postman for your system
```pip install virtualenv```

```source bin/activate```

```pip install flask flask-sqlalchemy flask-login```
### Export 
```export FLASK_APP=app.py```

```export FLASK_DEBUG=True```

``` flask run ``` 
### Create DB 
```python```

```from app import db```

``` db.create_all() ``` 
``` exit() ``` 
### Start Server
```flask run```
### Open Browser
http://localhost:5000


### Demo
<img width="1429" alt="form de cadastro" src="https://user-images.githubusercontent.com/22040894/95146807-423f6e80-0755-11eb-93b9-c05fad3afa9f.png">
<img width="1424" alt="form de login" src="https://user-images.githubusercontent.com/22040894/95146826-4c616d00-0755-11eb-8594-6d08ed26fbe0.png">
<img width="1427" alt="dashboard bi" src="https://user-images.githubusercontent.com/22040894/95146876-76b32a80-0755-11eb-9da4-d49c29bbea70.png">

