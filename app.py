import pywhatkit as kit

# Phone number in international format (e.g., +91 for India)
phone_number = "+91 0123456789"  # Replace with recipient's number

# Message to be sent
message = "Hello! This is a scheduled WhatsApp message."

# Scheduled time (24-hour format)
hour = 20  
minute = 30

# Send the message at the scheduled time
kit.sendwhatmsg(phone_number, message, hour, minute)

print(f"Message scheduled for {hour}:{minute} to {phone_number}")
