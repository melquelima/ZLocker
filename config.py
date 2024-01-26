from datetime import timedelta

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
CORS_HEADERS = 'Content-Type'
SECRET_KEY = "asdjkgasd$#43"

#DRIVER = "ODBC+Driver+17+for+SQL+Server"

#USER,PWD,SERVER,DB = ('postgres','qwerty333','localhost','Rpa') 


#SQLALCHEMY_DATABASE_URI     = f"mssql+pyodbc://{SERVER}/{DB}?driver={DRIVER}&trusted_connection=yes"
#SQLALCHEMY_DATABASE_URI     =f"postgresql+psycopg2://{USER}:{PWD}@{SERVER}:5432/postgres"
SQLALCHEMY_DATABASE_URI     =f"sqlite:///data/db.sqlite"


JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)

