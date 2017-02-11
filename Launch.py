#!/usr/bin/python
from CoinScript import CoinScript
from Constants import Constants as cnt

# Launch(.py)
# .--=
# | Creates and launches the CoinScript which creates CoinWizards for
# | each supported coin in a file that is passed in to the object
# | constructor
#  ----=
# CoinScript(.py)
# .--=
# | Requires a space seperated list of the coin name and coin port which
# | is used to create a list of CoinWizards that  are responsible for
# | managing each coin daemon
#  ----=
# CoinWizard(.py)
# .--=
# | Requires the name and port of the coin daemon to manage. This object
# | creates Wallets from the wallet files found in the coin directory
# | and provides a variety of methods including displaying the total BTC
# | value of the coins
#  ----=
# Wallet(.py)
# .--=
# | Provides a high-level abstraction of a coin wallet and simplifies
# | the process of making JSON API RPC calls to the coin wallet daemon
#  ----=

theScript = CoinScript(cnt.COIN_LIST_PATH)
theScript.read_coin_list()
theScript.sort_coins()
theScript.spawn_wizards()
theScript.summon_wizards()
