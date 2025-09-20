from dotenv import load_dotenv
import os

# Charge automatiquement les variables du .env
load_dotenv()

# Accéder aux variables
github_token = os.getenv("GITHUB_TOKEN")
slack_webhook = os.getenv("SLACK_WEBHOOK_URL")
sendgrid_api = os.getenv("SENDGRID_API_KEY")

# Test rapide
print("GitHub Token:", github_token)
