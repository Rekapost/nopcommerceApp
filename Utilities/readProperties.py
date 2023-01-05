import configparser  # package
config=configparser.RawConfigParser()    # object config =class RawConfigParser()
# this object , has some methods by which we can  read data from ini file
config.read(".//Configurations/config.ini")   # .// current project     read method

class ReadConfig: #class need not have ()
    @staticmethod
    def getApplicationURL(): # i want to access this method directly using class name,so remove (self)in method and make this method as stattic method without creating object
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password