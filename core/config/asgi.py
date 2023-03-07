from django.core.asgi import get_asgi_application
import asyncio
import os
import django
#
#
# class MyASGIHandler(ASGIHandler):
#     def __init__(self):
#         super().__init__()
#         self.on_shutdown = []
#
#     async def __call__(self, scope, receive, send):
#         if scope['type'] == 'lifespan':
#             while True:
#                 message = await receive()
#                 if message['type'] == 'lifespan.startup':
#                     # Do some startup here!
#                     await send({'type': 'lifespan.startup.complete'})
#                 elif message['type'] == 'lifespan.shutdown':
#                     # Do some shutdown here!
#                     await self.shutdown()
#                     await send({'type': 'lifespan.shutdown.complete'})
#                     return
#         await super().__call__(scope, receive, send)
#
#     async def shutdown(self):
#         for handler in self.on_shutdown:
#             if asyncio.iscoroutinefunction(handler):
#                 await handler()
#             else:
#                 handler()
#
#
# def my_get_asgi_application():
#     django.setup(set_prefix=False)
#     return MyASGIHandler()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# application = my_get_asgi_application()
application = get_asgi_application()
