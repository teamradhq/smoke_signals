import time
import os
from typing import Optional
from unittest.mock import MagicMock
from gpiozero import LED, BadPinFactory

import smoke_signals.config as config

if os.environ.get('MOCK_GPIO') == '1':
    print("Mocking GPIO")
    LED = MagicMock()


def translate_to_morse(text: str):
    return ''.join([config.MORSE_CODES[char] + ' ' if char in config.MORSE_CODES else ' ' for char in text.upper()])


def transmit_character(duration: float, led: LED, char: Optional[str] = None):
    """
    Activate LED for the given duration. Optionally, provide char to print to stdout.

    :param duration:
    :param led:
    :param char:
    :return:
    """
    if char is not None:
        print(char, end='', flush=True)
    try:
        led.on()
        time.sleep(duration)
        led.off()
        time.sleep(config.REST_DURATION)
    except BadPinFactory:
        return "GPIO functionality is not available on this system."
    return None


DURATION_MAP = {
    '.': config.DOT_DURATION,
    '-': config.DASH_DURATION
}


def transmit_morse(morse_code: str, pin_number: Optional[int] = None):
    """
    Transmit the provided morse code.
    :param morse_code:
    :param pin_number:
    :return:
    """
    if pin_number is None:
        pin_number = config.DEFAULT_PIN
    error = None
    led = LED(pin_number)
    for symbol in morse_code:
        duration = DURATION_MAP.get(symbol)
        if duration:
            result = transmit_character(duration, led, symbol)
            error = error or result
    time.sleep(config.PAUSE_DURATION)


def main():
    pin = int(input("GPIO pin number (default 17): ") or config.DEFAULT_PIN)
    text = input("Enter text: ")
    translated = translate_to_morse(text)
    print(f"Translated: {translated}")
    transmit_morse(translated, pin)
