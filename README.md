# Registration_verification
Registration Verification System for supplier onboarding to our quality system.


# Registration Verification System (Python)

A simple Python-based registration validation project used to verify user details during registration of onboarding suppliers to our datasource.

This project demonstrates:
- User input validation
- Password complexity checks
- Email validation
- Banned-user filtering
- User status verification (admin/moderator)
- Step-by-step data verification logic

---

## 🔍 Features

### ✔ Step 1: Validate Name and Age
- Name and age cannot be empty.
- Age must be a numeric value.

### ✔ Step 2: Age Restriction
- Users must be 18 years or older.

### ✔ Step 3: Password Validation
Password must:
- Be at least 8 characters long  
- Contain 1 uppercase letter  
- Contain 1 lowercase letter  
- Contain 1 special character  
- Contain no spaces  

### ✔ Step 4: Email Validation
- Must contain `@`
- Must end with `.com`

### ✔ Step 5: Input Type Checking
- Username must be a string and not `None`

### ✔ Step 6: Banned User Check
The following users are banned: Suman, Karthik, kishore

### ✔ Step 7: User Status Validation
- User status must be either `admin` or `moderator`
- Banned users must have a verified email

### ✔ Step 8: Final Output
If all checks pass, user details are displayed.

---

## 📦 How to Run

```open 
python registration.py






🎯 Purpose of This Project
This project is ideal for:

Demonstrating data validation and input handling
Showcasing Python programming skills
Onboarding supplier data base validation
ETL pipeline 
Teaching basic backend verification concepts
Practicing secure user‑input rules

It highlights how multi-layered verification is implemented in real applications to ensure data integrity and prevent invalid registrations.
