class Constants:
    query = "冷蔵庫"

    __BASE_URL = "https://www.biccamera.com/bc/category/"
    __encoded_query = query.encode("shift_jis")



    @property
    def BASE_URL(self):
        return self.__BASE_URL

    @BASE_URL.setter
    def BASE_URL(self, value):
        raise AttributeError("Cannot modify read-only attribute")

    @property
    def encoded_query(self):
        return self.__encoded_query

    @encoded_query.setter
    def encoded_query(self, value):
        raise AttributeError("Cannot modify read-only attribute")