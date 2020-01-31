box =  ['_','_','_','_','_','_',' ',' ',' '] #this variable is used to create the matrix for the game
position_filled = [1]
def print_matrix():
    print (box)
    for index, item in enumerate(box, start=1):
        print(item, end='|' if index % 3 else '\n')
print("Hello Players ('|') Lets Play")



def p1():
    print("Hello Player1")
    i = int(input("Player1 Enter the box number from 1 to 9 "))
    c1(i)
    #chara = 'X'
    #update_a(a, i, chara)
    print_matrix()


def c1(i):
    if i in position_filled:
        print("Already entered")
        p1()

    else:
        position_filled.append(i)
        box[i-1] = 'X'


print_matrix()
p1()