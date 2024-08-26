import asyncio
from typing import Iterable, Any


def split_list(a: list, n: int) -> Iterable[list[Any]]:
    """
    Split list 'a' into 'n' approximately equal sublists
    """
    k, m = divmod(len(a), n)
    for sublist in [a[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)] for i in range(n)]:
        yield sublist


async def async_example() -> None:

    def do_thing(items) -> int:
        s: int = sum(items)
        print(s)
        print(items)
        return s

    async def do_async_thing(items) -> int:
        loop: asyncio.AbstractEventLoop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, do_thing, items)

    all_things = list(range(100))
    batches: Iterable[list[Any]] = split_list(all_things, 5)

    work = [do_async_thing(items) for items in batches]
    results: list[int] = await asyncio.gather(*work)

    print(results)


def main() -> None:
    asyncio.run(async_example())


if __name__ == "__main__":
    main()
