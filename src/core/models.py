from dataclasses import dataclass


@dataclass
class Job:
    start: str
    end: str
    location: str
    position: str
    description: list[str]


@dataclass
class Education:
    started: str
    finished: str
    location: str
    specialization: str


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
        str, Job
    ]
    education: dict[
        str, Education
    ]
