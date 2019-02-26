import os


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

    def is_valid(self, file_path):
        context_path = os.path.join(os.path.dirname(file_path), self.context)
        if not os.path.isfile(os.path.join(context_path, self.dockerfile)):
            raise FileNotFoundError(
                f"Dockerfile '{self.dockerfile}' "
                f"not found at context' {self.context}'"
            )
