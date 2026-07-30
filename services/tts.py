import io
import re
import wave
from pathlib import Path

from piper import PiperVoice
from piper.download_voices import download_voice

VOICE_NAME = "en_US-lessac-medium"
MODELS_DIR = Path(__file__).resolve().parent.parent / "models"
MODEL_PATH = MODELS_DIR / f"{VOICE_NAME}.onnx"

_voice = None


def _get_voice() -> PiperVoice:
    global _voice

    if _voice is None:
        if not MODEL_PATH.exists():
            MODELS_DIR.mkdir(parents=True, exist_ok=True)
            download_voice(VOICE_NAME, MODELS_DIR)

        _voice = PiperVoice.load(str(MODEL_PATH))

    return _voice


def _clean_for_speech(text: str) -> str:
    """Strips common markdown symbols so they aren't read aloud."""

    text = re.sub(r"[*_#`]", "", text)
    text = re.sub(r"^\s*[-•]\s+", "", text, flags=re.MULTILINE)
    return text


def synthesize_speech(text: str) -> bytes:
    """
    Converts text to speech using the local Piper TTS engine.
    Returns WAV audio bytes.
    """

    voice = _get_voice()
    cleaned_text = _clean_for_speech(text)

    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wav_file:
        voice.synthesize_wav(cleaned_text, wav_file)

    return buffer.getvalue()
