print("Script Started")
import pandas as pd
from database.db import get_connection

# Read Excel
# Read Excel
df = pd.read_excel("data/Aradhana nakshatra_sorted.xlsx")

# Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()

print("Original Columns:")
print(df.columns.tolist())

# Rename Hindi columns to database columns
df = df.rename(columns={
    "कंपनी का नाम": "company_name",
    "नक्षत्र का नाम": "nakshatra_name",
    "नक्षत्र मालिक": "nakshatra_owner",
    "राशि": "rashi",
    "राशि का स्वामी": "rashi_owner",
    "Sector": "sector",
    "सेक्टटर का करक गृह": "sector_karak"
})

print("Columns After Rename:")
print(df.columns.tolist())
conn = get_connection()
cur = conn.cursor()

# Remove old data (safe for re-import)
cur.execute("DELETE FROM companies")

# Insert rows
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO companies
        (company_name, nakshatra_name, nakshatra_owner,
         rashi, rashi_owner, sector, sector_karak)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (
        row["company_name"],
        row["nakshatra_name"],
        row["nakshatra_owner"],
        row["rashi"],
        row["rashi_owner"],
        row["sector"],
        row["sector_karak"]
    ))

conn.commit()
cur.close()
conn.close()

print(f"✅ Imported {len(df)} companies successfully!")
print("Script Finished")