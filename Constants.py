class Constants:
    __BASE_URL = "https://www.biccamera.com/bc/main/"

    @property
    def BASE_URL(self):
        return self.__BASE_URL

    @BASE_URL.setter
    def BASE_URL(self, value):
        raise AttributeError("Cannot modify read-only attribute")