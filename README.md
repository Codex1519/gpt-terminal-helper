# gpt-terminal-helper
# 🤖 gpt-terminal-helper

Ein leichtes Python-Terminal-Tool, um direkt Fragen an OpenAI GPT-Modelle zu stellen – perfekt für Entwickler, die beim Coden schnelle Hilfe brauchen.

---

## ⚙️ Funktionen

- 🔁 GPT-4 / GPT-3.5 via OpenAI API (terminalbasiert)
- 🔍 Alternative: StackOverflow-Abfragen ohne API-Key
- 📦 Minimalistisches CLI-Tool mit schneller Ausgabe
- 🔐 API-Key bleibt sicher durch Umgebungsvariable

---

## 🚨 Wichtig: API kostet Geld

Dieses Tool nutzt die OpenAI API.  
Die API ist **nicht kostenlos** – du brauchst:

- Ein OpenAI-Konto → https://platform.openai.com
- Einen **API-Key**
- Aufgeladenes Guthaben (ab 5 $ möglich)

> Ohne Guthaben funktionieren GPT-Anfragen **nicht**!  
> Du erhältst sonst Fehlermeldungen wie `model_not_found`, `quota_exceeded` o. ä.

💡 **Keine Angst:** Guthaben wird **nur bei Nutzung** verbraucht.  
GPT-3.5 kostet nur Bruchteile eines Cents pro Anfrage.

---

## 🧪 Kostenloser Modus: `livehelper.py`

Wenn du kein Guthaben nutzen willst, kannst du alternativ `livehelper.py` starten.  
Dieses Tool nutzt die StackOverflow-Such-API – komplett **kostenlos**, ohne API-Key oder Konto.

---

## 🔧 Installation

1. 📦 Repository klonen oder Dateien downloaden
2. 🐍 Python installieren (mind. 3.7)
3. Abhängigkeiten installieren:

```bash
pip install openai

python gpt_helper.py

python livehelper.py (StackVverflow API)


