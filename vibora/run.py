#!/usr/bin/env python
# encoding: utf-8
"""
@author: morgan
@time: 2/21/19 11:46 AM
"""

from config.config import *
from vibora.responses import JsonResponse, asyncio, StreamingResponse

app = app


# @app.route('/')
# async def home():
#     return JsonResponse({'hello': 'world'})


@app.route('/')
async def home():
    async def stream_builder():
        for x in range(0, 5):
            yield str(x).encode()
            # await asyncio.sleep(1)

    return StreamingResponse(
        stream_builder, chunk_timeout=10, complete_timeout=30
    )


if __name__ == '__main__':
    port = 80
    if IS_DEBUG:
        port = 8000
    app.run(host="0.0.0.0", port=port)
