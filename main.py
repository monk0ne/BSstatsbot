import brawlstats
from config import TOKEN


client = brawlstats.Client(TOKEN)
player = client.get_profile('#92URLQ2GQ')

