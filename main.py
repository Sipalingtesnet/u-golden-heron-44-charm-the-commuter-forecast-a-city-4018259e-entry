# Oakhaven joke: the city is fictional; the forecast mentions rogue umbrellas and rubber ducks to amuse a commuter stuck in rain.

import os


def main():
    os.makedirs("/output", exist_ok=True)
    forecast = "Oakhaven: Overcast, 14°C. Today the sky will drop a parade of rogue umbrellas and rubber ducks; bring a hat, a spare, and a grin."
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(forecast)

if __name__ == "__main__":
    main()
