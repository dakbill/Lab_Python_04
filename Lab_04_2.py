#Dictionary  so the stock can be modified and also located easily

stock={'Apples     ':7.3,'Bananas    ':5.5,'Bread     ':1.0,'Carrots ':10.0,'Champagne   ':20.90,'Strawberries':32.6}
###############################################
print "Initially:"
print "Item\t\t|\tPrice"
print "---------------------------------"
for i in stock.viewkeys():
    print i+"\t|\t"+str(stock[i])
###############################################
print "#############################################"
stock['Strawberries']=63.43
print "During winter:"
print "Item\t\t|\tPrice"
print "---------------------------------"
for i in stock.viewkeys():
    print i+"\t|\t"+str(stock[i])
###############################################
print "#############################################"
stock['Chicken  ']=6.5
print "Chicken came then"
print "Item\t\t|\tPrice"
print "---------------------------------"
for i in stock.viewkeys():
    print i+"\t|\t"+str(stock[i])
###############################################
print "#############################################"
#List of all foods in stock
print 'Shoprite got in stock:'
for stock in in_stock:
    print stock
###############################################
print "#############################################"
tup=()
tup+=tuple(in_stock)
print "We always have in stock:"
print tup

