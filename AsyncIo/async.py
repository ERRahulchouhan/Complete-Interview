import asyncio
import time

async def funtion1():
    await asyncio.sleep(4)
    print("fun1")

async def funtion2():
    await asyncio.sleep(4)
    print("fun2")

async def funtion3():
    await asyncio.sleep(4)
    print("fun3")

# async def main():
#     await funtion1()
#     await funtion2()
#     await funtion3()
    
# asyncio.run(main())

# when time is available automatic function1 will execute
"""
async def main():
    task = asyncio.create_task(funtion1())
    await funtion2()
    await funtion3()
    
asyncio.run(main())
"""
# all will run at a time
async def main():
    L = await asyncio.gather(funtion1(),funtion2(),funtion3())
    
asyncio.run(main())

