import tools

try:
    youbikes_data:list[dict] = tools.get_youbikes()
except Exception as e:
    print(e)
else:
    print(youbikes_data)