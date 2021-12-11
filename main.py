from fastapi import FastAPI, Query
import aioredis
from anogram import is_input_anogram
import aioredis

app = FastAPI()


@app.get("/")
async def root():
    return {"message": 'Thanks for giving me an oppotunity to share myself'}


@app.get("/isanogram")
async def counter_of_anagrams(q: str = Query(None), q2: str = Query(None)):
    """ Принимает на вход две строки.
     Возвращает количество полученных анаграмм за все время."""
    is_anagram = is_input_anogram(q, q2)
    return await counter(is_anagram)


async def counter(is_anagram: bool):
    """ функция увеличения счетчика. на вход приходит тру/фолс"""
    redis = aioredis.from_url("redis://localhost/0")
    # идем в редис за счетчиком
    my_counter_of_anagrams = await redis.get("counter")
    # интуем
    my_counter_of_anagrams = int(my_counter_of_anagrams)
    # если значения не получили считаем что наш счетчик = 0

    if not my_counter_of_anagrams:          # эквивалентно if ...== None
        my_counter_of_anagrams = 0
        # записываем его в редис
        await redis.set("counter", my_counter_of_anagrams)

    # если на вход пришло тру - увеличиваем счетчик на 1
    # если фолс - оставляем таким же
    if is_anagram:  # эквивалентно    if is_anagram == True
        result = 'Yes, it is anagrmm '
        my_counter_of_anagrams = my_counter_of_anagrams + 1
    else:
        result = 'Not an anagrmm '
        my_counter_of_anagrams = my_counter_of_anagrams
    # записываем в редис актуальное значение счетчика
    await redis.set("counter", my_counter_of_anagrams)
    # возвращаем значение, которе потом выведется в браузере
    return f"{result}. Total counter of anagrams: {my_counter_of_anagrams}"