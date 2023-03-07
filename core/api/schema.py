from drf_yasg import openapi

article_param_config = openapi.Parameter(
    'article',
    in_=openapi.IN_FORM,
    description='article',
    type=openapi.TYPE_INTEGER
)

file_param_config = openapi.Parameter(
    'file',
    in_=openapi.IN_FORM,
    description='file',
    type=openapi.TYPE_FILE,
)
