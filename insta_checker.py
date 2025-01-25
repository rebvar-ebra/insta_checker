from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from instaloader import Instaloader, Profile
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Initialize Instaloader (no login)
insta_loader = Instaloader()
# Function to fetch Instagram content URLs
def fetch_instagram_content_urls(username: str):
    profile = Profile.from_username(insta_loader.context, username)

    # Initialize media URLs
    latest_story_url = None
    latest_post_url = None
    latest_reel_url = None

    # Get the latest story
    try:
        for story in profile.get_stories():
            for item in story.get_items():
                latest_story_url = item.url  # Get the direct story URL
                break
            if latest_story_url:
                break
    except Exception as e:
        print(f"Error fetching story: {e}")

    # Get the latest post
    try:
        posts = profile.get_posts()
        latest_post = next(posts, None)
        if latest_post:
            latest_post_url = latest_post.url  # Get the direct post URL
    except Exception as e:
        print(f"Error fetching post: {e}")

    # Get the latest reel
    try:
        for post in profile.get_posts():
            if post.typename == "GraphVideo":  # Reels are videos
                latest_reel_url = post.url  # Get the direct reel URL
                break
    except Exception as e:
        print(f"Error fetching reel: {e}")

    return latest_story_url, latest_post_url, latest_reel_url


# Command handler for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome! Send me an Instagram username, and I'll fetch the latest story, post, and reel for you."
    )


# Message handler for Instagram usernames
async def handle_instagram_username(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.text.strip()  # Get the plain username
    if username:
        await update.message.reply_text(f"Fetching content for @{username}...")
        try:
            # Fetch Instagram content URLs
            latest_story_url, latest_post_url, latest_reel_url = fetch_instagram_content_urls(username)

            # Send the URLs back to the user
            if latest_story_url:
                await update.message.reply_text(f"Here is the latest story: {latest_story_url}")

            if latest_post_url:
                await update.message.reply_text(f"Here is the latest post: {latest_post_url}")

            if latest_reel_url:
                await update.message.reply_text(f"Here is the latest reel: {latest_reel_url}")

            if not (latest_story_url or latest_post_url or latest_reel_url):
                await update.message.reply_text(
                    f"Could not find any recent content for @{username}. They might not have public posts, reels, or stories."
                )

        except Exception as e:
            await update.message.reply_text("Failed to fetch Instagram content. Please try again later.")
            print(f"Error: {e}")
    else:
        await update.message.reply_text("Please send a valid Instagram username.")

# Main function to set up the bot
def main():
    # Replace TOKEN with your Telegram bot token
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_instagram_username))

    # Start the bot
    application.run_polling()


if __name__ == "__main__":
    main()
