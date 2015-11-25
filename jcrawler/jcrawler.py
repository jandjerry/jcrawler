import bot

def main():
    url = bot.url.Url('http://yahoo.com');
    crawler = bot.bot.Bot(url)
    crawler.run()


if __name__ == "__main__":
    main()
