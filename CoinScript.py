#!/usr/bin/python
from CoinWizard import CoinWizard
from Constants import Constants as cnt

class CoinScript:
    """Requires a space seperated list of the coin name, coin port, coin
    ticker symbol, and coin addresses which is used to create a list of
    CoinWizards that  are responsible for managing each coin daemon"""

    # Path to the coin list
    coinListPath = ""

    # List that contains information that is used to create CoinWizards
    coinList = []

    # List that contains CoinWizards for the CoinScript to manage
    wizardList = []

    def __init__(self, a_str):
        """CoinScript constructor, takes in a single string which is the
        path to the coin list"""

        self.coinListPath = a_str

    def generate_id(string_length=10):
        """Returns a random string of length string_length."""

        import uuid

        random = str(uuid.uuid4())
        random = random.upper()
        random = random.replace("-","")
        return random

    def sort_coins(self):
        """Method that is called upon creation that checks the inbound
        wallet directory for new wallets and sorts the coins into the
        appropriate coin folder for processing by the CoinWizard"""

        import os, shutil

        os.chdir(cnt.NEW_WALLET_DIR)

        newWalletDirList = os.listdir(os.getcwd())

        for x in range(0, len(newWalletDirList)):
            os.chdir(newWalletDirList[x])

            print(os.getcwd())

            newWalletList = os.listdir(os.getcwd())

            for y in range(0, len(newWalletList)):
                print("\_" + newWalletList[y])
                coinName = newWalletList[y].split('_')[0].lower()
                print("  \_" + coinName)

                for z in range(0, len(self.coinList)):
                    if(coinName == self.coinList[z].split()[0]):
                        print(coinName)
                        randomStr = self.generate_id()
                        copyPath = cnt.GOOD_WALLET_DIR + coinName + "/" + randomStr + ".dat"
                        open(copyPath, 'a').close()
                        shutil.copyfile(newWalletList[y], copyPath)

            os.chdir(cnt.NEW_WALLET_DIR)
            shutil.move(newWalletDirList[x], cnt.OLD_WALLET_DIR)

    def read_coin_list(self):
        """Reads the coin list that was passed to the CoinScript upon
        creation and writes it to the coinList object"""

        with open(self.coinListPath) as theCoinList:
            self.coinList = theCoinList.read().splitlines()

    def spawn_wizards(self):
        """Reads the coinList object and appends a new CoinWizard to the
        wizardList"""

        wizardName = ""
        wizardPort = 00000

        for x in range(0, len(self.coinList)):
            wizardName = self.coinList[x].split()[0]
            wizardPort = self.coinList[x].split()[1]
            wizardTicker = self.coinList[x].split()[2]
            wizardAddress = self.coinList[x].split()[3]

            self.wizardList.append(CoinWizard(wizardName, wizardPort,
                wizardTicker, wizardAddress))

    def summon_wizards(self):
        """Prints out a summary of each CoinWizard in the wizardList"""

        for x in range(0, len(self.wizardList)):
            print(".------- WIZARD NO. " +
                '%0*d' % (3, x) + " -------=")
            self.wizardList[x].print_summary()
            print(" --------------------=")

            self.wizardList[x].check_for_more()
