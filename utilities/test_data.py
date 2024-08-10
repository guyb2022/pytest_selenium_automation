import os
from dotenv import load_dotenv, find_dotenv


class TestData:
    load_dotenv(find_dotenv())
    url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/login"
    email = os.environ.get("email")
    password = os.environ.get("password")
