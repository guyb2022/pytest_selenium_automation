import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()


class TestData:
    load_dotenv(find_dotenv())
    url = os.getenv("url")
    email = os.getenv("mail")
    password = os.getenv("password")
