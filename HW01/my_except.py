class ErrorCounts(Exception):

    def __init__(self, msg):
        super().__init__()
        self.message = msg

    def __str__(self):
        return str(self.message)


class ErrorPrice(Exception):

    def __init__(self, msg):
        super().__init__()
        self.message = msg

    def __str__(self):
        return str(self.message)
