import random
def game():
    score = random.randint(1, 100)

    with open("CHAPTER 9/PRACTICE SET/high-score.txt", "r") as f:
        high_score = f.read()
        if(high_score !=""):
            high_score = int(high_score)
        else:
            high_score = 0

    print("Your score is: ", score)
    if(score > high_score):
        print("You have just broken the high score!")
        with open("CHAPTER 9/PRACTICE SET/high-score.txt", "w") as f:
            f.write(str(score))

    return score

game()
