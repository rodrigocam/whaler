import yaml
from .utils import is_compose, get_services


def process_file(file_path):
    """
    Process Dockerfile and docker-compose.yml.
    """
    with open(file_path) as f:
        data = yaml.safe_load(f)
        if(is_compose(data)):
            process_compose(data, file_path)


def process_folder(folder):
    pass


def process_compose(data, file_path):
    services = list(get_services(data))
    print(services)
