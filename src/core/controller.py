import json

from pathlib import Path
from dataclasses import dataclass
from core import models


@dataclass
class ControllerConfig:
    path_to_info_json: Path
    path_to_avatar_jpg: Path


class Controller:

    def __init__(
        self,
        config: ControllerConfig
    ) -> None:
        self.__info = config.path_to_info_json
        self.__avatar = config.path_to_avatar_jpg

        self.__data = self.__read_data_json()

    def __read_data_json(
        self,
    ) -> models.Data:
        with open(self.__info, 'r', encoding='utf-8') as info:
            json_data: dict = json.load(info)

            for field in ['work_experience', 'education']:
                for key, value in json_data.get(field, '').items():
                    json_data[field][key] = models.Experience(
                        start=value.get('start', ''),
                        end=value.get('end', ''),
                        location=value.get('location', ''),
                        position=value.get('position', ''),
                        description=value.get('description', [''])
                    )

            data: models.Data = models.Data(**json_data)

            return data

    def get_data(
        self
    ) -> models.Data:
        return self.__data

    def get_avatar(
        self
    ) -> Path:
        return self.__avatar
