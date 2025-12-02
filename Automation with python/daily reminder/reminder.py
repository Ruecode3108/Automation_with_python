import schedule
import time
from plyer import notification

def send_notification(message_text):
    """Function to create and send the desktop notification with a custom message."""
    print(f"Sending Notification: {message_text}")
    notification.notify(
        title='🛑 PYTHON REMINDER 🛑',
        message=message_text,
        app_name='Python Automation Bot',
        timeout=5 # Reduced timeout for more frequent popups
    )

def main():
    """Set up the scheduler to run the function automatically with multiple popups in seconds."""
    
    # Schedule 1: A general reminder every 10 seconds
    schedule.every(10).seconds.do(send_notification, 
                                  message_text='Quick check-in! Take a deep breath.')
    
    # Schedule 2: A different reminder every 30 seconds
    schedule.every(30).seconds.do(send_notification, 
                                  message_text='💧 Hydration Alert: Grab a drink of water!')

    # Schedule 3: A third reminder every 45 seconds
    schedule.every(45).seconds.do(send_notification, 
                                  message_text='👀 Eye break! Look away from the screen for 20 seconds.')
    
    print("✅ Python Scheduler Started!")
    print("   Multiple notifications are now scheduled in seconds.")
    print("   Press Ctrl+C to stop the script.")
    
    # Keep the script running: Loop forever to check the schedule
    while True:
        schedule.run_pending()
        time.sleep(1) # Wait 1 second before checking the schedule again

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nScheduler stopped by user. Goodbye!")