# code to generate log file
# log entries we can create in test case itself
# log file creation and format of log file  will be created in utitlity file
import logging
class LogGen:
    @staticmethod    # to call class without creating object
    def loggen():    # where we need to exactly generate log file
        logging.basicConfig(filename=".//Logs//automation.log",format='%(asc)s:%(name)s:%(message)s',
                            datefmt='%m/%d/%y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


