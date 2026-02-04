import datetime
import os
from typing import List, Dict

from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Load environment variables from .env file
load_dotenv()

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

# Configuration from environment or defaults
CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID", "primary")
CREDENTIALS_PATH = os.getenv("GOOGLE_CREDENTIALS_PATH", "secrets/credentials.json")
TOKEN_PATH = "token.json"


def get_credentials() -> Credentials:
    """
    Handles the OAuth2 flow: loads existing tokens or runs 
    the local server to authenticate the user.
    """
    creds = None

    # The file token.json stores the user's access and refresh tokens
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_PATH):
                raise FileNotFoundError(
                    f"Credentials file not found at {CREDENTIALS_PATH}. "
                    "Please download it from the Google Cloud Console."
                )
            
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_PATH, SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(TOKEN_PATH, "w") as token:
            token.write(creds.to_json())

    return creds


def get_upcoming_events(service, max_results: int = 10) -> List[Dict]:
    """Fetch upcoming calendar events starting from 'now'."""
    # 'Z' indicates UTC time
    now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()

    events_result = (
        service.events()
        .list(
            calendarId=CALENDAR_ID,
            timeMin=now,
            maxResults=max_results,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    return events_result.get("items", [])


def build_calendar_service():
    """Builds and returns the Google Calendar API service object."""
    creds = get_credentials()
    return build("calendar", "v3", credentials=creds)


def main():
    """Main entry point for the script."""
    try:
        print(f"Connecting to calendar: {CALENDAR_ID}...")
        service = build_calendar_service()
        
        events = get_upcoming_events(service)

        if not events:
            print("No upcoming events found.")
            return

        print("\n--- Upcoming Events ---")
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            summary = event.get("summary", "No title")
            print(f"{start} | {summary}")

    except HttpError as error:
        print(f"An API error occurred: {error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
