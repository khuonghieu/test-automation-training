import json

class TestData:
    BASE_URL = "https://www.got-it.io/solutions/excel-chat/"
    SUCCESSFUL_TRANSACTION_CARD = {
        "NUMBER": "4009348888881881",
        "DATE": "0522",
        "CVV": "123",
        "POSTAL": "19123"
    }
    FAIL_TRANSACTION_CARD = {
        "NUMBER": "4000111111111115",
        "DATE": "0522",
        "CVV": "200",
        "POSTAL": "19123"
    }
    LOGIN_SUCCESS_ACCOUNT = {
        "USERNAME": "khuongletrunghieu1@gmail.com",
        "PASSWORD": "Abc123!"
    }
    LOGIN_FAIL_ACCOUNT = {
        "USERNAME": "khuongletrunghieu1@gmail.com",
        "PASSWORD": "Abc123@"
    }

    INCOMPLETE_CARD_NUMBER = "400934888888"
    INCOMPLETE_CARD_DATE = "5"
    INCOMPLETE_CARD_CVV = "12"
    INCOMPLETE_CARD_POSTAL = ""
