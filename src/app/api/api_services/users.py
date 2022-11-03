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
import uuid

class credentials:
    def __init__(self, email:str, password:str):
        self.email = email
        self.password = password

class user:
    def __init__(self, name:tuple, login:credentials, institution_id,  verification_type):
        self.first_name = name[0]
        self.last_name = name[1]
        self.email = login.email
        self.__password = login.password
        self.institution = institution_id
        self.validated = False
        self.permissions = ['read_permissions']
        self.verification_type = verification_type
        self.userId = None

    def setUserId(self):
        self.userId = self.institution + f'-U-{str(uuid.uuid4())[:6]}'
    
    def getname(self):
        return self.first_name + ' ' + self.last_name

    def getEmail(self):
        return self.email

    def setValidated(self):
        self.validated = not self.validated

    def getValidated(self):
        return self.validated

    def getPermissions(self):
        return self.permissions

    def setVerificationType(self, verification_type):
        self.verification_type = verification_type

    def getVerificationType(self):
        return self.verification_type



class admin(user):
    def __init__(self, pin):
        self.__pin = pin
        self.permissions.append('write_permissions')
        self.permissions.append('elevate_permissions(admin)')

    def getEmail(self):
        return self.email

    def setPin(self, pin):
        self.__pin = pin


class superuser(user):
    def __init__(self, pin):
        self.__pin = pin
        self.permissions.append('write_permissions(super)')
        self.permissions.append('elevate_permissions(super)')

    def getemail(self):
        return self.email

    def setPin(self, pin):
        self.__pin = pin


users = admins = superUsers = []


