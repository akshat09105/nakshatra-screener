import psycopg2

conn = psycopg2.connect(
    host="db.hkucvqwahygzyihtkduq.supabase.co",
    port=5432,
    database="postgres",
    user="postgres",
    password="KLRahul@1234",
    sslmode="require"
)

print("Connected")