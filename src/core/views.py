import streamlit

from pathlib import Path
from dataclasses import dataclass
from core import controller, models, templates
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
                template: str = templates.headline(
                    self.__data.name,
                    self.__data.date_of_birth,
                    self.__data.occupation
                )

                streamlit.markdown(template)

        with right_column:
            with streamlit.container(border=True):
                streamlit.image(str(self.__avatar))

    def __work_experience_view(
        self
    ) -> None:
        with streamlit.expander("Work Experience"):
            for key, value in self.__data.work_experience.items():
                title: str = templates.experience_title(
                    key,
                    value.position,
                    value.start,
                    value.end,
                    value.location
                )

                description: str = templates.experience_description(
                    value.description
                )

                streamlit.markdown(title)
                streamlit.markdown(description)

    def __skills_view(
        self
    ) -> None:
        with streamlit.expander("Skills"):
            for key, value in self.__data.skills.items():
                streamlit.caption(key)

                points: str = templates.skill_points(value)

                streamlit.markdown(points)

    def __education_view(
        self,
    ) -> None:
        with streamlit.expander("Education"):
            for key, value in self.__data.education.items():
                education: str = templates.experience_title(
                    key,
                    value.position,
                    value.start,
                    value.end,
                    value.location,
                )

                streamlit.markdown(education)

    def __contacts__view(
        self,
    ) -> None:
        template: str = templates.contacts(self.__data.contacts)

        with streamlit.expander("Contacts"):
            streamlit.markdown(template)
