import dotenv


config = dotenv.dotenv_values('config.env')
bot_token = config['bot_token']
