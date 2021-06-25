from mongoengine import Document
class MongoService:
    """
    This class provides various MongoDb releated services. Its lot more easier to seperate the DB Operations
    into a seperate service than directly writing DB related code in each service.
    """

    @staticmethod
    def save_to_db(mongo_obj:Document):
        """
        This function receives a MongoEngine document object and save it in the database.
        :param mongo_obj:
        :return:
        """
        try:
            db_result = mongo_obj.save()
            return True,db_result.id
        except Exception as e:
            False,str(e)

