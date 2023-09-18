import time

def count(start, end, countBy = 1):
    if end < start and countBy >= 0:
        print("\nSwapping\n")
        temp = end
        end = start
        start = temp
    count = start
    print(f"Counting from {start} to {end} by {countBy}'s")
    for count in range(start,end,countBy):
        time.sleep(0.05)
        print(count)
        count += countBy
    print(count,"\n")
count(int(input("\nCount from: ")),int(input("Count to: ")),int(input("Count by: ")))

