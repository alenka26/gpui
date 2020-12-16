import requests
import telegram_send

url = "https://api.telegram.org/bot"+TELEGRAM_TOKEN

if __name__ == "__main__":
    TELEGRAM_TOKEN = '1426788499:AAF5_2D2WjlQsUYa2cnGhQLMlfaK2viqYB0'
    CHAT_ID = '-1001409849256'
    path_config = telegram_send.get_config_path()
    with open(path_config, 'w') as f:
        f.write(f'[telegram]\ntoken = {TELEGRAM_TOKEN}\nchat_id = {CHAT_ID}')
    # checker = Checker()
    telegram_send.send(messages=["test).\n" 
        #+\
#        checker.check_energosbyt()])
