# TTS-Engine 🗣️✨


<a href="https://ibb.co/Lzwvn7Zs"><img src="https://i.ibb.co/xSv3JT7r/20250824-133746-0000.png" alt="TTS-Engine Logo" width="40" height="40"></a>

---

[![A neon red soundwave on a black background](https://i.ibb.co/mrLdQh45/20250824-135757-0000.png)](https://ibb.co/p6tNC4j)


---
## What is this? 🤔

Tired of all the good TTS APIs being locked behind a paywall or requiring your credit card info before you can even try 'em? **TTS-Engine** is a simple, plug-and-play toolkit that bundles a bunch of the best *actually free* and reverse-engineered TTS providers into one clean package. No cap.

This project is basically what happened when we took the голосовые связки (voice components) from the powerful [Jarvis 4.0](https://github.com/SreejanPersonal/Jarvis-4.0) project, gave 'em a major glow-up, and stripped away all the extra baggage. чистота (purity) is the name of the game.

---
## Key Features 🔥

* ✅ **Multi-Provider:** Effortlessly switch between different voice engines like Deepgram (fast & pro), Speechify (hello, celebrity voices 👋), and TikTok TTS (you know the one 😉) by tweaking just one line of code.
* 💸 **Fr fr free:** We're all about that zero-cost life. This engine uses providers that don't slap you with API key requirements or sneaky charges for basic use.
* 🛠️ **Low-Key Useful:** Designed to be a lightweight, reusable piece of tech that you can yeet into any of your future projects without a second thought.

---
## 🚀 Quick Start - Let's Goooo

Get this running on your setup faster than your internet speed (hopefully).

### 1. Clone the Ting

On your local machine or in your go-to cloud dev environment (like Codespaces), grab the repo:

<details>
<summary>Click to reveal the code</summary>
<pre><code>git clone [YOUR_REPO_URL_HERE]
cd tts-engine
</code></pre>
</details>

*(Don't forget to replace `YOUR_REPO_URL_HERE` with the actual URL of your GitHub repo!)*

### 2\. Drop the Dependencies

Install all the necessary packages. We kept the `requirements.txt` super lean:

<details>
<summary>Click to reveal the code</summary>
<pre><code>pip install -r requirements.txt
</code></pre>
</details>

### 3\. Make it Go ⚙️

Create a `main.py` file in your project, paste the code below into it, and run it like it's hot.

<details>
<summary>Click to reveal the code</summary>
<pre><code class="language-python">
import sys
import os
import asyncio
import traceback

# This adds the project folder to Python's path so it can find the 'voice' module
sys.path.append(os.getcwd())

from voice.text_to_speech.manager import TTSManager

async def main():
    print("🔥 Running the Clean TTS Engine...")

    # --- CONFIGURATION ---

    # Step 1: See all your options in this list
    ALL_PROVIDERS = [
        "deepgram",    # Fast & Professional
        "edge_tts",    # Huge variety of voices
        "speechify",   # Celebrity voices (Snoop Dogg, etc.)
        "tiktok_tts",  # Viral, natural voice
        "hurling",     # Natural WaveNet voices
    ]

    # Step 2: Pick one from the list above and put its name here
    PROVIDER_TO_USE = "deepgram"

    TEXT_TO_SPEAK = f"This is a test using the {PROVIDER_TO_USE} provider. Let's see how it sounds."
    OUTPUT_FOLDER = "output"
    # The filename will now include the provider's name
    OUTPUT_FILENAME = f"{PROVIDER_TO_USE}_output.mp3"

    # ---------------------

    try:
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)
        output_path = os.path.join(OUTPUT_FOLDER, OUTPUT_FILENAME)

        tts_manager = TTSManager()
        active_provider = tts_manager.get_provider(PROVIDER_TO_USE)
        print(f"🎤 Using voice provider: {PROVIDER_TO_USE}")

        audio_path = active_provider.generate_speech(TEXT_TO_SPEAK, output_path=output_path)

        print(f"✅✅✅ SUCCESS! Audio saved to: {audio_path}")
        print(f"You should find the audio file in the '{OUTPUT_FOLDER}' folder.")

    except Exception as e:
        print(f"💀💀💀 An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
</code></pre>
</details>

Then, in your terminal:

<details>
<summary>Click to reveal the command</summary>
<pre><code>python main.py
</code></pre>
</details>

---
## 🗣️ The Voices (A Lineup)

This engine is stacked with different voice options. Just tweak the `PROVIDER_TO_USE` variable in your `main.py` to hear 'em.

* **`deepgram`**: Lightning-fast, crystal-clear, and super professional vibes. Our top pick for serious biz.
* **`edge_tts`**: The ultimate variety pack with over 1000 voices and accents. You'll find *the one*.
* **`speechify`**: Wanna hear Snoop Dogg say your grocery list? This is where the fun's at (celebrity voices for the win!).
* **`tiktok_tts`**: You know this voice. It's the one that's all over your FYP – surprisingly natural.
* **`hurling`**: This is the one you use when you need a voice that sounds genuinely human. Smooth, natural, and super high-quality.

---

## Contributing? Bet. 🙌

Got ideas for more free TTS providers to add? Found a bug? Want to make this even cleaner? Pull requests are always welcome. Let's build this together.

---
## Shoutouts 📢

Massive respect to the creators of [Jarvis 4.0](https://github.com/SreejanPersonal/Jarvis-4.0) for laying the groundwork. This project wouldn't exist without their awesome work.

---
## License 📄

MIT
