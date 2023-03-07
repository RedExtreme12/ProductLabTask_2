from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .schema import article_param_config, file_param_config

from .service import ArticlesHandler
from .xlsx_handlers.utils import get_articles_to_process


class ProductDetailApiView(APIView):
    parser_classes = (MultiPartParser, )

    @swagger_auto_schema(
        manual_parameters=[article_param_config, file_param_config],
        parser_classes=parser_classes,
        responses={status.HTTP_400_BAD_REQUEST: 'You should pass only one parameter: only one article or only file',}
    )
    def post(self, request: Request):
        article = request.data.get('article')
        xlsx_file = request.FILES.get('file')

        if article and xlsx_file:
            return Response(
                {'Error': 'You should pass only one parameter: only one article or only file'},
                status.HTTP_400_BAD_REQUEST
            )

        articles_to_process = None
        if article:
            articles_to_process = [article]
        elif xlsx_file:
            articles_to_process = get_articles_to_process(xlsx_file)

        product_cards_jsons = ArticlesHandler(articles_to_process).act()

        return Response(product_cards_jsons, status=status.HTTP_200_OK)
