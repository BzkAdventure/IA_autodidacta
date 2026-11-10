import random
random.seed(a=1) #a seed to make the result repeatable. 
def time(runs:int):
    moneda = {"cara": 0, "cruz":0}
    dice = {1 : 0, 2: 0 , 3: 0, 4: 0, 5: 0, 6: 0}

    for i in range (0, runs):
    
        moneda[random.choice(["cara", "cruz"])]+=1
        dice[random.randint(1, len(dice))]+=1
    print(moneda)
    print(dice)
        #show the frequency
    freq_cara = moneda["cara"] / runs
    freq_cruz = moneda["cruz"] / runs

    print(f"Frequency of face: {freq_cara}")
    print(f"Frequency of cross: {freq_cruz}")

    frequencies = []

    for face,number in dice.items():
        freq = number / runs
        print(f"Frequency of {face}: {number / runs}")
        frequencies.append (freq)



    #bet: we pay 6 if it appears that number  (6). Other numbers aren't paid. 
    payout = 6 * frequencies[5]
    expected_payout = 6 * (1/6)

    margin_of_error = payout - expected_payout


    print(f"expected payout: {expected_payout}")
    print(f"real payout: {payout}")
    print(f"Margin of error: {margin_of_error}")


    if margin_of_error > 0:
        print("It's not fair; the bussiness wins")
    elif margin_of_error < 0:
        print("It's more than fair; the better wins :)")
    else:
        print("It's completely fair")

    

#100 times: 
time(100)

#1000 times:
time(1000)

#10000 times: 
time(10000)


