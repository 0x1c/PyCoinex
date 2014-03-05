import urllib
import urllib2
import json
import time
import hmac,hashlib
import pprint

class Coinex:
    def __init__(self, APIKey, APISecret):
        self.APIKey = APIKey
        self.APISecret = APISecret
        # Required to bypass Cloudflare 403
        self.UserAgent = "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"

    def api_query(self, method, req={}):

        req['method'] = method
        post_data = urllib.urlencode(req)

        # PUBLIC
        if(method == "currencies" or method == "trade_pairs"):
            headers = {
                'Content-Type': 'application/json',
                'User-Agent': self.UserAgent,
            }
            url = "https://coinex.pw/api/v2/%s" % method
            ret = urllib2.urlopen(urllib2.Request(url, None, headers))
            jsonRet = json.loads(ret.read())
            return jsonRet

        # PRIVATE
        if(method == "balances" or method.find("own") != -1):
            sign = hmac.new(self.APISecret, None, hashlib.sha512).hexdigest()
            headers = {
                'Content-Type': 'application/json',
                'User-Agent': self.UserAgent,
                'API-Sign': sign,
                'API-Key': self.APIKey
            }
            url = "https://coinex.pw/api/v2/%s" % method
            print "[-] %s" % url
            ret = urllib2.urlopen(urllib2.Request(url, None, headers))
            jsonRet = json.loads(ret.read())
            return jsonRet


    def getCurrencies(self):
        return self.api_query("currencies")

    def getTradePairs(self):
        return self.api_query("trade_pairs")

    def getBalances(self):
        return self.api_query("balances")

    def getOpenOrders(self):
        return self.api_query("orders/own")

