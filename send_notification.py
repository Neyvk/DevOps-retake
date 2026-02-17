import os
import telebot
from datetime import datetime

bot_token = os.environ.get("BOT_TOKEN")
chat_id = os.environ.get("CHAT_ID")

repo = os.environ.get("GITHUB_REPOSITORY")
pr_title = os.environ.get("PR_TITLE")
source_branch = os.environ.get("PR_SOURCE_BRANCH")
target_branch = os.environ.get("PR_TARGET_BRANCH")
merge_url = os.environ.get("PR_URL")
release_tag = os.environ.get("RELEASE_TAG")
sonar_url = "https://sonarcloud.io/project/overview?id=Neyvk_DevOps-retake"

bot = telebot.TeleBot(bot_token)

merge_time = datetime.now()

message = f"""
<b>Новый Merge выполнен</b>
<b>Репозиторий:</b> <a href="https://github.com/{repo}">{repo}</a>
<b>Учавствовашие ветки:</b>
<code>{source_branch}</code> ➜ <code>{target_branch}</code>

<b>Pull request:</b> {pr_title}
<b>Дата:</b> {merge_time}
<a href="{merge_url}">ссылка на merge</a>

🏷 <b>Текущий Release:</b><code>{release_tag}</code>
<a href="{sonar_url}">ссылка на sonarQube</a>
"""

bot.send_message(chat_id, message, parse_mode="HTML")