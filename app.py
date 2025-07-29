from logger.custom_logger import CustomLogger

# Initialize the logger
logger_instance = CustomLogger()
logger = logger_instance.get_logger(__file__)

# Use it
logger.info("This is an info log testing")
logger.error("This is an error log testing")
