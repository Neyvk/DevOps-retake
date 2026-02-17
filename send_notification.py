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

bot = telebot.TeleBot(bot_token)

merge_time = datetime.now()

message = f"""
<b>Новый Merge выполнен!</b>
<b>Репозиторий:</b> <a href="https://github.com/{repo}">{repo}</a>
<b>Замержена ветка:</b>
<code>{source_branch}</code> ➜ <code>{target_branch}</code>

<b>PR:</b> {pr_title}
<b>Дата мержа:</b> {merge_time}
<b>Ссылка на merge:</b>
<a href="{merge_url}">Открыть Pull Request</a>

🏷 <b>Текущий Release:</b><code>{release_tag}</code>
"""

bot.send_message(chat_id, message, parse_mode="HTML")