import time
import asyncio

async def brew_coffe():
    print("Brewing coffee...")
    # await time.sleep(5)
    await asyncio.sleep(5)
    print("End brewing coffee...")
    return "Coffee is ready."

async def toast_bagel():
    print("Toasting bagel...")
    # await time.sleep(3)
    await asyncio.sleep(3)
    print("End toasting bagel...")
    return "Bagel toasted."


async def main():
    start_time = time.time()

    # coffee = brew_coffe()
    # bagel = toast_bagel()
    # batch = asyncio.gather(brew_coffe(), toast_bagel())
    # coffee, bagel = await batch
    coffee_task = asyncio.create_task(brew_coffe())
    bagel_task = asyncio.create_task(toast_bagel())

    coffee = await coffee_task
    bagel = await bagel_task

    end_time = time.time()
    elasped_time = end_time - start_time

    print(f"Coffee: {coffee}")
    print(f"Bagel: {bagel}")
    print(f"Total time taken: {elasped_time} seconds")


if __name__ == "__main__":
    asyncio.run(main())