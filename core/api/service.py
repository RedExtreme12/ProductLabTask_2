from abc import ABC, abstractmethod
from copy import copy
from typing import Union, List, Any, Dict

from .wildberries.wildberries_requests_info_accumulator import build_wildberries_requests_accumulator


class BaseService(ABC):

    def __init__(self):
        pass

    def __call__(self) -> Any:
        return self.act()

    @abstractmethod
    def act(self) -> Any:
        raise NotImplementedError


class ArticlesHandler(BaseService):

    pattern = 'https://basket-05.wb.ru/vol{volume}/part{part}/{article}/info/sellers.json'

    def __init__(self, articles: Union[List[str], str]):
        super().__init__()

        self._articles = None
        self.articles = articles

    @property
    def articles(self):
        return self._articles

    @articles.setter
    def articles(self, value: Union[List[str], str]):
        if isinstance(value, list):
            self._articles = copy(value)
        elif isinstance(value, str):
            self._articles = [value]
        else:
            raise ValueError('Need a list or str')

    def act(self) -> List[Dict]:
        result_jsons = [
            build_wildberries_requests_accumulator(
                self.pattern,
                article
            ).get_product_card().dict()
            for article in self.articles
        ]

        return result_jsons




