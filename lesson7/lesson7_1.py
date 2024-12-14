from tools import taipei

try:
    youbikes_data:list[dict] = taipei.get_youbikes()
except Exception as e:
    print(e)
else:
    print(youbikes_data)