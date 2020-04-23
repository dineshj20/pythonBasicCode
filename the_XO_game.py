class main:
    box =  ['_','_','_','_','_','_',' ',' ',' '] #this variable is used to create the matrix for the game
    box2 = [1,2,3,4,5,6,7,8,9]
    position_filled = [0,0,0,0,0,0,0,0,0] #this variable will help in to know which position is filled in the 3 X 3 matrix
    player1 = 0 #to take input from player 1
    player2 = 0 #to take input from player 2
    count = 0
    player1_name = "Dinesh"
    player2_name = "Samruddhi"
    temp_list = [0,0,0,0,0,0,0,0,0]
m1 = main()

def print_matrix():
    for index, item in enumerate(m1.box, start=1):
        print(item, end='|' if index % 3 else '\n')
    return(m1.box)
print("Hello Players ('|') Lets Play")



def check_win(a):
    c1 = (m1.box2[0] == m1.box2[1] == m1.box2[2]) 
    c2 = (m1.box2[3] == m1.box2[4] == m1.box2[5])
    c3 = (m1.box2[6] == m1.box2[7] == m1.box2[8])
    r1 = (m1.box[0] == m1.box2[3] == m1.box2[6])
    r2 = (m1.box[1] == m1.box2[4] == m1.box2[7])
    r3 = (m1.box[2] == m1.box2[5] == m1.box2[8])
    d1 = (m1.box[0] == m1.box2[4] == m1.box2[8]) 
    d2 = (m1.box[6] == m1.box2[4] == m1.box2[2])
    if c1 or c2 or c3 or r1 or r2 or r3 or d1 or d2:
        return 0
        
def players_input(): #here we take the input of player1 and check whether the place is empty or is the input correct
    i = 0
    while m1.count in range(0,9):
        try:
            if m1.count % 2 == 0:
                temp = 0
                while temp == 0:
                    i = int(input(m1.player1_name+ " Please select empty place to play your turn\n"))
                    if m1.position_filled[i-1] == i:
                        pass
                    else:
                        m1.box[i-1] = 'x'
                        m1.box2[i-1] = 'x'
                        m1.position_filled[i-1] = i
                        temp = 1
                        if m1.count > 3:
                            if check_win(i) == 0:
                                print(m1.player1_name+ " You win")
                                print_matrix()
                                m1.count = 10
                                #temp = 1
                                break
                        print_matrix()
            else:
                temp = 0
                while temp == 0:
                    i = int(input(m1.player2_name+ " Please select empty place to play your turn\n"))
                    if m1.position_filled[i-1] == i:
                        pass
                    else:
                        m1.box[i-1] = 'o'
                        m1.box2[i-1] = 'o'
                        m1.position_filled[i-1] = i
                        temp = 1
                        if m1.count > 3:
                            if check_win(i) == 0:
                                print(m1.player2_name+ " You win")
                                m1.count = 10
                                temp = 1
                                break
                        print_matrix()
            m1.count += 1
            #print(m1.count)
        except ValueError:
            print ("wooow that was not a number:(")
        except IndexError:
            print ("wooow that was not in range:(")


print_matrix()
players_input()