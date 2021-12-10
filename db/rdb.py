import asyncio

import aioredis

async def counter():

    redis = aioredis.from_url("redis://localhost/0")
    value = await redis.get("counter")
    print(value)
    await redis.set("counter", int(value)+1)
    return(int(value))




#if __name__ == "__main__":
    #asyncio.run(main())


