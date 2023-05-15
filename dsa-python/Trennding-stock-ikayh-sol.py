from collections import defaultdict
from typing import OrderedDict


class TrendingStock:

    def __init__(self):
        self.stocksFreq = {}
        self.maxFreq = 0
        self.freqStocks = defaultdict(dict)

    def processStock(self, stock):
        if stock not in self.stocksFreq:
            self.stocksFreq[stock] = 1
            self.freqStocks[1][stock] = stock
        else:
            freq = self.stocksFreq.get(stock)
            self.freqStocks[freq].pop(stock)

            # update freq
            freq += 1
            self.maxFreq = max(self.maxFreq, freq)
            # insert new freq
            self.stocksFreq[stock] = freq
            self.freqStocks[freq][stock] = stock

    def getTrendingStock(self):
        id, stock = self.freqStocks[self.maxFreq].popitem()
        self.stocksFreq[stock] -= 1
        stockFreq = self.stocksFreq[stock]

        if stockFreq != 0:
            self.freqStocks[stockFreq][stock] = stock
        else:
            del self.stocksFreq[stock]

        # update maxFreq
        if not self.freqStocks[self.maxFreq]:
            self.maxFreq -= 1

        return stock


t = TrendingStock()
t.processStock('TSLA')
t.processStock('APPL')
t.processStock('TSLA')
t.processStock('APPL')
t.processStock('NTFX')
t.processStock('TSLA')
print(t.freqStocks)
print(t.stocksFreq)

print(t.getTrendingStock())
print(t.getTrendingStock())
print(t.getTrendingStock())
print(t.freqStocks)
print(t.stocksFreq)
