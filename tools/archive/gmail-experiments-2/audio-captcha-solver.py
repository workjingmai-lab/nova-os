#!/usr/bin/env python3
"""
Audio CAPTCHA Solver — Self-built, no external APIs
Uses open-source speech recognition
"""

import subprocess
import tempfile
import os
import base64
import json

class AudioCaptchaSolver:
    """Solve audio CAPTCHAs using self-hosted speech recognition"""

    def __init__(self):
        # Check for available speech recognition tools
        self.speech_engine = self.detect_speech_engine()

    def detect_speech_engine(self):
        """Detect available speech recognition engines"""

        engines = []

        # Check for Whisper (OpenAI's speech recognition - can run locally)
        try:
            result = subprocess.run(
                ["whisper", "--help"],
                capture_output=True,
                timeout=5
            )
            if "OpenAI Whisper" in result.stderr.decode():
                engines.append("whisper")
        except:
            pass

        # Check for Sphinx (CMU Sphinx - offline speech recognition)
        try:
            import speech_recognition as sr
            engines.append("sphinx")
        except:
            pass

        # Check for Deepspeech (Mozilla's offline STT)
        try:
            result = subprocess.run(
                ["deepspeech", "--help"],
                capture_output=True,
                timeout=5
            )
            engines.append("deepspeech")
        except:
            pass

        return engines[0] if engines else None

    def download_audio_captcha(self, url):
        """Download audio CAPTCHA from URL"""

        print(f"[Audio CAPTCHA] Downloading from {url}...")

        result = subprocess.run(
            ["python3", "/home/node/.openclaw/workspace/tools/lightweight-browser.py", "get", url],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode != 0:
            print(f"❌ Failed to download audio")
            return None

        data = json.loads(result.stdout)

        if not data.get("ok"):
            return None

        # Save to temp file
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            # Assume content is audio data
            f.write(data.get('content', '').encode())
            return f.name

    def solve_audio_file(self, audio_file):
        """Solve audio CAPTCHA from file"""

        if not self.speech_engine:
            print("❌ No speech recognition engine available")
            return None

        print(f"[Audio CAPTCHA] Solving with {self.speech_engine}...")

        if self.speech_engine == "whisper":
            return self.solve_with_whisper(audio_file)
        elif self.speech_engine == "sphinx":
            return self.solve_with_sphinx(audio_file)
        elif self.speech_engine == "deepspeech":
            return self.solve_with_deepspeech(audio_file)

        return None

    def solve_with_whisper(self, audio_file):
        """Use Whisper for speech recognition"""

        try:
            result = subprocess.run(
                ["whisper", audio_file, "--model", "base", "--output_format", "json"],
                capture_output=True,
                text=True,
                timeout=60
            )

            # Parse output
            output = result.stdout

            # Extract text from JSON output
            if ".json" in output:
                json_file = audio_file.replace(".mp3", ".json")
                if os.path.exists(json_file):
                    with open(json_file, 'r') as f:
                        data = json.load(f)
                        return data.get('text', '').strip()

            return output.strip()

        except Exception as e:
            print(f"❌ Whisper error: {e}")
            return None

    def solve_with_sphinx(self, audio_file):
        """Use CMU Sphinx for speech recognition"""

        try:
            import speech_recognition as sr

            r = sr.Recognizer()

            with sr.AudioFile(audio_file) as source:
                audio_data = r.record(source)

                text = r.recognize_sphinx(audio_data)
                return text

        except Exception as e:
            print(f"❌ Sphinx error: {e}")
            return None

    def solve_with_deepspeech(self, audio_file):
        """Use Mozilla DeepSpeech for speech recognition"""

        try:
            result = subprocess.run(
                ["deepspeech", audio_file],
                capture_output=True,
                text=True,
                timeout=30
            )

            return result.stdout.strip()

        except Exception as e:
            print(f"❌ DeepSpeech error: {e}")
            return None

def test_audio_captcha():
    """Test audio CAPTCHA solver"""

    print("🎙️  Audio CAPTCHA Solver")
    print("="*60)

    solver = AudioCaptchaSolver()

    print(f"\nAvailable engines: {solver.speech_engine or 'None'}")

    if not solver.speech_engine:
        print("\n⚠️  No speech recognition engine found")
        print("\nTo install:")
        print("  Whisper: pip install openai-whisper")
        print("  Sphinx: pip install SpeechRecognition pocketsphinx")
        print("  DeepSpeech: pip install deepspeech")
        return False

    print(f"\n✅ Using {solver.speech_engine} for audio CAPTCHA solving")

    # If we have an audio file, test it
    print("\n💡 Usage:")
    print("  1. Download audio CAPTCHA from form")
    print("  2. Pass to solver.solve_audio_file(path)")
    print("  3. Get transcribed text")

    return True

if __name__ == "__main__":
    test_audio_captcha()
