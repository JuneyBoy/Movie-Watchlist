import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("/Users/arjun/Documents/Movie Watchlist/Movie-Watchlist/creds.json",scope)

client = gspread.authorize(creds)

sheet = client.open("Movie Watchlist").worksheet("Watched Movies")

print(sheet.get_all_records())