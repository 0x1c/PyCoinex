import Coinex

class CoinexTest:
    def __init__(self):
        self.nothing = None
        # Coinex private key / API key
        private_key = 'XXX'
        api_key = 'XXX'
        self.exchange = Coinex.Coinex(private_key,api_key)
        self.trade_pairs = {}
        self.last_price = {}
        self.currencies = {}
        self.total_value = 0
        self.btc_only = True

    def getCurrencies(self):
        print "[-] Getting currencies"
        data = self.exchange.getCurrencies()
        for k in data['currencies']:
            self.currencies[k['id']] = k['name']

    def getTradePairs(self):
        print "[-] Getting trade pairs"
        data = self.exchange.getTradePairs()
        for k in data['trade_pairs']:
            if (self.btc_only == True and k['url_slug'].find("_btc") != -1):
                last_price = "%0.8f" % (float(k['last_price'])/100000000)
                self.trade_pairs[k['id']] = k['url_slug']
                self.last_price[k['currency_id']] = last_price


    def printBalances(self):
        print "[-] Getting balances"
        data = self.exchange.getBalances()
        for k in data['balances']:
            ticker = k['currency_name']
            amount = "%0.8f" % (float(k['amount'])/100000000)
            print "%s\t%s" % (ticker, amount)

    def printOpenOrders(self):
        print "[-] Getting open orders"
        data = self.exchange.getOpenOrders()
        print "Pair\t\tAmount\tRate"
        for k in data['orders']:
            trade_pair = self.trade_pairs[k['trade_pair_id']]
            amount = "%0.8f" % (float(k['amount'])/100000000)
            rate = "%0.8f" % (float(k['rate'])/100000000)
            print "%s\t\t%s\t%s" % (trade_pair, amount,rate)

    def printValue(self):
        print "[-] Getting balances"
        data = self.exchange.getBalances()
        for k in data['balances']:
            ticker = k['currency_name']
            amount = "%0.4f" % (float(k['amount'])/100000000)
            try:
                if ticker == "BTC":
                    value_in_btc = "%0.8f" % (float(amount))
                    last_price = "%0.8f" % 1
                else:
                    value_in_btc ="%0.8f" % ( float(last_price) * float(amount))
                    last_price = "%0.8f" % (float(self.last_price[k['currency_id']]))
                self.total_value = self.total_value + float(value_in_btc)
            except:
                last_price = "FAIL"
                value_in_btc = "FAIL"
            print "%s\t%s\t%s\t%s" % (ticker, amount, last_price, value_in_btc)
        print "==================================="
        print "Total value in BTC: %s" % self.total_value
        print "==================================="

def main():
    c = CoinexTest()
    c.getTradePairs()
    c.getCurrencies()
    c.printBalances()
    c.printOpenOrders()
    c.printValue()

if __name__ == "__main__":
    main()
