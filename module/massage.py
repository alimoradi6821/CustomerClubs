
class E(object):
    PERMISSION_DENIED = {"msg": "Permission denied;"}
    ALREADY_EXIST = {"msg": "Already exist;"}
    @classmethod
    def invalid(cls,m):
        return {"msg": f"You have entered an invalid {m}."}

    @classmethod
    def not_found(cls,m):
        return {"msg": f"The requested {m} object does not exist."}
class R(object):

    CREATED = {"msg": "Created."}