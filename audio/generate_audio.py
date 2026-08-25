import os
import asyncio
import edge_tts

# Using Jenny Neural: A premier, crisp, professional adult US English instructional voice
VOICE = "en-US-JennyNeural"
# Slowed down by 15% to ensure flawless pronunciation and distinct syllable/letter emphasis
RATE = "-15%"

# 1. Define the weekly spelling list once
weekly_words = [
    "staff", "locate", "spray", "explain", "relay", "amaze", "fact", "began", "clasp", "rapid", 
    "greatly", "maintain", "natural", "national", "trails", "stranger", "display", "freight", 
    "weigh", "neighbor"
]

# 2. Map the students to their specific GitHub subfolders
student_folders = {
    "abigail_week1": weekly_words,
    "zoey_week1": weekly_words,
    "scarlett_week1": weekly_words,
    "annabel_week1": weekly_words
}

async def generate_all_audio():
    base_dir = "audio"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"Created base directory: /{base_dir}")

    total_words = sum(len(words) for words in student_folders.values())
    current_count = 0

    print(f"Starting audio generation using voice '{VOICE}' (Rate: {RATE})...\n")

    for folder_name, words in student_folders.items():
        folder_dir = os.path.join(base_dir, folder_name)
        if not os.path.exists(folder_dir):
            os.makedirs(folder_dir)
            
        print(f"--- Processing Folder: {folder_name} ---")
        
        for word in words:
            current_count += 1
            filename = f"{word.lower()}.mp3"
            filepath = os.path.join(folder_dir, filename)
            
            # Skips the file if you already generated it to save time
            if os.path.exists(filepath):
                print(f"[{current_count}/{total_words}] Skipped (Already exists): {filepath}")
                continue

            try:
                communicate = edge_tts.Communicate(word, VOICE, rate=RATE)
                await communicate.save(filepath)
                print(f"[{current_count}/{total_words}] Saved: {filepath}")
            except Exception as e:
                print(f"❌ Error generating {word}: {e}")

    print("\n🎉 All custom student audio files generated successfully!")

if __name__ == "__main__":
    asyncio.run(generate_all_audio())