from agent import create_ticket

# Test with sample email
sample_email = """
Hi Support Team,

I'm having trouble logging into my account. I keep getting an error message 
saying "Invalid credentials" even though I'm sure my password is correct. 
I tried resetting it twice but still can't get in. This is urgent as I have 
a client presentation tomorrow.

Please help ASAP!

Thanks,
John Doe
"""

if __name__ == "__main__":
    result = create_ticket(sample_email)
    print("=== Ticket Created ===")
    print(f"Summary: {result['summary']}")
    print(f"Priority: {result['priority']}")
    print(f"Category: {result['category']}")
