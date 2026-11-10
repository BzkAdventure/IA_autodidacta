import random

moneda = {"cara": 0, "cruz":0}

dice = {1 : 0, 2: 0 , 3: 0, 4: 0, 5: 0, 6: 0}

times = 1000

counter_dice:int = 0

for i in range (0, times):

    moneda[random.choice(["cara", "cruz"])]+=1
    dice[random.randint(1, len(dice))]+=1

print(moneda)
print(dice)


#show the frequency
freq_cara = moneda["cara"] / times
freq_cruz = moneda["cruz"] / times

print(f"Frequency of face: {freq_cara}")
print(f"Frequency of cross: {freq_cruz}")

freq_1 = dice[1] / times
freq_2 = dice[2] / times
freq_3 = dice[3] / times
freq_4 = dice[4] / times
freq_5 = dice[5] / times
freq_6 = dice[6] / times

print(f"Frequency of 1: {freq_1}")
print(f"Frequency of 2: {freq_2}")
print(f"Frequency of 3: {freq_3}")
print(f"Frequency of 4: {freq_4}")
print(f"Frequency of 5: {freq_5}")
print(f"Frequency of 6: {freq_6}")



margin_of_error = (1 / 6) - freq_6


payout = 6 * freq_6
expected_payout = 6 * (1/6)

print(expected_payout)
print(payout)