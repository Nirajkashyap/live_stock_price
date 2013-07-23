import re
import urllib
import string
ur = urllib.urlopen('http://www.exchangerates.org.uk/commodities/live-silver-prices/XAG-EUR.html')
#print ur.read()

html = ur.read()

str1 = re.search("value_XAGEUR",html,re.I)

if str1 :
    
    index_val =  html.index("value_XAGEUR")
    index_val_update = index_val + 14
    
    index_val_update_end = index_val + 22
    
    print html[index_val_update : index_val_update_end ]
    
    
else :
    print 'no live value'
