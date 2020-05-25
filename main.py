#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from aiogram import Bot, Dispatcher, executor, types
import requests
import asyncio
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import os
from stem import Signal
from stem.control import Controller

API_TOKEN = "406995115:AAEX_Dk8KQOXkLICfZKCvTWA7yw38tLVlcQ"
CHANNEL = -1001436713727

api_id_0 = 908484
api_hash_0 = "5c0c8d2020848c64d37f1e41a7e28bea"

if os.path.isdir("downloaded") is False:
    print(f"downloaded directory dose not exitst\ncurrent directory: {os.getcwd()}")
    os.mkdir("downloaded")
    print("downloaded directory created!")


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}
# proxies1 = {
#     'http': 'socks4://37.235.28.42:40520',
#     'https': 'socks4://37.235.28.42:40520'
# }

ua = UserAgent()

@dp.message_handler(commands="ketab")
async def ketabonline(message: types.Message):
    try:
        msg = await message.reply("Handling...")
        headers = ua.chrome
        try:
            req = requests.get(url="https://ketaabonline.com/", headers={'User-Agent': headers}, allow_redirects=True).text
        except requests.exceptions.ConnectionError:
            with Controller.from_port(port=9051) as controller:
                controller.authenticate("si63236323na")
                controller.signal(Signal.NEWNYM)
            with_tor = requests.get(url='https://ident.me', proxies=proxies).text
            await bot.send_message(CHANNEL, f"Ip changed: {with_tor}")
            req = requests.get(url="https://ketaabonline.com/", headers={'User-Agent': headers}, allow_redirects=True).text

        soup = BeautifulSoup(req, 'lxml')

        three_main = soup.find('div', {'id': 'bookcats'}).find('div', class_='row flex-row no-margin').find_all('div', class_='col s12 no-margin')
        count = 0
        sents = 0
        for three in three_main:
            try:
                useragent = ua.random
                if (count % 3) == 0:
                    print(f"{count} one, its 0, passing...")
                    count += 1
                    continue
                elif (count % 3) == 1:
                    print(f"{count} one, its 1, send header and passing...")
                    header = three.find('header', class_='page-header').h2.text
                    full_cat = f"#fullcategory\n\n{header}"
                    await bot.send_message(chat_id=CHANNEL, text=full_cat)
                    count += 1
                    await asyncio.sleep(2)
                    continue
                elif (count % 3) == 2:
                    print(f"{count} one, thats it, im on it...")
                    count += 1
                    main_d = three.find('div', class_='row flex-row no-margin').find_all('div', class_='col l2 m3 s6')
                    for divs in main_d:
                        cat = divs.h3.text
                        url = divs.a['href']
                        await bot.send_message(chat_id=CHANNEL, text=f'<a href="{url}">{cat}</a>', disable_web_page_preview=True, parse_mode='Html')
                        await asyncio.sleep(5)

                        try:
                            breq = requests.get(url=url, headers={'User-Agent': useragent}, allow_redirects=True).text
                        except requests.exceptions.ConnectionError:
                            with Controller.from_port(port=9051) as controller:
                                controller.authenticate("si63236323na")
                                controller.signal(Signal.NEWNYM)
                            with_tor = requests.get(url='https://ident.me', proxies=proxies).text
                            await bot.send_message(CHANNEL, f"Ip changed: {with_tor}")
                            breq = requests.get(url=url, headers={'User-Agent': useragent}, allow_redirects=True).text
                        await asyncio.sleep(3)
                        fsoup = BeautifulSoup(breq, 'lxml')
                        pages = fsoup.find('div', class_='col s12 m12 s12 navigation clearfix').ul.find_all('li')[-2].text
                        pages = int(pages)
                        await asyncio.sleep(3)
                        for page in range(1, pages + 1):
                            page_url = url + f"page/{page}"
                            try:
                                breq = requests.get(url=page_url, headers={'User-Agent': useragent},
                                                    allow_redirects=True).text
                            except requests.exceptions.ConnectionError:
                                with Controller.from_port(port=9051) as controller:
                                    controller.authenticate("si63236323na")
                                    controller.signal(Signal.NEWNYM)
                                with_tor = requests.get(url='https://ident.me', proxies=proxies).text
                                await bot.send_message(CHANNEL, f"Ip changed: {with_tor}")
                                breq = requests.get(url=page_url, headers={'User-Agent': useragent},
                                                    allow_redirects=True).text
                            bsoup = BeautifulSoup(breq, 'lxml')
                            archive = bsoup.find('div', {'id': 'archive'}).find('div', class_='row flex-row no-margin booklist').find_all('div', class_='col l2 m3 s6')

                            for divs in archive:
                                try:
                                    book_url = divs.a['href']
                                    await asyncio.sleep(10)

                                    try:
                                        creq = requests.get(url=book_url, headers={'User-Agent': useragent}, allow_redirects=True).text
                                    except requests.exceptions.ConnectionError:
                                        with Controller.from_port(port=9051) as controller:
                                            controller.authenticate("si63236323na")
                                            controller.signal(Signal.NEWNYM)
                                        with_tor = requests.get(url='https://ident.me', proxies=proxies).text
                                        await bot.send_message(CHANNEL, f"Ip changed: {with_tor}")
                                        creq = requests.get(url=book_url, headers={'User-Agent': useragent}, allow_redirects=True).text
                                    csoup = BeautifulSoup(creq, 'lxml')

                                    entry_content = csoup.find('div', class_='entry-content')
                                    photo_url = entry_content.find('div', class_='col l4 m4 s12 no-margin').img['src']
                                    book_title = entry_content.find('header', class_='entry-header').h1.text
                                    book_table = entry_content.find('div', {'id': 'bookdetails'}).find('table', class_='booktable').find_all('tr')
                                    author = book_table[0].find_all('td')[1].text
                                    down_link = entry_content.find('div', {'id': 'bookdetails'}).find('div', class_='downloadandreadbook').a['href']
                                    photo_cap = f"Title: {book_title}\n\nAuthor: {author}"

                                    print()
                                    print(f"title:  {book_title}\npurl:   {photo_url}\nfurl:  {down_link}")
                                    print()

                                    filename = os.path.basename(down_link)
                                    r = requests.get(url=down_link, allow_redirects=True)

                                    open(f"downloaded/{filename}", "wb").write(r.content)

                                    await bot.send_photo(chat_id=CHANNEL, photo=photo_url, caption=photo_cap)
                                    await asyncio.sleep(5)
                                    file = types.InputFile(f"downloaded/{filename}")
                                    await bot.send_document(chat_id=CHANNEL, document=file)
                                    await asyncio.sleep(20)
                                    await msg.edit_text(f"{sents} Book sent...")
                                    sents += 1
                                except Exception as e:
                                    await bot.send_message(CHANNEL, f"Error: {e}")
            except Exception as e:
                await bot.send_message(CHANNEL, f"Error: {e}")

        await msg.edit_text(f"Done!, total: {sents}")
    except Exception as e:
        await bot.send_message(CHANNEL, f"Error: {e}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

