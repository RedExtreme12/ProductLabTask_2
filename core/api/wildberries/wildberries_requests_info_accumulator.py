from typing import Union

from .url_formatters import UrlFormatter, WildberriesUrlFormatter
from .article_separators import ArticleSeparator, WildberriesArticleSeparator
from .wildberries_request import RequestMaker, WildberriesRequestAsync
from .payload_objects.product_card import ProductCard


class WildberriesRequestsInfoAccumulator:

    def __init__(
            self,
            article_separator: ArticleSeparator,
            url_formatter: UrlFormatter,
            request_maker: RequestMaker,
    ):
        self._article_separator = article_separator
        self._url_formatter = url_formatter
        self._request_maker = request_maker

        self._separated_article = None
        self._formatted_url = None

        self._prepare()

    def _prepare(self):
        self._separated_article = self._article_separator.separate()

        self._formatted_url = self._url_formatter.format_url(
            volume=self._separated_article.volume,
            part=self._separated_article.part,
            article=self._separated_article.full_article,
        )

        self._request_maker.url = self._formatted_url

    def get_product_card(self) -> ProductCard:
        json_ = self._request_maker.make_request()

        article = json_['nmId']
        supplier_name = json_['supplierName']
        trademark = json_['trademark']

        product_card = ProductCard(article=article, supplier_name=supplier_name, trademark=trademark)

        return product_card


def build_wildberries_requests_accumulator(
        url_pattern: str,
        article: Union[int, str]
) -> WildberriesRequestsInfoAccumulator:
    article_separator = WildberriesArticleSeparator(article)

    url_formatter = WildberriesUrlFormatter(
        pattern=url_pattern
    )

    wildberries_request = WildberriesRequestAsync()

    return WildberriesRequestsInfoAccumulator(
        article_separator=article_separator,
        url_formatter=url_formatter,
        request_maker=wildberries_request,
    )
