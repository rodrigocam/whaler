import yaml
from .utils import is_compose
from .compose.compose import Compose


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
    compose = Compose(data, file_path)

    for s in compose.services:
        if s.build:
            s.build.is_valid(file_path)
