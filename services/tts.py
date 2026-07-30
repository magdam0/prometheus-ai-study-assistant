import io
import re
import wave
from pathlib import Path

from piper import PiperVoice
from piper.download_voices import download_voice

VOICES = {
    "pl": "pl_PL-gosia-medium",
    "en": "en_US-lessac-medium",
}
MODELS_DIR = Path(__file__).resolve().parent.parent / "models"

_voices_cache = {}

POLISH_CHARS = re.compile(r"[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]")


def _detect_language(text: str) -> str:
    return "pl" if POLISH_CHARS.search(text) else "en"


def _get_voice(language: str) -> PiperVoice:
    if language not in _voices_cache:
        voice_name = VOICES[language]
        model_path = MODELS_DIR / f"{voice_name}.onnx"

        if not model_path.exists():
            MODELS_DIR.mkdir(parents=True, exist_ok=True)
            download_voice(voice_name, MODELS_DIR)

        _voices_cache[language] = PiperVoice.load(str(model_path))

    return _voices_cache[language]


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

    cleaned_text = _clean_for_speech(text)

    if not cleaned_text.strip():
        raise ValueError("No text to synthesize speech from.")

    voice = _get_voice(_detect_language(cleaned_text))

    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wav_file:
        voice.synthesize_wav(cleaned_text, wav_file)

    return buffer.getvalue()
