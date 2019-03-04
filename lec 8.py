#quiz


x = 1
def test():
    x = 2
test()
print(x) #1


x = 1
def test():
    global x
    x = 2
test()
print(x) #2


x = [1]
def test():
    x = [2]
test()
print(x) #[1]


x = [1]
def test():
    global x
    x = [2]
test()
print(x) #[2]


x = [1]
def test():
    x[0] = 2
test()
print(x)#[2]




game=[[0,0,0],
      [0,0,0],
      [0,0,0]]


def game_board(game_varible,player=0,row=0,col=0,just_print=False):

    print("  a   b   c")
    if not just_print:
        game_varible[row][col]=player

    for count,abc in enumerate(game):
        print(count, abc)



game_board(game,1,1,1)


