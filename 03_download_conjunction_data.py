

from io import StringIO
from pathlib import Path
import sys

import pandas as pd
import requests

URL = (
    "https://celestrak.org/socrates/table-socrates.php"
    "?CATNR=25544&ORDER=MINRANGE&MAX=25"
)

OUTPUT = Path("data/conjunctions_iss.csv")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    print("Downloading SOCRATES conjunction data...")
    print(URL)
    print()

    try:
        response = requests.get(
            URL,
            timeout=60,
            headers={
                "User-Agent": "OrbitalNexus-Student-Project/1.0"
            },
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"Download failed: {exc}")
        sys.exit(1)

    html = response.text

    if "<html" not in html.lower():
        print("The response does not look like an HTML page.")
        sys.exit(1)

   
    try:
        tables = pd.read_html(StringIO(html), flavor="lxml")
    except ValueError as exc:
        print(f"Could not find an HTML table: {exc}")
        sys.exit(1)

    if not tables:
        print("No tables were found.")
        sys.exit(1)

    
    target = None

    for table in tables:
        cols = " ".join(str(col) for col in table.columns).upper()

        if (
            "NORAD" in cols
            and "NAME" in cols
            and "TCA" in cols
        ):
            target = table
            break

    if target is None:
        target = max(tables, key=lambda t: len(t))

    
    target = target.dropna(axis=0, how="all").dropna(axis=1, how="all")

    target.to_csv(OUTPUT, index=False)

    print("SUCCESS")
    print(f"Saved: {OUTPUT.resolve()}")
    print(f"Rows: {len(target)}")
    print(f"Columns: {len(target.columns)}")
    print()
    print("Columns:")
    for column in target.columns:
        print(f"  - {column}")

    print()
    print("First rows:")
    print(target.head().to_string(index=False))


if __name__ == "__main__":
    main()
