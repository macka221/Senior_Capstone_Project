from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ARRAY, Float, ForeignKey, Boolean, ForeignKeyConstraint
from sqlalchemy.orm import declarative_base, relationship

user = 'root'
password = 'password'
host = 'localhost'
port = 3306
database = 'CapstoneProject'


def get_connection():
    return create_engine(url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}"
                         .format(user, password, host, port, database), echo=True)


