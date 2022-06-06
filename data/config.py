from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")

log_chat_id = env.str("log_chat_id")
errors_chat_id = env.str("errors_chat_id")

db_name = env.str("db_name")
log_file_name = env.str("log_file_name")


skip_updates = True
