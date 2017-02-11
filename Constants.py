#!/usr/bin/python

class Constants:
    """Constants"""

    USER = "REPLACE ME"
    PASSWORD = "REPLACE ME"

    HOME_DIR = "/home/user/"
    SCRIPT_DIR = HOME_DIR + "CoinScript/"
    WALLET_DIR = SCRIPT_DIR + "wallets/"
    BAD_WALLET_DIR = WALLET_DIR + "bad/"
    LOCKED_WALLET_DIR = BAD_WALLET_DIR + "locked/"
    EMPTY_WALLET_DIR = BAD_WALLET_DIR + "empty/"
    OTHER_WALLET_DIR = BAD_WALLET_DIR + "other/"
    GOOD_WALLET_DIR = WALLET_DIR + "good/"
    NEW_WALLET_DIR = WALLET_DIR + "new/"
    OLD_WALLET_DIR = WALLET_DIR + "old/"

    COIN_LIST_PATH = "coin_list"
