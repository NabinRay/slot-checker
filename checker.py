import os
import requests

TELEGRAM_BOT_TOKEN = os.environ.get("8716898007:AAEjaCQNrMTDkgUl88yY-mfSQzf7DLF8ZRc")
TELEGRAM_CHAT_ID = "6540710700"
URL = "https://edlvrs.madhesh.gov.np/edl/19e90008-bd31-4bec-b381-926267d6ecfc"

def check_slot():
    try:
        response = requests.get(URL, timeout=15)
        if "उपलब्ध" in response.text:
            msg = f"🚨 URGENT: Janakpur License Exam Slot Available!\nJaldi book karein: {URL}"
            requests.post(
                f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
                data={"chat_id": TELEGRAM_CHAT_ID, "text": msg}
            )
            print("Slot Found! Alert sent.")
        else:
            print("No slot available.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_slot()
