# FastAPI template with JWT auth
For fast start and typical service and microservice. 
application layers
- First layer: **engines** - database interaction, *this template use async driver postgresql with single operations,
- Second layer: **repositories** - operation with database models, postfix DB, based on engines layer
- Third layer:  **services** - business level operation, bases on repositories layer
- Fourth layer: **routes** - based on service layer logic, use validations and dependence

other layers
- **models** - declarative database model
- **enums** - system enums
- **helpers** - checkers
- **utilities** - other


WARNING: for test, on start application create test user with credentials:
username: admin, password: admin,  user_uuid: 00000000-0000-4000-0000-000000000001

## DEPLOYMENT

### Docker container
1. create .env file from example
```shell
cp example.env .env
```
_!!! USE POSTGRES_URI for your operations system from example file_

full application environment and default   app/setting.py

#### docker 
create and running docker containers
```shell
docker compose up -d --build
```

### IDE running with poetry depends
1. install poetry 
```shell 
pip install poetry
```

2. configure poertry virtualenvs:
```shell
poetry config virtualenvs.in-project true
```

3. create poetry shell:
```shell
poetry shell
``` 

4. install dependence:
```shell
poetry install
```

5. run appilcation
```python
python app/main.py
```
