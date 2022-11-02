
from Creation_Functions import *

get_connection()

# create_institution("MO", "Morehouse_College", "GP")

create_campus("Morehouse_College", "MO", "MO-MA", "GP", 45.77, 63.44)

create_building("Morehouse_College", "MO-MA", "MO-MA-DANS", "Dansby", "830 Westview Dr", 12.11, 98.09, 400.37)

create_room("MO-MA", "MO-MA-DANS", "206", 10, 12, 10, 1200)

create_user("MO748be", "MO", "Justin", "Wynn", "justinwynn719@gmail.com", False, True, 1234)