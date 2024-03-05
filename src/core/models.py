from dataclasses import dataclass


@dataclass
class Experience:
    start: str
    end: str
    location: str
    position: str
    description: list[str]


@dataclass
class Data:
    name: str
    date_of_birth: str
    contacts: dict[
        str, str
    ]
    occupation: str
    skills: dict[
        str, list[str]
    ]
    work_experience: dict[
        str, Experience
    ]
    education: dict[
        str, Experience
    ]
