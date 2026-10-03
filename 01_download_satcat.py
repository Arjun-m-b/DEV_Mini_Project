

from pathlib import Path
import sys
import requests

URL = "https://celestrak.org/pub/satcat.csv"
OUTPUT = Path("data/satcat.csv")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    print(f"Downloading SATCAT from:\n{URL}")

    try:
        response = requests.get(
            URL,
            timeout=60,
            headers={"User-Agent": "OrbitalNexus-Student-Project/1.0"},
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"Download failed: {exc}")
        sys.exit(1)

    
    content = response.content
    if b"<html" in content[:500].lower() or b"<!doctype" in content[:500].lower():
        print("The server returned HTML instead of CSV. No file was saved.")
        sys.exit(1)

    OUTPUT.write_bytes(content)

    print(f"Saved: {OUTPUT.resolve()}")
    print(f"Size: {len(content) / 1024:.1f} KB")


if __name__ == "__main__":
    main()
