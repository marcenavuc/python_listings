import logging
import sys

# # logging.basicConfig(level=logging.INFO, handlers=[
# #     logging.FileHandler("logs.txt")
# # ], format=logging.Formatter("%(asctime) - %(name) - %(levelsname) - %(message)"))
# logging.basicConfig(level=logging.INFO, handlers=[
#     logging.FileHandler("logs.txt")
# ], format="%(asctime) - %(name) - %(levelsname) - %(message)")
# # handler = logging.FileHandler("logs.txt")
# # formater = logging.Formatter("%(asctime) - %(name) - %(levelsname) - %(message)")
# # handler.setFormatter(formater)
# logger = logging.getLogger(__name__)

# logger.debug("Its debug")
# logger.info("Application canceled")
# logger.critical("Critical error")
# logger.error("Eroor")
logging.basicConfig(level=logging.INFO, 
    format="%(asctime) %(message)")
logger = logging.getLogger(__name__)
logger.debug("It's log")