from typing import Dict
import os

DEFAULT_PIN: int = 17

DOT_DURATION: float = os.environ.get('DOT_DURATION') or 0.1
DASH_DURATION: float = os.environ.get('DASH_DURATION') or 0.3
REST_DURATION: float = os.environ.get('REST_DURATION') or 0.1
PAUSE_DURATION: float = os.environ.get('PAUSE_DURATION') or 0.3

MORSE_CODES: Dict[str, str] = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}
