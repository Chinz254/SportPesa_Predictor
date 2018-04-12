import random
def bounty_hunter():
    n = 0
    while n <= 12:
        def game_predictor():
            rng = random.Random()
            number = rng.randrange(1,4)
            if number == 1:
                return "X"
            elif number == 2:
                return "1"
            else:
                return "2"

        predicted_no = game_predictor()

        print(predicted_no, end= " ")
        n += 1
bounty_hunter()
