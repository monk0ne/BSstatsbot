import brawlstats as bs
from config import TOKEN


user = bs.Client(token=TOKEN)
print(user.profile.brawlers)