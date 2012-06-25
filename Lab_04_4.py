#List in a dictionary where items in the list represent respective prices

bill= range(5)    
def bin_ins(item,list_of_prices):
        lb=0
        ub=len(list_of_prices)
        while lb<=ub:
            mid=(ub+lb)/2
            if(item>=list_of_prices[mid] and item<=list_of_prices[mid+1]):
                pos=mid+1
                break
            elif(item>list_of_prices[mid]):
                lb=mid+1
            elif(item<list_of_prices[mid]):
                    ub=mid-1
            else:
                break
        list_of_prices.insert(pos,item)
        return list_of_prices
print bin_ins(3.5,bill)
groceries=['Apples     ','Bananas    ','Bread     ','Carrots ','Champagne   ','Strawberries']
stock={'Apples     ':[7.3,6.8],'Bananas    ':[5.5,6.5],'Bread     ':[1.0,2.0],'Carrots ':[10.0,11.0],'Champagne   ':[20.90,17.5],'Strawberries':[32.6,29.0]}
def min_cost(item_list,stock_list):
        out=[]
        for item in item_list:
                if(stock_list[item][0]<stock_list[item][1]):
                        store_num=1
                else:
                        store_num=2
                out.append(store_num)
        return out
save_money=min_cost(groceries,stock)
print save_money
i=0
for item in groceries:
        print 'For '+item+' go to store ' +str(save_money[i])
        i+=1
