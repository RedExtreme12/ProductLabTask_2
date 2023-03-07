from abc import ABC, abstractmethod
from typing import Union

from .payload_objects.separated_article import SeparatedArticle


class ArticleSeparator(ABC):

    @abstractmethod
    def separate(self):
        raise NotImplementedError()


class WildberriesArticleSeparator(ArticleSeparator):

    def __init__(self, article: Union[str, int]):
        self._article = None
        self.article = article

    @property
    def article(self):
        return self._article

    @article.setter
    def article(self, value: Union[str, int]):
        if isinstance(value, int):
            self._article = str(value)
        elif isinstance(value, str):
            self._article = value
        else:
            raise ValueError('Article can be only str or int')

    def separate(self) -> SeparatedArticle:
        volume = self.article[:3]
        part = self.article[:5]
        article = self.article

        return SeparatedArticle(volume=volume, part=part, full_article=article)
