import logging.config
import logging
from common.public import Public



def get_log():
    with open(Public().get_object_path() + "/configs/log.conf") as con_log:
        logging.config.fileConfig(con_log)
        log = logging.getLogger()
        return log