import time
import re
import csv
from imap_tools import MailBox, AND
import requests
import json
from config import REPORT,REPORT_ENDPOINT,MAIL_ADDRESS,MAIL_PASS,IMAP_SERVER


csvFile = "./helper/SCANNERS_LIST.csv"

#### FOR READ CONFIG ####
def csvReader(ticker):
    # coin list to be signaled 
    # for trade security
    with open(csvFile) as csvFL:
        csvText = csv.reader(csvFL, delimiter=',')
        lineCount = 0
        for row in csvText:
            if lineCount == 0:
                lineCount += 1
            else:
                lineCount += 1
                csvTicker = str(row[0])
                if csvTicker == ticker:
                    return str(row[1])
        return ""

#### GET ALL SCANNING MAILS ####
def main():
    firstLoop = True # ignore old mails
    print("\nINFO: Waiting for old signals..")
    while True:
        try:
            symbolList = []
            with MailBox(IMAP_SERVER).login(MAIL_ADDRESS, MAIL_PASS, 'INBOX') as mailbox:
                
                # get unseen emails from INBOX folder
                for msg in mailbox.fetch(AND(seen=False)):
                    #print(msg.date,msg.from_) # for testing
                    if firstLoop == True:
                        continue

                    allText = msg.html.split(" ")
                    for tx in allText:
                        ticker = re.findall("BINANCE:.+",tx)
                        
                        if ticker:
                            ticker = str(ticker[0]).split("<")[0]
                            ticker = ticker.split(":")[1]
                            
                            # if the coin name is unknown 
                            orderTicker = csvReader(ticker)
                            if (orderTicker != ""):
                                symbolList.append(orderTicker)

            if symbolList != []:
                for symbol in symbolList:
                    now = int(time.time())
                    packed = {"ticker": symbol,"updateTime": now}
                    print("INFO: New signal received. Symbol: {}".format(symbol))
                    if REPORT == True:
                        try:
                            packed = json.dumps(packed)
                            requests.post(REPORT_ENDPOINT,packed)
                        except:
                            print("\nALERT: Request failed..")
        except:
            pass
        if firstLoop == True:
            print("\nINFO: Process Active. Ready for signals")        
        firstLoop = False
        time.sleep(10)

if (__name__ == "__main__"):
    if (MAIL_ADDRESS != "") and (MAIL_PASS != "") and (IMAP_SERVER != ""):
        main()
    else:
        print("\nALERT: Fill in the account to be connected in the config file")
