import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
# console = logging.StreamHandler()
# console.setLevel(logging.WARNING)
# console.setFormatter(formatter)
filehandler = logging.FileHandler('sample.log')
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)
# logger.addHandler(console)
logger.addHandler(filehandler)

class AddStudentUser(Exception):

    def __init__(self, msg):
        super().__init__()
        self.message = msg

    def __str__(self):
        return str(self.message)


class RemoveStudentUser(Exception):

    def __init__(self, msg):
        super().__init__()
        self.message = msg

    def __str__(self):
        return str(self.message)


