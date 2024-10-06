import json
import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    LICENSE_KEY = os.getenv("LICENSE_KEY")

    API_ID = os.getenv("API_ID")
    API_HASH = os.getenv("API_HASH")

    POINTS_COUNT = json.loads(os.getenv("POINTS_COUNT", "[450, 600]"))
    AUTO_PLAY_GAME = os.getenv("AUTO_PLAY_GAME", "True")
    AUTO_TASK = os.getenv("AUTO_TASK", "True")
    AUTO_DAILY_REWARD = os.getenv("AUTO_DAILY_REWARD", "True")
    AUTO_CLAIM_STARS = os.getenv("AUTO_CLAIM_STARS", "True")
    AUTO_CLAIM_COMBO = os.getenv("AUTO_CLAIM_COMBO", "True")

    USE_RANDOM_DELAY_IN_RUN = os.getenv("USE_RANDOM_DELAY_IN_RUN", "True")
    RANDOM_DELAY_IN_RUN = json.loads(os.getenv("RANDOM_DELAY_IN_RUN", "[5, 30]"))

    USE_PROXY_FROM_FILE = os.getenv("USE_PROXY_FROM_FILE", "False")


settings = Settings()
