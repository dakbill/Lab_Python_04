groceries=['bananas','strawberries','apples','bread']
out="Original list"
for good in groceries:
    out+=", "+good
print out
print "********************************************************"
groceries.append("champagne")
out="Celebratory list"
for good in groceries:
    out+=", "+good
print out
print "*********************************************************"
groceries.remove("bread")
out="Poor John hates bread but likes "
for good in groceries:
    out+=", "+good
print out
print "*********************************************************"
#out="Sorted list is "
groceries.sort()
for item in groceries:
    s=list(item)
    print 'For '+item+' go to'+str(s[0:1])
print "*********************************************************"
