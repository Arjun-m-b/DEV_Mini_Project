ORBITAL NEXUS - DATA RETRIEVAL SCRIPTS

Files:
1. 01_download_satcat.py
   Downloads CelesTrak's SATCAT CSV -> data/satcat.csv

2. 02_download_orbital_data.py
   Downloads CelesTrak GP orbital data for the STATIONS group
   -> data/stations_gp.csv

3. 03_download_conjunction_data.py
   Retrieves the documented SOCRATES ISS search page and extracts
   the conjunction table -> data/conjunctions_iss.csv

SETUP
-----
Open a terminal in this folder and run:

    pip install -r requirements.txt

Then run:

    python 01_download_satcat.py
    python 02_download_orbital_data.py
    python 03_download_conjunction_data.py

The CSV files will appear in the data/ folder.

NOTE
----
Use these scripts as a one-time/occasional data acquisition step.
Do not repeatedly hammer CelesTrak endpoints; follow their usage policy.
