import sys

def initial_slambook():
    row, cols = int(input("Please enter a number of your choosing:")), 5
    
    slam_book = []
    print(slam_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):" % (i+1))
        print("NOTE: * indicated mandatory fields")
        print ("...............................................")
        temp = []
        for j in range(cols):
            
            if j == 0:
                temp.append(str(input("Enter your name": ")))
                if temp[j] == '' or temp[j] == '':
                
                temp[j] = Noneif j ==4:
                temp.append(str(input("Enter category(Family/Friends/Work/Others):")))
                
                if temp[j] == "" or temp[j] == '':
                temp[j] = None
                slam_book.append(temp)
                
                print(slam_book)
                return slam_book
                def menu():
                
                print("........................................")