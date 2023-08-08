# Telegram-Estates-Bot

# Here's a step-by-step guide on how to create a Telegram bot using BotFather:

# Create a Telegram Account:

If you don't have a Telegram account, download the Telegram app and create an account.

# Open Telegram Web:

Open your web browser and go to the Telegram Web version at https://web.telegram.org/. This step is not mandatory, but it can be useful for managing your bot later.

# Search for BotFather:

In the Telegram app or on the Telegram Web, search for "BotFather." BotFather is the official Telegram bot that helps you create and manage other bots.

# Start a Chat with BotFather:

Click on the BotFather's profile and start a chat with it.

# Create a New Bot:

To create a new bot, send the command /newbot. BotFather will guide you through the process of creating your bot:

It will ask for a name for your bot. Choose a name (ending with "bot"), e.g., "MyAwesomeBot."
Then, it will ask for a username for your bot. This username must be unique and end with "bot," e.g., "MyAwesomeBot_bot."
Get the Bot Token:

Once you've completed the creation process, BotFather will provide you with a unique token for your bot. The token will look something like this: 1234567890:ABCdefGHIjklmnOPQrstuvWXYZ.

# Keep Your Token Safe:

Your bot token is like a password. Keep it safe and do not share it with anyone. It's used to authenticate your bot with the Telegram API.

# Set Privacy Mode:

If you want your bot to respond to messages only when mentioned, you can enable privacy mode. Send /setprivacy to BotFather and follow the prompts.

# Configure Bot Settings (Optional):

You can configure various settings for your bot using BotFather's commands. For example, you can set a profile picture, add a description, or configure commands.

# Estates Bot

Estates Bot is a Telegram bot that retrieves information about estates from a Zillow link and displays them to users. The bot uses the Telegram API for communication and BeautifulSoup for web scraping.

## Prerequisites

- Python 3.x
- Required Python packages: `telegram`, `requests`, `beautifulsoup4`, `python-dotenv`

## Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   
# Innstall the required packages:
pip install -r requirements.txt

# Create an .envs file in the repository directory with the following content:
TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
URL=YOUR_ZILLOW_URL

## Usage
1. Start the bot by running:
    python main.py
2. Open your Telegram app and search for your bot. Send the command /start to begin.

3. Use the /show command to retrieve and display estate information.


# Replace `YOUR_TELEGRAM_BOT_TOKEN` with your actual Telegram bot token and `YOUR_ZILLOW_URL` with the Zillow link you're using.

# In this README, I've included sections for Prerequisites, Setup, Usage, Important Notes, and License. You might need to customize it further to suit your project's specific details and requirements.


