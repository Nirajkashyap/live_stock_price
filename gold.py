import re
import urllib
import string
ur = urllib.urlopen('http://www.exchangerates.org.uk/commodities/live-gold-prices/XAU-EUR.html')
#print ur.read()

html = ur.read()

str1 = re.search("value_XAUEUR",html,re.I)

if str1 :
    #print 'ya-----'
    #print str1.group()
    index_val =  html.index("value_XAUEUR")
    index_val_update = index_val + 14
    #print index_val_update
    index_val_update_end = index_val + 23
    #print index_val_update_end
    print html[index_val_update : index_val_update_end ]
    
    
else :
    print 'no'
