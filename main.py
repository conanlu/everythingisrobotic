import discord
import syllables
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
intents = discord.Intents.default()
intents.message_content = True


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if message.author.bot:
            return

        sentence = message.content.lower().split()

        length = len(sentence)

        if length > 10:
            return

        if length == 2:
            if (sentence[0] == 'everything') and (sentence[1] == 'is'):
                await message.channel.send('romantic')
                return

        if sentence.count('on') == 1:
            onpoint = sentence.index('on')
            pre_syllables = 0
            for i in range(onpoint):
                pre_syllables += syllables.estimate(sentence[i])
            post_syllables = 0
            for i in range(onpoint+1, length):
                post_syllables += syllables.estimate(sentence[i])

            print (str(pre_syllables) + " " + str(post_syllables))
            if (pre_syllables == 3 or pre_syllables == 4) and (post_syllables == 4 or post_syllables == 5):
                await message.channel.send('jesus christ on a plastic sign')

        elif length > 3:
            if sentence[length-3] == 'again' and sentence[length-2] == 'and' and sentence[length-1] == 'again':
                syllablesin = 0
                for i in range(length-3):
                    syllablesin += syllables.estimate(sentence[i])

                if syllablesin == 3:
                    await message.channel.send('winding roads doing manual drive')


client = MyClient(intents=intents)


client.run(os.environ.get('TOKEN'))