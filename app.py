import json

from aiohttp import web
from services import get_info_product

app = web.Application()
routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world!")

@routes.get('/friend/')
async def friend(request):
    return web.Response(text="Hello, friend!!!")

@routes.get('/search/')
async def friend(request):
    name = request.query.get('name')
    result = await get_info_product(name)
    return web.Response(body=json.dumps(result), content_type='application/json')

@routes.post('/book/')
async def book(request):
    book_detail = await request.json()
    result = {'card_id': 24141212, 'name': book_detail['name']}
    return web.Response(body=json.dumps(result), content_type='application/json')



app.add_routes(routes)

web.run_app(
    app,
    host='127.0.0.1',
    port=8002
)
