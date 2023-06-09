from typing import Optional, Iterable, List, Callable

from functions import filter_query, unique_query, limit_query, map_query, sort_query, regex_query

CMD_TO_FUNCTIONS: dict[str, Callable[..., Iterable[str]]] = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
    'regex': regex_query,
}


def read_file(file_name: str) -> Iterable[str]:
    with open(file_name) as file:
        for line in file:
            yield line


def build_query(cmd: str, value: str, file_name: str, data: Optional[Iterable[str]]) -> List[str]:
    if data is None:
        prepared_data: Iterable[str] = read_file(file_name)
    else:
        # assert data is not None
        prepared_data = data

        func: Callable = CMD_TO_FUNCTIONS[cmd]
        result: Iterable[str] = func(value=value, data=prepared_data)

    return list(result)
