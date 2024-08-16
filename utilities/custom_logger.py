import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)


class LogGen:
    @staticmethod
    def loggen():
        FORMAT = '%(asctime)s: %(levelname)s: %(message)s'
        DATEFMT = '%m/%d/%Y %I:%M:%S %p'
        logging.basicConfig(
                            format=FORMAT,
                            datefmt=DATEFMT,
                            handlers=[
                                        logging.FileHandler("logs/automation.log"),
                                        logging.StreamHandler()
                                    ]
                            )
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        return logger
