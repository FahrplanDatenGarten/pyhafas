from typing import Union


def find(station_name_by_lid: dict[str, str], lid: str, id: str) -> Union[str, None]:
    to_search = lid if lid else id
    for entry in station_name_by_lid.items():
        if to_search.startswith(entry[0]):
            return entry[1]
    return None