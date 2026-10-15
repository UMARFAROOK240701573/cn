n = int(input("Enter total number of frames: "))
w = int(input("Enter window size: "))

i = 0

while i < n:
    print("\nSending frames:")
    for j in range(i, min(i + w, n)):
        print("Frame", j + 1, "sent")

    ack = input("Acknowledgment received? (yes/no): ")

    if ack.lower() == "yes":
        i += w
        print("Window slides forward")
    else:
        print("Waiting for acknowledgment...")

print("\nAll frames transmitted successfully!")