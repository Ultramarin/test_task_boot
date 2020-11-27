from envparse import Env

env = Env()

# Values can be used from env file.
env.read_envfile()

# Telegram Bot Token
BOT_TOKEN = env("SCREENSHOT_BOT_TOKEN")

# Logging level
LOGGING_LEVEL = env("LOGGING_LEVEL", default="INFO")

START_MESSAGE = (
    "Hello, I'm simple screenshot bot."
    "Use me to get a screenshot of any webpage."
    "Just send me any webpage link and I will send you a screenshot!"
)

WEB_URL_REGEX = (
    r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"
)

SCREENSHOT_WIDTH = 1920

SCREENSHOT_HEIGHT = 1080

FULL_PAGE_SCREENSHOT = False
