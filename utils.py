import os
import json
import streamlit as st
from deep_translator import GoogleTranslator

HISTORY_FILE = "history.json"

ALL_LANGUAGES = {
        '🇺🇸|🇬🇧 English': 'en',
        '🇧🇷 Português': 'pt',
        '🇪🇸 Español': 'es',
        '🇫🇷 Français': 'fr',
        '🇮🇹 Italiano': 'it',
        '🇮🇳 Hindi': 'hi',
        '🇯🇵 日本語': 'ja',
        '🇨🇳 中文': 'zh-CN',
    }

def load_history():
    """Load history from JSON file safely."""
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:  # empty file
                return []
            return json.loads(content)
    except (json.JSONDecodeError, IOError):
        return []
    
def save_to_history(entry):
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as f:
            json.dump([], f)

    with open(HISTORY_FILE, "r") as f:
        history = load_history()
        history.append(entry)
        # Keep only last 10 entries
        history = history[-10:]
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=2)
        history.append(entry)

def show_history():
    history = load_history()
    if history:
        for i, item in enumerate(reversed(history)):
            st.sidebar.markdown(
                f"**{i+1}. {item['text']}**\n"
                f"- `{item['lang']}`, `{item['voice']}`, speed `{item['speed']}`"
            )
def translate_text(text, dest_lang="en"):
    for language, langcode in ALL_LANGUAGES.items():
        st.divider()
        translated = GoogleTranslator(source='auto', target=langcode).translate(text)
        st.text(f'{language}: {translated}')
        