import logging
import config as cf
from aiogram import Bot, Dispatcher, executor, types
HELP_MESSAGE = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/buyryba</b> - <em>купить рыбов</em>
if __name__ == '__main__':
"""
ribov_list = [1,2,3,4,5,6,7,8,9]
token = cf.token
tgbot = Bot(token)
dp = Dispatcher(tgbot)

@dp.message_handler(commands = ['start'])
async def send_welkom(massege: types.Message):
    return await tgbot.send_massege.reply(massege.chat.id, "Я родился")

@dp.message_handler(commands = ['buyryba'])
async def send_welkom(massege: types.Message):
    args = message.get_args()
    if len(ribov_list) == 0:
        return await tgbot.send_massege.reply(massege.chat.id, "мы сожалеем , но рыбов""не осталось, Джамшут их съел и теперь мы продаем его на органы""приходите по позже")
    if not args:
        return await tgbotbot.send_message(message.chat.id, f"ейчас есть {len(ribov_list)}" f"рыбов в наличии. " f"сколько рыбов вы хотите + пивасик скидка от джамшута")
    else:
        if args.isdigit():
            args = int(args)
            if args > len(ribov_list):
                return await tgbot.send_message.chat.id, "звиняюсь у нас мало рыбов видите число поменьше "
            else:
                for i in range(args):
            ribov_list.pop()
            return awaittgbot.send_message(message.chat.id, f"осталось {len(ribov_list)} " f"рыбов в наличие")
@dp.message_handler(commands = ['help'])
async def send_welkom(massege: types.Message):
    return await tgbot.send_massege.reply(massege.chat.id,
                                        HELP_MESSAGE<"HTML")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)