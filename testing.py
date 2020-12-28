# %%
from configparser import ConfigParser


parser = ConfigParser()
parser.read('config.ini')
print('test' in parser.sections())


print(parser.sections())
print(type(parser.get('settings', 'selected_db')))

with open('config.ini', 'w') as f:
    parser.set("settings", "selected_db", "none")
    parser.write(f)
try:
    dat = int(parser.get('settings', 'selected_db'))
except:
    print("exception")

# %%
