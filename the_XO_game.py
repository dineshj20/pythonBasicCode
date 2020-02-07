class main:
    box =  ['_','_','_','_','_','_',' ',' ',' '] #this variable is used to create the matrix for the game
    position_filled = []
    player1 = 0
    player2 = 0
m1 = main()
def print_matrix():
    print (m1.box)
    for index, item in enumerate(m1.box, start=1):
        print(item, end='|' if index % 3 else '\n')
    return(m1.box)
print("Hello Players ('|') Lets Play")

def p1():
    while m1.player1 < 1:
        print("Hello Player1")
        i = int(input("Player1 Enter the box number from 1 to 9 "))
        c1(i)
    #chara = 'X'
    #update_a(a, i, chara)
    print_matrix()

def p2():
    while m1.player2 < 1:
        print("Hello Player2")
        i = int(input("Player2 Enter the box number from 1 to 9 "))
        c2(i)
    #chara = 'X'
    #update_a(a, i, chara)
    print_matrix()

def c1(i):
    if i in m1.position_filled:
        print("Already entered")
    else:
        m1.position_filled.append(i)
        m1.box[i-1] = 'X'
        m1.player1 = 2


def c2(i):
    if i in m1.position_filled:
        print("Already entered")

    else:
        m1.position_filled.append(i)
        m1.box[i-1] = 'O'
        m1.player2 = 2


print_matrix()
p1()
p2()