import pytest
import logging

class BaseClass:

    def getLogger(self):

        # create an object out of logging class that will be used for logs

        logger = logging.getLogger(__name__) # __name__ arg will catch the file name and print in log file
                
        #In cases where we have inherited this class and failed is there in the child class
        # then the file name in the log should belong to the child class
        # Below is how
        # loggerName = inspect.stack()[1][3] # Not working in my PC
        # logger = logging.getLogger(loggerName) # child class will be printed in logs
        
            # Let's collect the info on the file name
        fileHandler = logging.FileHandler('logfile1.log') # file object assigned to 'file'

        # Format of logging
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        fileHandler.setFormatter(formatter) # find handler provided info on the log format

        logger.addHandler(fileHandler) # file info sent to logger

        logger.setLevel(logging.INFO) # setting level means only the logs from info to critical will be logged not the debug lines
        
        return logger # return the logger object to be used by other programs