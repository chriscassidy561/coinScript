#!/usr/bin/python
from CoinDaemon import CoinDaemon
from Wallet import Wallet
from Constants import Constants as cnt

class CoinWizard:
    """Requires the name and port of the coin daemon to manage. This
    object creates Wallets from the wallet files found in the coin
    directory and provides a variety of methods including displaying the
    total BTC value of the coins collected"""

    # Total balance of coins processed
    wizardBalance = 0.0

    # Estimated BTC value of the coins processed
    wizardBTCValue = 0.0

    # Name of the coin daemon to manage
    # Ex. "dogecoin"
    wizardName = ""

    # RPC API port
    # Ex. 22555
    wizardPort = 00000

    # Coin name ticker
    # Ex. "DOGE"
    wizardTicker = ""

    # List of Wallets to process
    walletList = []

    # Address to dump coins to
    wizardAddress = ""

    WALLET_STORE = ""

    def __init__(self, a_str, b_int, c_str, d_lst):
        self.wizardName = a_str
        self.wizardPort = b_int
        self.wizardTicker = c_str
        self.wizardAddress = d_lst

        self.wizardBalance = self.get_balance()
        self.wizardBTCValue = self.get_BTC_value()
        self.WALLET_STORE = cnt.GOOD_WALLET_DIR + self.wizardName + "/store/"

    def format_int(self, a_int, b_int):
        return '%0*d' % (a_int, b_int)

    def check_for_more(self):
        """Method that checks for new coin wallets in the inbound wallet
        directory, also discards of any empty or encrypted wallets"""

        import os, shutil, time

        newWalletList = []

        os.chdir(cnt.GOOD_WALLET_DIR + self.wizardName)

        newWalletListing = os.listdir(os.getcwd())

        for x in range(0, len(newWalletListing)):
            if not(os.path.isdir(newWalletListing[x])):
                print(os.path.abspath(newWalletListing[x]))

                newWalletList.append(Wallet(os.path.basename(newWalletListing[x]), x, self.wizardPort, self.wizardName))

        for x in range(0, len(newWalletList)):
            result = newWalletList[x].test_wallet()

            # Empty wallet
            if(result == 0):
                os.remove(newWalletList[x].walletPath)
                print("[LOG] EMPTY " + self.wizardTicker + " - " + newWalletList[x].walletPath + " DELETED")

            # Unlocked nonempty wallet
            elif(result == 1):
                shutil.copy(newWalletList[x].walletPath, self.WALLET_STORE)
                os.remove(newWalletList[x].walletPath)
                print("[LOG] GOOD " + str(newWalletList[x].walletBalance) + " " + self.wizardTicker + " - " + newWalletList[x].walletPath + " STORED")

            # Locked wallet
            elif(result == 2):
                shutil.copy(newWalletList[x].walletPath, cnt.LOCKED_WALLET_DIR + self.wizardName + "/" + newWalletList[x].walletPath)
                os.remove(newWalletList[x].walletPath)
                print("[LOG] LOCKED " + str(newWalletList[x].walletBalance) + " " + self.wizardTicker + " - " + newWalletList[x].walletPath + " MOVED")


    def get_balance(self):
        """Loops through each Wallet in the walletList and tallies the
        total balance"""

        return 1

        #~ import os
        #~ walletFileList = []
        #~ print(self.WALLET_STORE)
        #~ os.chdir(self.WALLET_STORE)
        #~ walletFileList = os.listdir(os.getcwd())
        #~ for x in range(0, len(walletFileList)):
            #~ if not(os.path.isdir(walletFileList[x])):
                #~ print(os.path.basename(walletFileList[x]))

                #~ self.walletList.append(Wallet(os.path.basename(walletFileList[x]), x, self.wizardPort, self.wizardName))

    def get_BTC_value(self):
        """Returns the BTC value of the total amount of coins
        processed"""

        import urllib2, json

        if(self.wizardName == 'bitcoin'):
            return self.wizardBalance * 1
        else:
            API_CALL = 'last_price'
            API_COIN = self.wizardTicker
            API_URL = "https://api.mintpal.com/market/stats/" + API_COIN + "/BTC.json"

            APIResponse = urllib2.urlopen(API_URL)
            jsonData = json.load(APIResponse)

            return self.wizardBalance * float(jsonData[0]['last_price'])

    def print_summary(self, highscore=True):
        print("| Wizard name: " + self.wizardName + " (" + self.wizardTicker + ")")
        print("| Wizard port: " + self.wizardPort)
        print("| Wizard balance: " + str(self.wizardBalance) + " " + self.wizardTicker)
        print("| Wizard BTC value: " + str(self.wizardBTCValue))
        print("| Wizard address: " + self.wizardAddress)
