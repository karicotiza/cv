import streamlit

from pathlib import Path
from dataclasses import dataclass
from core import controller, models
from streamlit.delta_generator import DeltaGenerator


@dataclass
class ViewsConfig:
    controller: controller.Controller
    left_column_width: float
    right_column_width: float


class Views:

    def __init__(
        self,
        config: ViewsConfig
    ) -> None:
        self.__controller: controller.Controller = config.controller
        self.__left_column_width: float = config.left_column_width
        self.__right_column_width: float = config.right_column_width

        self.__data: models.Data = self.__controller.get_data()
        self.__avatar: Path = self.__controller.get_avatar()

        self.__init_view()

    def __init_view(
        self
    ) -> None:
        self.__header_view()
        self.__work_experience_view()
        self.__skills_view()
        self.__education_view()
        self.__contacts__view()

    def __header_view(
        self,
    ) -> None:
        columns: list[DeltaGenerator] = streamlit.columns(
            [self.__left_column_width, self.__right_column_width]
        )

        left_column, right_column = columns

        with left_column:
            with streamlit.container(border=True):
                message: list[str] = [
                    '',
                    self.__data.name,
                    self.__data.date_of_birth,
                    '',
                    self.__data.occupation,
                ]

                template: str = f'``` {'\n'.join(message)}'

                streamlit.markdown(template)

        with right_column:
            with streamlit.container(border=True):
                streamlit.image(
                    str(self.__avatar),
                )

    def __work_experience_view(
        self
    ) -> None:
        with streamlit.expander("Work Experience"):
            for key, value in self.__data.work_experience.items():
                memory_for_head: list[str] = [
                    '',
                ]

                memory_for_body: list[str] = [
                    '',
                ]

                memory_for_head.append(f'{key}, {value.position}')
                memory_for_head.append(f'{value.start} - {value.end}')
                memory_for_head.append(value.location)

                for line in value.description:
                    memory_for_body.append(line)

                head: str = f'``` {'\n'.join(memory_for_head)}'
                body: str = f'{'\n'.join(memory_for_body)}'

                streamlit.markdown(head)
                streamlit.markdown(body)

    def __skills_view(
        self
    ) -> None:
        with streamlit.expander("Skills"):
            for key, value in self.__data.skills.items():
                streamlit.caption(key)

                memory: list[str] = []

                for skill in value:
                    message: str = f'```{skill}```'
                    memory.append(message)

                message = ' '.join(memory)

                streamlit.markdown(message)

    def __education_view(
        self,
    ) -> None:
        with streamlit.expander("Education"):
            for key, value in self.__data.education.items():
                memory: list[str] = [
                    '',
                ]

                memory.append(f'{key}, {value.specialization}')
                memory.append(f'{value.started} - {value.finished}')
                memory.append(value.location)

                template: str = f'``` {'\n'.join(memory)}'

                streamlit.markdown(template)

    def __contacts__view(
        self,
    ) -> None:
        message: list[str] = [
            '',
        ]

        for key, value in self.__data.contacts.items():
            message.append(f'{key}: {value}')

        template: str = f'``` {'\n'.join(message)}'

        with streamlit.expander("Contacts"):
            streamlit.markdown(template)
