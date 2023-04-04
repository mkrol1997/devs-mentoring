from InstaFollower import InstaFollower

USERNAME = "Your instagram acc login"
PASSWORD = "Your instagram acc password"
INSTA_ACCOUNT = 'pythonbot301'


insta_bot = InstaFollower()
insta_bot.login(USERNAME, PASSWORD)
insta_bot.search_insta_account(INSTA_ACCOUNT)

to_follow = insta_bot.get_followers_list()
print(len(to_follow))
insta_bot.follow_profiles(to_follow)
