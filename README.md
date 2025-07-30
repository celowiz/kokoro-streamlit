# 🎙️ Kokoro Streamlit

A simple Streamlit interface to test the open-source Text-to-Speech library [Kokoro](https://github.com/hexgrad/kokoro).

## Features

- Support for multiple languages and voices  
- Intuitive text input interface  
- Local TTS audio generation  
- Audio streaming and download  

## How to Run

Make sure you have **Python 3.13+** and `uv` installed.
`uv` is a fast and modern Python package manager that handles virtual environments and dependencies using `pyproject.toml`.

## Installation Steps

```bash
# Clone the repository
git clone https://github.com/your-username/kokoro-streamlit.git
cd kokoro-streamlit

# Create a virtual environment and install dependencies from pyproject.toml
uv venv
uv pip install --upgrade pip
uv sync

# Run the Streamlit app
streamlit run app.py
```

---

## 🔜 FUTURE IMPROVEMENTS (we can work on these together):

- [x] ✅ Button to download generated audio (`st.download_button`)
- [x] 🕓 Display **estimated** audio duration
- [x] 📂 Store history of texts + voices
- [x] 🌐 Automatic translation deep-translator
- [ ] 🧪 Automated tests with `pytest`

---