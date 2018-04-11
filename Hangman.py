
def hangman(word):
    wrong=0
    stages = ["",
              "________               ",
              "|                      ",
              "|        |             ",
              "|        0             ",
              "|       /|\            ",
              "|       / \            ",
              "|                      "]
    word_letters = list(word)
    board=["_"]*len(word)
    win=False
    print("Welcome to Hangman")

    while wrong < len(stages)-1:
        print("\n")
        guess= input("Guess a letter:")
        if guess in word_letters:
            index_pismene=word_letters.index(guess)
            board[index_pismene]=guess
            word_letters[index_pismene]="$"
        else: wrong+=1
        print((" ".join(board)))
        e= wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win")
            print(" ".join(board))
            win = True
            break

hangman("cat")
