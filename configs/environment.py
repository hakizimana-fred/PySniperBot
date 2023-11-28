import os
from dotenv import load_dotenv


load_dotenv()


class Environment:
    node_provider = os.getenv("WS_PROVIDER")
