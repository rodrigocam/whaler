from .build import Build


class Service:
    """
    Representation of the "service" on docker-compose.yml.
    """

    def __init__(self, name, value):
        self.name = name
        self.build = None
        try:
            self.build = Build(value['build'])
        except KeyError:
            pass
