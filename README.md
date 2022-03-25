# tradingview-crypto-follower-mail-parser
It receives new follower signals from Tradingview to its e-mail address and extracts which crypto currency name is written. Script can optionally send coin name to an entpoint.

<br>

## Summary

<br>

#### Config

Config file have account ID, password and IMAP_SERVER settings. You have to make those setting before running. 

Thoroughly tested on Gmail.

<br>

#### Send new signals to an endpoint

Config file have report coins endpoint. If you complete this setting, you can send the incoming signal to a process located on another server. 

<br>

#### Scanner List

Script have a coin list file and config file. SCANNERS_LIST contains the coin names that it will parse from the coin list and the names it will print cleanly after parsing.

The SCANNERS_LIST should be updated frequently according to new coins entering the market. 

You can add the new symbols in list you want to add. By default, it is set according to the Binance Futures cryptocurrency list.

<br><br>

## Run

Firstly, before run the app.py, install the requirements

`pip install -r requirements.txt`

Secondly, make sure you have completed the settings in the config file. 

If you have completed all the requirements you can simply run the app.py file with this command:

`python app.py`

<br><br><br>



