from linkedin_bot import LinkedInBot
ACCOUNT_EMAIL = "YourEmail@example.com"
ACCOUNT_PASSWORD = "YourPassword"
PHONE = "YourPhoneNumber"



if __name__ == "__main__":

    bot = LinkedInBot(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, PHONE)
    bot.run()


