import os
import requests

TELEGRAM_BOT_TOKEN = os.environ.get("8716898007:AAEjaCQNrMTDkgUl88yY-mfSQzf7DLF8ZRc")
TELEGRAM_CHAT_ID = "6540710700"

# Real Janakpur License Portal URL
URL = "https://edlvrs.madhesh.gov.np/edl/19e90008-bd31-4bec-b381-926267d6ecfc"

def check_slot():
    try:
        response = requests.get(URL, timeout=15)
        html_content = response.text.lower()
        
        # Color codes aur status indicators jo green slot highlight hone par detect honge
        green_indicators = [
            "#28a745", 
            "rgb(40, 167, 69)", 
            "bg-success", 
            "available", 
            "उपलब्ध"
        ]
        
        # Checking if any green/available status exists in page HTML
        if any(indicator in html_content for indicator in green_indicators):
            msg = f"🚨 URGENT: Janakpur License Exam Slot Available (Green Marked)!\nJaldi book karein: {URL}"
            requests.post(
                f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
                data={"chat_id": TELEGRAM_CHAT_ID, "text": msg}
            )
            print("Green Slot Found! Alert sent successfully.")
        else:
            print("No green slot available right now.")
            
    except Exception as e:
        print(f"Error checking portal: {e}")

if __name__ == "__main__":
    check_slot()
