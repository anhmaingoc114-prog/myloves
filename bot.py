import os
import logging
from dotenv import load_dotenv

# Tắt log thừa
logging.getLogger("discord").setLevel(logging.CRITICAL)

from discord.ext import commands
from discord import Activity, ActivityType, Status

load_dotenv()

# ====================== CONFIG ======================
CONFIG = {
    "TOKEN": os.getenv("DISCORD_TOKEN", "").strip(),
    "APPLICATION_ID": os.getenv("APPLICATION_ID", "").strip(),   # BẮT BUỘC
    "NAME": "for in love",
    "DETAILS": "Only u",
    "LARGE_IMAGE": os.getenv("LARGE_IMAGE", ""),                 # Không bắt buộc nữa
    "LARGE_TEXT": "bes bo",
}
# ====================================================

if not CONFIG["TOKEN"]:
    print("❌ Không tìm thấy DISCORD_TOKEN!")
    exit(1)

if not CONFIG["APPLICATION_ID"]:
    print("❌ Phải có APPLICATION_ID để dùng ảnh!")
    exit(1)

client = commands.Bot(
    command_prefix="!", 
    self_bot=True,
    chunk_guilds_at_startup=False,
    guild_subscriptions=False
)

@client.event
async def on_ready():
    print(f"✅ Đã đăng nhập: {client.user}")

    # Nếu không có LARGE_IMAGE thì dùng tên mặc định "logo" (bạn có thể đổi sau)
    large_image = CONFIG["LARGE_IMAGE"] or "logo"

    activity = Activity(
        application_id=int(CONFIG["APPLICATION_ID"]),
        type=ActivityType.playing,
        name=CONFIG["NAME"],
        details=CONFIG["DETAILS"],
        large_image=large_image,
        large_text=CONFIG["LARGE_TEXT"],
    )

    await client.change_presence(activity=activity, status=Status.online)

    print("🎮 Rich Presence đã chạy!")
    print(f"   Tên       : {CONFIG['NAME']}")
    print(f"   Chi tiết  : {CONFIG['DETAILS']}")
    print(f"   Ảnh       : {large_image}")

# ====================== CHẠY ======================
if __name__ == "__main__":
    try:
        print("🚀 Đang khởi động selfbot...")
        client.run(CONFIG["TOKEN"], log_handler=None, root_logger=False)
    except Exception as e:
        print(f"❌ Lỗi: {e}")