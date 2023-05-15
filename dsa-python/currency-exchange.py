"""
    Question summary
    1. Given a list of strings separated by "|" where string contains banks, currPair and exchage rate:
    Design a class with the the following functions:
    - "add currencty pair" takes params of  (strings)(if currency exist, increment exisiting rate and count else add new curPair)
    - get average of of all currency pair (return type: list or dict)-------> hint(average = totalRate/currFreq)

    strings = ["1|eurusd|1.3", "1|eurusd|1.4", "2|eurgbp|1.1", "3|usdgbp|0.8", "2|eurusd|1.2", "3|eurusd|1.5", "2|eurgbp|1.3", "1|eurusd|1.5"]

    expected output ---> {'eurusd': 1.4, 'eurgbp': 1.3, 'usdgbp': 0.8}
"""
"""
    bank = {1:{eurusd:1.4}, 1:{eurusd:1.3}}
    bank,currPair,rate = 1,eurusd,1.3
    currency = {eurusd: [1.4,2],}
    curs,count = 1.4,2

    average = {eurusd:2.65}
"""




from collections import defaultdict
class Exchange:
    def __init__(self):
        self.banks = defaultdict(dict)
        self.currency = {}
        self.average = {}

    def addPair(self, bankInfo):
        bankInfo = bankInfo.split("|")
        bank, currPair, currRate = bankInfo

        # covert bankRate from string to float
        currRate = float(currRate)

        # check if currency already exists in bank
        if bank in self.banks and currPair in self.banks[bank]:
            # remove former rate and decrement count in currency store
            prevRate = self.banks[bank][currPair]
            self.currency[currPair][0] -= prevRate
            self.currency[currPair][1] -= 1

        # insert/update into bank store
        self.banks[bank][currPair] = currRate

        # insert currency, its rate and freq in curreny store
        if currPair not in self.currency:
            self.currency[currPair] = [currRate, 1]
        else:
            self.currency[currPair][0] += currRate
            self.currency[currPair][1] += 1

        # get currency pair average
        totalRate, totalCurr = self.currency[currPair]
        currPairAverage = round(totalRate/totalCurr, 2)

        # update currncy pair average
        self.average[currPair] = currPairAverage

    def getAverage(self):
        return self.average


obj = Exchange()
strings = ["1|eurusd|1.3", "1|eurusd|1.4", "2|eurgbp|1.1", "3|usdgbp|0.8",
           "2|eurusd|1.2", "3|eurusd|1.5", "2|eurgbp|1.3", "1|eurusd|1.5"]
for string in strings:
    obj.addPair(string)
print(obj.banks)
print(obj.currency)
print(obj.getAverage())
