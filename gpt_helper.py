import openai
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def frage_Codex(prompt):
    try:
        response = client.chat.completions.create(
            model = "gpt-4",
            messages = [{"role":"user","content": prompt}],
            temperature = 0.4
        )
        return response.choices[0].message.content.strip()
    except Exception as e: 
        return f"Fehler bei der Anfrage:\n{e}"
    
def main():
    print("Codex - dein GPT-4 Assistent ")
    print("Stell Fragen rund ums Coden, Python, Java, Fehler usw.")
    print("Zum Beenden einfach [Enter] drücken.\n")
    
    while True:
        frage = input ("Frage an Codex: ").strip()
        if not frage:
            print("Bis bald - keep coding !")
            break
        antwort = frage_Codex(frage)
        print(f"\nAntwort von Codex:\n{antwort}\n{'-'*60}")
        
if __name__ == "__main__":
    main()