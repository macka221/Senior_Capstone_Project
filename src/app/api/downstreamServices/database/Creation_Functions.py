# create institution table
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKeyConstraint, Float, ForeignKey, Boolean

user = 'root'
password = 'password'
host = 'localhost'
port = 3306
database = 'CapstoneProject'


def get_connection():
    return create_engine(url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}"
                         .format(user, password, host, port, database), echo=True)

def create_institution(institution_id, institution_name, number_of_campuses, provider_id):
    # database connection

    engine = get_connection()

    meta = MetaData()

    institutions = Table(
        'institutions', meta,
        Column('institutionID', String, primary_key=True),
        Column('institution_name', String),
        Column('number_of_campuses', Integer),
        Column('providerID', Integer),
    )
    meta.create_all(engine)

    ins = institutions.insert().values(institutionID=institution_id,
                                       institution_name=institution_name,
                                       number_of_campuses=number_of_campuses,
                                       providerID=provider_id)
    conn = engine.connect()
    result = conn.execute(ins)

    return result

def create_campus(institution_name, institution_id, campus_id, provider_id, long, lat):
    # database connection

    engine = get_connection()

    meta = MetaData()

    camps_of_inst = Table(
        institution_name+' Campuses', meta,
        Column('institutionID', String(45)),
        Column('campusID', String(45), primary_key=True),
        Column('provider_id', String(45)),
        Column('long', Integer),
        Column('lat', Integer),
    )
    meta.create_all(engine)

    ins = camps_of_inst.insert().values(institutionID=institution_id,
                                        campusID=campus_id,
                                        provider_id=provider_id,
                                        long=long,
                                        lat=lat)
    conn = engine.connect()
    result = conn.execute(ins)

    return result

def create_building(institution_name, campus_id, building_id, building_name, building_address, cost_per_day, cost_per_week, cost_per_month):
    engine = get_connection()

    meta = MetaData()

    buildings_of_inst = Table(
        institution_name+' Buildings', meta,
        Column('campusID', String(45)),
        Column('buildingID', Integer, primary_key=True),
        Column('building_name', String(45)),
        Column('building_address', String(45)),
        Column('cost_per_day', Float),
        Column('cost_per_week', Float),
        Column('cost_per_month', Float)
    )
    meta.create_all(engine)

    ins = buildings_of_inst.insert().values(campusID=campus_id,
                                    buildingID=building_id,
                                    building_name=building_name,
                                    building_address=building_address,
                                    cost_per_day=cost_per_day,
                                    cost_per_week=cost_per_week,
                                    cost_per_month=cost_per_month)
    conn = engine.connect()
    result = conn.execute(ins)

    return result

def create_room(campus_id, building_id, room_num, room_id, length, width, height, volume):
    engine = get_connection()

    meta = MetaData()

    rooms_in_camp_building = Table(
        'Rooms on Campus '+campus_id, meta,
        Column('buildingID', String(45)),
        Column('room_num', String(45)),
        Column('roomID', String(45)),
        Column('length', Float),
        Column('width', Float),
        Column('height', Float),
        Column('volume', Float)

    )
    meta.create_all(engine)

    ins = rooms_in_camp_building.insert().values(buildingID=building_id,
                                    room_num=room_num,
                                    roomID=room_id,
                                    length=length,
                                    width=width,
                                    height=height,
                                    volume=volume)
    conn = engine.connect()
    result = conn.execute(ins)

    return result

def create_user(user_id, institution_id, first_name, last_name, email, isAdmin, isSuper, admin_pin):
    engine = get_connection()

    meta = MetaData()

    users = Table(
        'users', meta,
        Column('userID', String(45), primary_key=True),
        Column('institutionID', String(45)),
        Column('first_name', String(45)),
        Column('last_name', String(45)),
        Column('email', String(45)),
        Column('isAdmin', Boolean),
        Column('isSuper', Boolean),
        Column('admin_pin', Integer)

    )
    meta.create_all(engine)

    ins = users.insert().values(userID=user_id,
                                institutionID=institution_id,
                                first_name=first_name,
                                last_name=last_name,
                                email=email,
                                isAdmin=isAdmin,
                                isSuper=isSuper,
                                admin_pin=admin_pin)
    conn = engine.connect()
    result = conn.execute(ins)

    return result
