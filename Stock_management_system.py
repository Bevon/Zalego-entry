from os import sys
def EnterNewStock(filename):
    
    itemName = ''
    itemPrice = 0
    stockCount = int(raw_input("Enter the number of items you wish to Stock: "))
    itemNumber = 0
    QuantityOfItemSold = 0
    QuantityRemaining = 0
    
        
    with open(filename, 'w') as items:
        QuantityRemaining = stockCount - QuantityOfItemSold
        
        while itemNumber != stockCount:
            itemName = raw_input("Enter name of the new item: ")
            itemPrice = raw_input("Enter price of the new item: ")
            QuantityOfItemSold = raw_input("Enter the number of item sold ")
        
            
            if itemNumber != stockCount:
                items.write("name = " + str(itemName) + '\t\t' + "price = " + str(itemPrice)+ 't\t' +
                            "Quantity =" + str(stockCount) + '\t\t' + "Quantity Sold= " + str(QuantityOfItemSold) +
                            '\t\t' + "Quantity Remaining= " + str(QuantityRemaining)+'\n\n')
                itemNumber += 1
            elif itemNumber == stockCount:
                print "All the data is stored"
                break
                
def availableStock(filename):
    with open(filename) as items:
        for line in items:
            print(str(line))

def main():

    finished = False

    while not finished:
        command = raw_input('Save(S), Load(L), Quit(Q): ')

        if command == 'S' or command == 's':
            EnterNewStock(raw_input("Enter data file type to store stock data: "))
        elif command == 'L' or command =='l':
            availableStock(raw_input("Enter file name to retrieve data: "))
        elif command == 'Q' or command == 'q':
            finished = True

    
if __name__ == '__main__':
    main()

    
                
                               
                

    
                

                
                
                            
                
            
            
            
            
