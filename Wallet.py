#!/usr/bin/python
from Constants import Constants as cnt
from CoinDaemon import CoinDaemon
from bitcoinrpc.authproxy import AuthServiceProxy

class Wallet:
    """Provides a high-level abstraction of a coin wallet and simplifies
    the process of making JSON API RPC calls to the coin wallet
    daemon"""

    walletPath = ""
    walletName = ""
    walletNumber = 0
    walletNumberStr = '%0*d' % (6, walletNumber)
    walletPort = 00000
    walletBalance = 0.0
    walletProxy = None

    def __init__(self, a_str, b_int, c_int, d_str):
        self.walletPath = a_str
        self.walletNumber = b_int
        self.walletPort = c_int
        self.walletName = d_str

    def get_balance(self):
        return self.daemonAPI.getbalance()

    def test_wallet(self):
        """Function that tests the wallet and returns an int depending
        on the result"""

        import os, shutil, time, socket
        from bitcoinrpc.authproxy import JSONRPCException

        copyPath = cnt.HOME_DIR + "." + self.walletName + "/wallet.dat"

        shutil.copy(self.walletPath, copyPath)

        theDaemon = CoinDaemon(self.walletName, self.walletPort, self.walletPath)
        COMMAND = cnt.SCRIPT_DIR + "bin/" + self.walletName + " getbalance"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        daemonTimer = 0
        RPCTimer = 0

        while(theDaemon.is_running()):
            print("[LOG] Waited " + str(daemonTimer) + " seconds for " + self.walletName + " daemon to stop...")
            daemonTimer = daemonTimer + 1
            time.sleep(1)
        else:
            theDaemon.start_daemon()

        while not(sock.connect_ex(('localhost', int(self.walletPort))) == 0):
            print("[LOG] Waited " + str(RPCTimer) + " seconds for RPC API...")
            RPCTimer = RPCTimer + 10
            time.sleep(10)
        else:
            self.walletProxy = AuthServiceProxy("http://" + cnt.USER + ":" + cnt.PASSWORD + "@127.0.0.1:" + self.walletPort)
            print("[LOG] RPC API Up!")

            self.walletBalance = self.walletProxy.getbalance()

            if(self.walletBalance == 0):
                #~ print("[LOG] Wallet tested - " + self.walletPath + " - EMPTY")
                theDaemon.stop_daemon()
                return 0
            else:
                try:
                    print(self.walletProxy.keypoolrefill())
                except JSONRPCException:
                    #~ print("[LOG] LOCKED Wallet tested - " + self.walletPath + " - balance: " + str(self.walletBalance))
                    theDaemon.stop_daemon()
                    return 2
                else:
                    #~ print("[LOG] Wallet tested - " + self.walletPath + " - balance: " + str(self.walletBalance))
                    theDaemon.stop_daemon()
                    return 1

