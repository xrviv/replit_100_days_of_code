import time, os

counter = 1
f = open("high.score", "a+")
print("HIGH SCORE TABLE\n")
f.write("HIGH SCORE TABLE\n")
while True:
    print()
    userInit = input("INITIALS > ")
    f.write(f"{userInit:<5}\t")
    score = input("SCORE > ")
    f.write(f"{score:^5}\n")
    counter += 1
    if counter < 4:
        os.system('clear')
        continue
    else:
        print("Exiting program...")
        print("Saving...")
        time.sleep(1)
        f.close()
        break
