def login(email, password):
    if not email or not password:
        return "Email and password are required"

    return "Login successful"


def calculate_total(price, quantity):
    total = price * quantity
    return total