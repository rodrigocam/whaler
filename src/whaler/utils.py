from .compose.service import Service


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
        yield Service(name, value)


def get_version(data):
    """
    Return the version of a docker-compose.yml.
    """
    return data['version']
