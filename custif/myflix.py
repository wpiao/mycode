#!/usr/bin/env python3

heros = ["Iron man", "Wanda", "Vision", "Captain America", "Falcon", "Ant man", "Hulk", "Thor", "Hawk eye", "Spider man", "Black widow", "Doctor strange"]

answers = ["Iron man", "Captain America", "Spider Man"]

chance = 6

while chance:
    first = input(f"Guess my favorite Marvel heros in the following options. {heros}.\n> ").lower()
    if first == answers[0].lower():
        print(f"Correct! My favorite marvel hero is {first.title()}!")
        while chance:
            second = input(f"You still have {chance} chances left, so please guess my second favorite marvel hero.\n> ").lower()
            chance = chance - 1
            if second == answers[1].lower():
                print(f"Congratulations! You got it right. My favorite marvel hero is {first.title()} and my second favorite is {second.title()}!")
                break
            elif chance: 
                print(f"Wrong! Try gussing my second favorite again. You have {chance} chance left!\n")
            else:
                print(f"My second favorite mavel hero is {answers[1]}")
        break
    else:
        chance = chance - 1
        print(f"Wrong! Try again, you have {chance} chances left!\n")

print(f"Great job on guessing whethere you got it right or not. My favorite marvel hero is {answers[0]} and my second favorite marvel hero is {answers[1]}.")
