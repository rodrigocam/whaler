from .compose import service


def is_compose(data):
    """
    Verify if the data corresponds to a docker-compose.yml.
    """
    if 'version' in data and 'services' in data:
        return True

    return False


def get_services(data):
    """
    Return all services of a docker-compose.yml.
    """
    for name, value in data['services'].items():
        yield service.Service(name, value)
