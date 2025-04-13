import pywhatkit as kit
import sys
import datetime

def schedule_whatsapp_message(phone_number, message, date_time):
    """
    Schedules a WhatsApp message using pywhatkit.
    """
    # Initialize hour and minute to default values
    hour = 0
    minute = 0
    try:
        # Convert the date_time string to a datetime object
        schedule_time = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M')

        # Get the hour and minute from the datetime object
        hour = schedule_time.hour
        minute = schedule_time.minute

        print(f"Message scheduled for {hour}:{minute} to {phone_number}")

        # Send the message at the scheduled time
        kit.sendwhatmsg(phone_number, message, hour, minute)
        print("Message scheduled successfully!")

    except Exception as e:
        print(f"Error scheduling message: {e}")

if __name__ == '__main__':
    # Check if the required arguments are provided
    if len(sys.argv) < 4:
        print("Error: Phone number, message, and date/time must be provided as command-line arguments.")
        sys.exit(1)

    # Get the phone number, message, and date_time from the command line arguments
    phone_number = sys.argv[1]
    message = sys.argv[2]
    date_time = sys.argv[3]

    # Schedule the WhatsApp message
    schedule_whatsapp_message(phone_number, message, date_time)
