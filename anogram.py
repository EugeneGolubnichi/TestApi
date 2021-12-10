from db.rdb import counter
import asyncio






def Anogram_check(str1, str2,a):

    if (sorted(str1) == sorted(str2)):


        return (f"Anogram:{a}")
    else:
        return ("Both strings are not an Anagram.")


