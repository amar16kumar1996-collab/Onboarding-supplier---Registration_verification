import re

# Step 6 - List of banned users
banned_users = ["Suman", "Karthik", "kishore"]

def validate_password(password):
    """Validate password: >= 8 chars, 1 uppercase, 1 lowercase, 1 special char, no spaces."""
    if len(password) < 8:
        return False
    if " " in password:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[!@#$%^&*()_+=\\[\\]{};:'\",.<>/?\\\\|-]", password):
        return False
    return True


def main():

    while True:

        # STEP 1 – Enter user_name & user_age
        user_name = input("Enter your name: ").strip()
        user_age = input("Enter your age: ").strip()

        if not user_name or not user_age:
            print("Error: Name or Age cannot be empty. Try again.\n")
            continue

        # STEP 5 – Check if user_name is valid string
        if not isinstance(user_name, str) or user_name is None:
            print("Invalid name. Restarting...\n")
            continue

        # STEP 2 – Check user_age >= 18
        if not user_age.isdigit():
            print("Age must be a number. Try again.\n")
            continue

        user_age = int(user_age)

        if user_age < 18:
            print("Underage! Access denied.\n")
            continue

        # STEP 3 – Validate password
        user_password = input("Enter your password: ")

        if not validate_password(user_password):
            print("Password invalid! Must contain uppercase, lowercase, special character, no spaces and be at least 8 chars long.\n")
            continue

        # STEP 4 – Validate email
        user_email_id = input("Enter your email ID: ").strip()

        if not user_email_id or "@" not in user_email_id or not user_email_id.endswith(".com"):
            print("Email ID is invalid! Must contain '@' and end with '.com'.\n")
            continue

        email_verified = True

        # STEP 7 – Validate user_status
        user_status = input("Enter your status (admin/moderator): ").strip().lower()

        if user_status not in ["admin", "moderator"]:
            print("Invalid status. Must be admin or moderator.\n")
            continue

        if user_name in banned_users and not email_verified:
            print("Access denied: User is banned and email not verified.\n")
            continue

        # STEP 8 – Everything OK → Print summary
        print("\n✔ Registration Successful!")
        print("Name:", user_name)
        print("Age:", user_age)
        print("Email:", user_email_id)
        print("Password:", user_password)
        break


if __name__ == "__main__":
    main()
