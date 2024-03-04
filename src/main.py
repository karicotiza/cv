from pathlib import Path
from core.controller import Controller, ControllerConfig
from core.views import Views, ViewsConfig

if __name__ == '__main__':
    path_to_info_json: Path = Path('data', 'info.json')
    path_to_avatar_jpg: Path = Path('data', 'avatar.jpg')

    controller_config: ControllerConfig = ControllerConfig(
        path_to_info_json=path_to_info_json,
        path_to_avatar_jpg=path_to_avatar_jpg
    )

    controller: Controller = Controller(
        config=controller_config
    )

    views_config: ViewsConfig = ViewsConfig(
        controller=controller,
        left_column_width=0.77,
        right_column_width=0.23
    )

    views: Views = Views(
        views_config
    )
