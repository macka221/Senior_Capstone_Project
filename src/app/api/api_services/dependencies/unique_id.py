import uuid

class unique_id:
    def __init__(self, org_name:str):
        """
        Used to generate unique IDs for each class.
        :param org_name: name of the institutions
        :param special_tag: special tag based on the association
        """
        org_tag = org_name[:3]
        self.unique_id = f"O-{org_tag}-{str(uuid.uuid4())[:6]}"

    def __str__(self):
        return self.unique_id

class provider_id:
    def __init__(self, prov_name:str, state_code:str):
        """
        Creates a provider unique code using the state information and the 
        providers name.
        :param prov_name: name of a provider
        :param state_code: the state that the provider operates
        """
        self.prov_id = f"pr-{prov_name[:3]}-ST{state_code}"
    
    def __str__(self):
        return self.prov_id
        


