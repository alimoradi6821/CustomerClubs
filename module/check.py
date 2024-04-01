import phonenumbers


class PhoneNumber(object):

    @classmethod
    def is_valid(cls, pn):
        try:
            phone_number = phonenumbers.parse(pn, "IR")

            if phonenumbers.is_valid_number_for_region(phone_number, "IR"):
                return True

            else:
                return False

        except:
            return False


class Parameters(object):

    @classmethod
    def is_required(cls, r, *args):
        data = {}
        for i in args:
            try:
                field = r.data[i]
                data[str(i)] = field
            except:
                data["err_msg"] = f"{str(i)} Parameter are required."
                return False, data

        return True, data

    @classmethod
    def non_required(cls, r, *args):
        data = {}
        for i in args:
            try:
                field = r.data[i]
                data[str(i)] = field
            except:
                data[str(i)] = None

        return data
