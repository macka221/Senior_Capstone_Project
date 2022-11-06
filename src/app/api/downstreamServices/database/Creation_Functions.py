# create institution table
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ARRAY, Float, ForeignKey, Boolean, ForeignKeyConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

user = 'root'
password = 'password'
host = 'localhost'
port = 3306
database = 'CapstoneProject'


def get_connection():
    return create_engine(url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}"
                         .format(user, password, host, port, database), echo=True)



def create_institution(institution_id, institution_name, provider_id):
    # database connection

    engine = get_connection()

    meta = MetaData()
    meta.bind = engine

    institutions = Table(
        'institutions', meta,
        Column('institutionID', String(45), primary_key=True),
        Column('institution_name', String(45)),
        Column('providerID', String(45))
    )
    meta.create_all(engine)

    ins = institutions.insert().values(institutionID=institution_id,
                                       institution_name=institution_name,
                                       providerID=provider_id)
    conn = engine.connect()
    result = conn.execute(ins)

    return result

def create_campus(institution_name, institution_id, campus_id, provider_id, long, lat):
    # database connection

    engine = get_connection()

    meta = MetaData()
    meta.bind = engine

    institutions = Table(
        'institutions', meta,
        Column('institutionID', String(45), primary_key=True),
        Column('institution_name', String(45)),
        Column('providerID', String(45))
    )
    camps_of_inst = Table(
        'campuses', meta,
        Column('institutionID', String(45)),
        Column('campusID', String(45), primary_key=True),
        Column('provider_id', String(45)),
        Column('long', Float),
        Column('lat', Float),
        ForeignKeyConstraint(
            ['institutionID'], ['institutions.institutionID'], name="fk_campus_institutionID"
        )
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

def create_building(institution_name, campus_id, building_id, building_name, building_address):
    engine = get_connection()

    meta = MetaData()
    meta.bind = engine

    institutions = Table(
        'institutions', meta,
        Column('institutionID', String(45), primary_key=True),
        Column('institution_name', String(45)),
        Column('providerID', String(45))
    )
    camps_of_inst = Table(
        'campuses', meta,
        Column('institutionID', String(45)),
        Column('campusID', String(45), primary_key=True),
        Column('provider_id', String(45)),
        Column('long', Float),
        Column('lat', Float),
        ForeignKeyConstraint(
            ['institutionID'], ['institutions.institutionID'], name="fk_campus_institutionID"
        )
    )
    buildings_of_inst = Table(
        'buildings', meta,
        Column('campusID', String(45)),
        Column('buildingID', String(45), primary_key=True),
        Column('building_name', String(45)),
        Column('building_address', String(45)),
        ForeignKeyConstraint(
            ['campusID'], ['campuses.campusID'], name="fk_building_campusID"
        )
    )
    meta.create_all(engine)

    ins = buildings_of_inst.insert().values(campusID=campus_id,
                                    buildingID=building_id,
                                    building_name=building_name,
                                    building_address=building_address)
    conn = engine.connect()
    result = conn.execute(ins)

    return result

def create_room(building_id, room_num, room_id, length, width, height, volume):
    engine = get_connection()

    meta = MetaData()
    meta.bind = engine

    institutions = Table(
        'institutions', meta,
        Column('institutionID', String(45), primary_key=True),
        Column('institution_name', String(45)),
        Column('providerID', String(45))
    )
    camps_of_inst = Table(
        'campuses', meta,
        Column('institutionID', String(45)),
        Column('campusID', String(45), primary_key=True),
        Column('provider_id', String(45)),
        Column('long', Float),
        Column('lat', Float),
        ForeignKeyConstraint(
            ['institutionID'], ['institutions.institutionID'], name="fk_campus_institutionID"
        )
    )
    buildings_of_inst = Table(
        'buildings', meta,
        Column('campusID', String(45)),
        Column('buildingID', String(45), primary_key=True),
        Column('building_name', String(45)),
        Column('building_address', String(45)),
        ForeignKeyConstraint(
            ['campusID'], ['campuses.campusID'], name="fk_building_campusID"
        )
    )
    rooms_in_camp_building = Table(
        'rooms', meta,
        Column('buildingID', String(45)),
        Column('room_num', String(45)),
        Column('roomID', String(45)),
        Column('length', Float),
        Column('width', Float),
        Column('height', Float),
        Column('volume', Integer),
        ForeignKeyConstraint(
            ['buildingID'], ['buildings.buildingID'], name="fk_rooms_buildingID"
        )
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
    meta.bind = engine

    institutions = Table(
        'institutions', meta,
        Column('institutionID', String(45), primary_key=True),
        Column('institution_name', String(45)),
        Column('providerID', String(45))
    )
    camps_of_inst = Table(
        'campuses', meta,
        Column('institutionID', String(45)),
        Column('campusID', String(45), primary_key=True),
        Column('provider_id', String(45)),
        Column('long', Float),
        Column('lat', Float),
        ForeignKeyConstraint(
            ['institutionID'], ['institutions.institutionID'], name="fk_campus_institutionID"
        )
    )
    buildings_of_inst = Table(
        'buildings', meta,
        Column('campusID', String(45)),
        Column('buildingID', String(45), primary_key=True),
        Column('building_name', String(45)),
        Column('building_address', String(45)),
        ForeignKeyConstraint(
            ['campusID'], ['campuses.campusID'], name="fk_building_campusID"
        )
    )
    rooms_in_camp_building = Table(
        'rooms', meta,
        Column('buildingID', String(45)),
        Column('room_num', String(45)),
        Column('roomID', String(45)),
        Column('length', Float),
        Column('width', Float),
        Column('height', Float),
        Column('volume', Integer),
        ForeignKeyConstraint(
            ['buildingID'], ['buildings.buildingID'], name="fk_rooms_buildingID"
        )
    )
    users = Table(
        'users', meta,
        Column('userID', String(45), primary_key=True),
        Column('institutionID', String(45), ),
        Column('first_name', String(45)),
        Column('last_name', String(45)),
        Column('email', String(45)),
        Column('isAdmin', Boolean),
        Column('isSuper', Boolean),
        Column('admin_pin', Integer),
        ForeignKeyConstraint(
            ['institutionID'], ['institutions.institutionID'], name="fk_users_institutionID"
        )

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
