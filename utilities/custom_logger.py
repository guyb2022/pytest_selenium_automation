import logging
import os

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)


class LogGen:
    @staticmethod
    def loggen(file_name):
        # Ensure the logs directory exists
        if not os.path.exists("logs"):
            os.makedirs("logs")

        FORMAT = '%(asctime)s: %(levelname)s: %(message)s'
        DATEFMT = '%m/%d/%Y %I:%M:%S %p'
        logging.basicConfig(
                            format=FORMAT,
                            datefmt=DATEFMT,
                            handlers=[
                                        logging.FileHandler("logs/"+file_name+".log"),
                                        logging.StreamHandler()
                                    ]
                            )
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        return logger

        # # Another version
        # logger = logging.getLogger(__name__)
        # logger.setLevel(logging.DEBUG)
        # formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s:')
        # file_handler = logging.FileHandler("logs/"+file_name+".log")
        # file_handler.setFormatter(formatter)
        # file_handler.setLevel(logging.ERROR)
        # logger.addHandler(file_handler)
        # return logger
