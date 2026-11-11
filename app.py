earnings = []

def add_earning(platform, amount):
    earnings.append((platform, amount))
    print(f"Added {amount} from {platform}")

def total():
    total_amount = sum(amount for _, amount in earnings)
    print(f"Total: {total_amount}")
    return total_amount

add_earning("Hustle", 30)
add_earning("Prolific", 0)
total()
