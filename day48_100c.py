import time, os

counter = 1
f = open("high.score", "a+")
f.write("HIGH SCORE TABLE\n")
while True:
    print()
    print("HIGH SCORE TABLE\n")
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
        time.sleep(1)
        f.close()
        break
