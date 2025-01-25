# Instagram Content Fetcher Bot

This is a Telegram bot that allows users to fetch the latest Instagram content (stories, posts, and reels) from public profiles by simply typing the username. The bot uses the `Instaloader` library to fetch the URLs and sends the links back to the chat.

## Features
- Fetch the latest story, post, and reel of a given Instagram username.
- Directly send URLs to the user without downloading content.
- Easy-to-use bot interface.

## Prerequisites
- Python 3.10+
- A Telegram bot token from [BotFather](https://t.me/BotFather)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rebvar-ebra/insta_checker.git
   cd insta_checker
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File**:
   In the project directory, create a `.env` file and add your bot token:
   ```
   BOT_TOKEN=your_telegram_bot_token
   ```

## Usage

1. **Run the Bot**:
   ```bash
   python insta_checker.py
   ```

2. **Interact with the Bot**:
   - Start the bot by sending the `/start` command in Telegram.
   - Send an Instagram username (e.g., `instagram`) to fetch the latest story, post, and reel.

## File Structure
```
.
├── insta_checker.py                # Main bot script
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (contains the bot token)
└── README.md             # Project documentation
```

## Dependencies
- [python-telegram-bot](https://python-telegram-bot.readthedocs.io/): For Telegram bot integration.
- [instaloader](https://instaloader.github.io/): For fetching Instagram content.

Install all dependencies using the following command:
```bash
pip install -r requirements.txt
```

## Notes
- This bot works only for public Instagram accounts.
- If you encounter rate-limiting or other issues with `Instaloader`, please try again after some time.
- The bot does **not** download or store any content on the server.

## Troubleshooting

### Common Errors
1. **Invalid Token**:
   Ensure that you have set your Telegram bot token correctly in the `.env` file.

2. **HTTP Error 429**:
   Instagram might temporarily block the bot due to rate limits. Wait for a few minutes and try again.

3. **No Story/Post/Reel Found**:
   Ensure the username is correct and the profile has public content available.

### Debugging
Run the insta_checker in debug mode to see detailed logs:
```bash
python insta_checker.py --debug
```

## License
This project is licensed under the MIT License. Feel free to use and modify it.

## Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.

## Author
Rebvar Ebrahimi
