# PyCoinex

This is a partially implemented Coinex [http://coinex.pw/][1] API in Python. I just wanted 
open trades, balances, and total value in BTC in one easy place. Add your
Coinex API key and private key to example.py and run as below. The CoinEx
developer has a more full API written in CoffeeScript [2][https://gist.github.com/erundook/83772222], which is also
useful if you want to extend this in any way. Feel free to send me pull
requests, otherwise do with this whatever thou wily^Ht.

```
PyCoinex$ python example.py 
[-] Getting trade pairs
[-] Getting currencies
[-] Getting balances
[-] https://coinex.pw/api/v2/balances
BTC	0.31123318
MNC	0.00000000
ZET	0.00000000
WDC	0.00000000
PXC	0.00000000
MOON	0.00000000
GLD	0.00000000
DOGE	0.00000000
CTM	0.00000000
SMC	0.00000000
[-] Getting open orders
[-] https://coinex.pw/api/v2/orders/own
Pair		Amount	Rate
pxc_btc		4990.00000000	0.00001320
wdc_btc		9.98000000	0.00020988
[-] Getting balances
[-] https://coinex.pw/api/v2/balances
BTC	0.3112	1.00000000	0.31120000
MNC	0.0000	0.00045502	0.00000000
ZET	0.0000	0.00001180	0.00000000
WDC	0.0000	0.00013488	0.00000000
PXC	0.0000	0.00000525	0.00000000
MOON	0.0000	0.00000002	0.00000000
GLD	0.0000	0.00002100	0.00000000
DOGE	0.0000	0.00000157	0.00000000
CTM	0.0000	0.00000001	0.00000000
SMC	0.0000	0.00001761	0.00000000
===================================
Total value in BTC: 0.3112
===================================
```


