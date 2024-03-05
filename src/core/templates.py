def headline(
    name: str,
    date_of_birth: str,
    occupation: str,
) -> str:
    memory: list[str] = ['', name, date_of_birth, '', occupation]
    template: str = f'``` {'\n'.join(memory)}'

    return template


def experience_title(
    place: str,
    position: str,
    start: str,
    end: str,
    location: str
) -> str:
    memory: list[str] = ['']

    memory.append(f'{place}, {position}')
    memory.append(f'{start} - {end}')
    memory.append(location)

    template: str = f'``` {'\n'.join(memory)}'

    return template


def experience_description(
    description: list[str]
) -> str:
    memory: list[str] = ['']

    for line in description:
        memory.append(line)

    template: str = f'{'\n'.join(memory)}'

    return template


def skill_points(
    points: list[str]
) -> str:
    memory: list[str] = []

    for point in points:
        message: str = f'```{point}```'
        memory.append(message)

    template = ' '.join(memory)

    return template


def contacts(
    contacts_dictionary: dict[str, str]
) -> str:
    message: list[str] = [
            '',
        ]

    for key, value in contacts_dictionary.items():
        message.append(f'{key}: {value}')

    template: str = f'``` {'\n'.join(message)}'

    return template
