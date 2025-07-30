import streamlit as st
from datetime import datetime
from kokoro import KPipeline
import soundfile as sf
import numpy as np
import tempfile
import os

from utils import save_to_history, show_history, translate_text

# Page configuration
st.set_page_config(
    page_title="Kokoro TTS", 
    page_icon="🔊",
    layout="wide", 
    initial_sidebar_state="expanded")

# Sidebar
with st.sidebar:
    st.image("kokoro.png")
    st.divider()
    st.subheader("🕘 History:")  

# --- LAYOUT ---
st.title("Kokoro TTS")
col1, col2 = st.columns([2, 1])

# --- LEFT COLUMN: Text input ---
with col1:
    st.markdown("### 🎙️ Text-to-Speech Input")
    text = st.text_area("Enter the text below:", height=300)

# --- RIGHT COLUMN: Voice parameters --
with col2:
    st.markdown("### ⚙️ Voice Parameters")

    lang_map = {
        '🇺🇸 English (US)': 'a',
        '🇬🇧 English (UK)': 'b',
        '🇧🇷 Português (BR)': 'p',
        '🇪🇸 Español': 'e',
        '🇫🇷 Français': 'f',
        '🇮🇹 Italiano': 'i',
        '🇮🇳 Hindi': 'h',
        '🇯🇵 日本語': 'j',
        '🇨🇳 中文': 'z',
    }

    lang_name = st.selectbox("🌍 Language", list(lang_map.keys()))
    lang_code = lang_map[lang_name]

    # Voice options per language
    voice_options = {
        'a': ['🚺 Heart', '🚺 Alloy', '🚺 Aoede', '🚺 Bella', '🚺 Jessica', '🚺 Kore', '🚺 Nicole', '🚺 Nova',
              '🚺 River', '🚺 Sarah', '🚺 Sky', '🚹 Adam', '🚹 Echo', '🚹 Eric', '🚹 Fenrir', '🚹 Liam', '🚹 Michael',
              '🚹 Onyx', '🚹 Puck', '🎅 Santa'],
        'b': ['🚺 Alice', '🚺 Emma', '🚺 Isabella', '🚺 Lily', '🚹 Daniel', '🚹 Fable', '🚹 George', '🚹 Lewis'],
        'p': ['🚺 Dora', '🚹 Alex', '🎅 Santa'],
        'e': ['🚺 Dora', '🚹 Alex', '🎅 Santa'],
        'f': ['🚺 Siwis'],
        'i': ['🚺 Sara', '🚹 Nicola'],
        'h': ['🚺 Alpha', '🚺 Beta', 'Omega', 'Psi'],
        'j': ['🚺 Alpha', '🚺 Gongitsune', '🚺 Nezumi', '🚺 Tebukuro', '🚹 Kumo'],
        'z': ['🚺 Xiaobei', '🚺 Xiaoni', '🚺 Xiaoxiao', '🚺 Xiaoyi', '🚹 Yunjian', '🚹 Yunxi', '🚹 Yunyang'],
    }

    voice = st.selectbox("Voice", voice_options.get(lang_code, []))

    speed = st.slider("Voice Speed", 0.5, 2.0, 1.0, 0.1)

    translate = st.checkbox("🌐 Auto-Translate to all languages!", False) 

    generate = st.button("🔊 Generate Audio")

# --- AUDIO GENERATION ---
if generate and text:
    with st.spinner("Generating audio..."):
        # Prepare voice code
        api_voice = lang_code + voice.replace('🎅 ', 'm_').replace('🚹 ', 'm_').replace('🚺 ', 'f_').lower()
        print('Voice:', api_voice)
        
        # Run Kokoro pipeline
        pipeline = KPipeline(lang_code=lang_code)
        generator = pipeline(text, voice=api_voice, speed=speed)

        audio_chunks = [audio for _, _, audio in generator]
        audio_final = np.concatenate(audio_chunks)

        # Save to temp file
        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        sf.write(tmp_file.name, audio_final, 24_000)

        st.success("✅ Audio successfully generated!")

        # --- Playback and download ---
        st.audio(tmp_file.name, format="audio/wav")

        # Show estimated duration
        duration_sec = round(len(audio_final) / 24000, 2)
        st.markdown(f"🕓 **Estimated duration:** {duration_sec} seconds")

        # Download button
        with open(tmp_file.name, "rb") as audio_file:
            audio_bytes = audio_file.read()

        st.download_button(
            label="⬇️ Download Audio",
            data=audio_bytes,
            file_name="kokoro_tts_output.wav",
            mime="audio/wav"
        )

        # Translate Text
        if translate:
            st.empty()
            st.markdown("## Translation:")
            user_text = translate_text(text)

        # Save Last Request to History
        save_to_history({
            "text": text,
            "lang": lang_name,
            "voice": voice,
            "speed": speed,
            "timestamp": datetime.now().isoformat()
        })

        # Show History
        show_history()

# --- FOOTER ---
st.markdown("---")
github_url = "https://github.com/celowiz/kokoro-streamlit" # GitHub repo

footer_html = f"""
<div style='text-align: center; margin-top: 30px; font-size: 0.9em;'>
    <a href="{github_url}" target="_blank">
        <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Repository" style="height: 30px;">
    </a>
    <p style='margin-top: 10px;'>
        Built by <strong>Marcelo Wizenberg</strong> • 
        <a href="{github_url}" target="_blank">{github_url}</a>
    </p>
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)