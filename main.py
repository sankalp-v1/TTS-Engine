import sys
import os
import asyncio
import traceback
import importlib

# This adds the project folder to Python's path so it can find the 'voice' module
sys.path.append(os.getcwd())

async def main():
    print("🔥 Running the Interactive TTS Engine...")
    
    # --- CONFIGURATION ---
    # A mapping of the provider filename to the class name inside that file
    PROVIDER_CLASS_MAP = {
        "deepgram": "DeepgramTTSProvider",
        "edge_tts": "EdgeTTSProvider",
        "speechify": "SpeechifyTTSProvider",
        "tiktok_tts": "TikTokTTSProvider",
        "hurling": "HurlingTTSProvider",
    }

    # Step 1: Pick a provider from the keys in the map above
    PROVIDER_TO_USE = "tiktok_tts"
    
    TEXT_TO_SPEAK = f"This is a test using the {PROVIDER_TO_USE} provider. Let's see how it sounds."
    OUTPUT_FOLDER = "output"
    # ---------------------

    try:
        # Dynamically import the correct provider module
        provider_module = importlib.import_module(f"voice.text_to_speech.providers.{PROVIDER_TO_USE}")
        
        # Get the correct class name from our map
        ProviderClass = getattr(provider_module, PROVIDER_CLASS_MAP[PROVIDER_TO_USE])
        
        # Create an instance of the provider
        active_provider = ProviderClass()

        print(f"🎤 Using voice provider: {PROVIDER_TO_USE}")

        # Get the list of available voices for the selected provider
        available_voices = active_provider.list_available_voices()
        chosen_voice = None

        if available_voices:
            voice_list = list(available_voices.keys())
            print("\nAvailable Voices:")
            for i, voice in enumerate(voice_list):
                print(f"  {i + 1}: {voice}")
            
            while True:
                try:
                    choice = int(input("\n➡️  Enter the number of the voice you want to use: "))
                    if 1 <= choice <= len(voice_list):
                        chosen_voice = voice_list[choice - 1]
                        print(f"👍 You selected: {chosen_voice}")
                        break
                    else:
                        print("💀 Invalid number, please try again.")
                except ValueError:
                    print("💀 Please enter a valid number.")
        
        output_filename = f"{PROVIDER_TO_USE}_{chosen_voice or 'default'}.mp3"
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        
        audio_path = active_provider.generate_speech(TEXT_TO_SPEAK, voice=chosen_voice, output_path=output_path)
        
        print(f"\n✅✅✅ SUCCESS! Audio saved to: {audio_path}")
        print(f"You should find the audio file in the '{OUTPUT_FOLDER}' folder.")

    except Exception as e:
        print(f"\n💀💀💀 An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())