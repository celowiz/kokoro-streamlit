# 🎙️ Kokoro Streamlit

Interface simples em Streamlit para testar a biblioteca open-source de Text-to-Speech [Kokoro](https://github.com/hexgrad/kokoro).

## Funcionalidades

- Suporte a múltiplos idiomas e vozes
- Interface intuitiva para input de texto
- Geração de áudio local via TTS
- Stream e download do áudio gerado

## Como rodar

```bash
uv venv
uv pip install --upgrade pip
uv sync
streamlit run app.py
```

---

## 🔜 MELHORIAS FUTURAS (podemos trabalhar juntos):

- [ ] ✅ Botão para **baixar o áudio** gerado (`st.download_button`)
- [ ] 🕓 Exibir **duração estimada** do áudio
- [ ] 🌗 Adicionar **modo escuro**
- [ ] 📂 Armazenar histórico de textos + vozes
- [ ] 🌐 Tradutor automático via DeepL ou Google Translate
- [ ] 🧪 Testes automatizados com `pytest`

---