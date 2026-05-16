import threading
import sys
import os

# 1. Start the Telegram Bot Daemon
def start_bot_daemon():
    print("\n" + "="*50)
    print("[Telegram Bot] Starting background listener...")
    
    # Add the current folder to sys.path so it can import the bot script
    current_dir = os.path.dirname(os.path.realpath(__file__))
    if current_dir not in sys.path:
        sys.path.append(current_dir)
        
    try:
        from .telegram_comfy_bot import TelegramBot, ConfigManager
        app_config = ConfigManager.load_config()
        if app_config:
            bot = TelegramBot(app_config)
            # Run start_polling in a daemon thread so it doesn't block ComfyUI
            threading.Thread(target=bot.start_polling, daemon=True).start()
        else:
            print("[Telegram Bot] Failed to load config. Bot disabled.")
    except Exception as e:
         print(f"[Telegram Bot] FAILED to start daemon: {e}")
         
    print("="*50 + "\n")

start_bot_daemon()

# 2. Keep your Save to Phone Node mapping (if you still want it)
try:
    from .save_to_phone import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
except ImportError:
    NODE_CLASS_MAPPINGS = {}
    NODE_DISPLAY_NAME_MAPPINGS = {}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']