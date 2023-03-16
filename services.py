import asyncio
from aiohttp import ClientSession
import pprint


async def request_url(url, data):
    print("request_url start working")
    async with ClientSession() as sessions:
        async with sessions.get(url, params=data) as response:
            result = await response.json()
    print('Ok', url)
    # product = {result[0]['items'][0]["brand"]["title"]:result[0]['items'][0]['storeProduct']['price'] for i in result}
    return result

async  def get_info_product(goods):
    url = "https://green-dostavka.by/api/v1/products/search/"
    data = {
        "storeId": 2,
        "includeAdultOnly": "true",
        "search": goods
    }
    result = await asyncio.gather(request_url(url, data))
    return result
async def main():


    res = await asyncio.gather(get_info_product("молоко"))
    print(res)
    return res
    # pprint.pprint(result[0]['items'][1]["brand"]["title"])
    # pprint.pprint(result[0]['items'][1]['storeProduct']['price'])


if __name__ == "__main__":
    asyncio.run(main())
