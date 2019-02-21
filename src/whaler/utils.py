
def is_docker_compose(data):
    if 'version' in data and 'services' in data:
        return True

    return False
