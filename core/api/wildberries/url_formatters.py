from abc import ABC, abstractmethod


class UrlFormatter(ABC):

    def __init__(self, pattern: str):
        self._pattern = pattern

    @abstractmethod
    def format_url(self, **params) -> str:
        raise NotImplementedError


class WildberriesUrlFormatter(UrlFormatter):

    def __init__(self, pattern: str):
        super().__init__(pattern)

    def format_url(self, **params) -> str:
        return self._pattern.format(**params)
