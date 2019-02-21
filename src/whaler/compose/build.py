

class Build:
    """
    Representation of the "build" option on docker-compose.yml.
    """

    def __init__(self, obj):
        if(isinstance(obj, dict)):
            self.context = obj['context']
            self.dockerfile = obj['dockerfile']
        elif(isinstance(obj, str)):
            self.context = obj
        else:
            raise TypeError(f'Invalid "build: {obj}" option')

    def is_valid(self):
        raise NotImplementedError
