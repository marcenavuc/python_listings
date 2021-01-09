import asyncio


async def foo():
    print("Running in foo")
    await asyncio.sleep(1)
    print("Return to foo")


async def bar():
    print('Explicit context to bar')
    await asyncio.sleep(1)
    print('Implicit context switch back to bar')


event_loop = asyncio.get_event_loop()
tasks = [event_loop.create_task(foo()), event_loop.create_task(bar())]
wait_tasks = asyncio.wait(tasks)
event_loop.run_until_complete(wait_tasks)
event_loop.close()
