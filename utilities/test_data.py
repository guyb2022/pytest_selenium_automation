import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()


class TestData:
    load_dotenv(find_dotenv())
    url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/login"
    email = os.getenv("mail")
    password = os.getenv("password")
