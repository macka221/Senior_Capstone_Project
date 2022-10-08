# Adding the class structure for users to be saved to the data base. 
# This includes regular users, admins, and super users. Admins and supers 
# will use pins for verification to promote permissions
# 
# All USERS have a FIRST NAME, LAST NAME, USERNAME, PASSWORD and EMAIL
#
# Regular USERS and ADMINS will only belong to a MAXIMUM of ONE INSTITUTION
#   SUPER USERS have NO LIMIT on NUMBER of INSTITUTIONS
# 
# VALIDATED, READ PERMISSIONS and WRITE PERMISSIONS are BOOL values
# On initial registration, all USERS default to
#  READ PERMISSIONS = TRUE
#  WRITE PERMISSIONS = FALSE
#
#  Only SUPER USERS and ADMINS can be promoted to have
#   WRITE PERMISSIONS = TRUE
#
# VERIFICATION TYPE will hold an ENUMERATED value 
# "User", "Admin", or "Super User"
#
# All USERS will have VALIDATED be 
# TRUE while LOGGED IN and 
# FALSE while LOGGED OUT
#


class user:
    def __init__(self, first_name, last_name, username, email, password, institution, campuses, validated, read_permissions, write_permissions, verification_type):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.institution = institution
        self.campuses = campuses
        self.validated = validated
        self.read_permissions = read_permissions
        self.write_permissions = write_permissions
        self.verification_type = verification_type

    def setFirstName(self, first_name):
        self.first_name = first_name

    def getFirstName(self):
        return self.first_name

    def setLastName(self, last_name):
        self.last_name = last_name

    def getLastName(self):
        return self.last_name

    def setemail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password

    def setInstitution(self, institution):
        self.institution = institution

    def getInstitution(self):
        return self.institution

    def addCampus(self, campus):
        self.campuses.append(campus)

    def getCampus(self, i):
        return self.campus[i]

    def getCampuses(self):
        return self.campuses

    def setValidated(self, validated):
        self.campus = validated

    def getValidated(self):
        return self.validated

    def setReadPermissions(self, read_permissions):
        self.campus = read_permissions

    def getReadPermissions(self):
        return self.read_permissions

    def setWritePermissions(self, write_permissions):
        self.campus = write_permissions

    def getWritePermissions(self):
        return self.write_permissions

    def setVerificationType(self, verification_type):
        self.verification_type = verification_type

    def getVerificationType(self):
        return self.verification_type



class admin:
    def __init__(self, username, pin, institute, campuses):
        self.username = username
        self.pin = pin
        self.institute = institute
        self.campuses= campuses

    def setUsername(self, username):
        self.username = username

    def getUsername(self):
        return self.username

    def setPin(self, pin):
        self.pin = pin

    def getPin(self):
        return self.pin

    def setInstitute(self, institute):
        self.institute = institute

    def getInstitute(self):
        return self.institute

    def addCampus(self, campus):
        self.campuses.append(campus)

    def getCampus(self, i):
        return self.campus[i]

    def getCampuses(self):
        return self.campuses



class superuser:
    def __init__(self, username, pin, institutes, campuses):
        self.username = username
        self.pin = pin
        self.institutes = institutes
        self.campuses = campuses

    def setUsername(self, username):
        self.username = username

    def getUsername(self):
        return self.username

    def setPin(self, pin):
        self.pin = pin

    def getPin(self):
        return self.pin

    def addInstitute(self, institute):
        self.institutes.append(institute)

    def getInstitute(self, i):
        return self.institutes[i]

    def getInstitutes(self):
        return self.institutes

    def addCampus(self, campus):
        self.campuses.append(campus)

    def getCampus(self, i):
        return self.campus[i]

    def getCampuses(self):
        return self.campuses



