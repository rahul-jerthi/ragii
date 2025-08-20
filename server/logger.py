import logging

def set_logger(name="RAGbot"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    #console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    
    #formatter 
    formatter=logging.Formatter("[%(asctime)s] [%(levelname)s] -  %(message)s ")
    console_handler.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(console_handler)

    return logger

logger = set_logger()
