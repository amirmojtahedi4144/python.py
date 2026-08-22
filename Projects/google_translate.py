import asyncio
from googletrans import Translator


async def main():
    print("############# WELCOME TO GOOGLE TRANSLATE #############")

    text_to_translate = input("Enter your word: ")

    if not text_to_translate.strip():
        print("Please enter a word or sentence.")
        return

    async with Translator() as translator:
        result = await translator.translate(
            text_to_translate,
            dest="fa"
        )

        print("Translation:", result.text)

    print("================================")
    print("Have a nice day!")


asyncio.run(main())