# Logs are of 4 kinds # Info # Warning # Error # Critical
import logging

def test_loggingDemo():

# create an object out of logging class that will be used for logs

    logger = logging.getLogger(__name__) # __name__ arg will catch the file name and print in log file

    # Let's collect the info on the file name
    fileHandler = logging.FileHandler('logfile1.log') # file object assigned to 'file'

    # Format of logging
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

    fileHandler.setFormatter(formatter) # find handler provided info on the log format

    logger.addHandler(fileHandler) # file info sent to logger

    logger.setLevel(logging.INFO) # setting level means only the logs from info to critical will be logged not the debug lines

    logger.debug("debug has started")
    logger.info("This is an info log")
    logger.warning("Warning occurred")
    logger.error("There is an error here")
    logger.critical("Critical error please check!!")