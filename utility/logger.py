import logging
import os

class loggen:
    @staticmethod       # used to excute without object and can modify everytime we execute it
    def log_txt():
        path=(os.path.abspath(os.curdir)+'r\\framework\\logs\\automation.log')
        #path= r"C:\Users\hp\PycharmProjects_SDET_24\SDETPythonProject\framework\logs\automation.txt"
        logging.basicConfig(filename=path, format='%(asctime)s: %(levelname)s: %(message)s')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
