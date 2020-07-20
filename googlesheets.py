from pprint import pprint
from googleapiclient import discovery


credentials = jeffrey_credentials.json
service = discovery.build('sheets', 'v4', credentials=credentials)

spreadsheet_ID = 1AGTCXVC_9h3LnF8GJaE-MJj978AVoBnl4kV4Z9a4r7I

# How the input data should be interpreted.
value_input_option = 'USER-ENTERED'  # TODO: Update placeholder value.

# How the input data should be inserted.
insert_data_option = 'INSERT_ROWS'  # TODO: Update placeholder value.

# The A1 notation of a range to search for a logical table of data.
# Values will be appended after the last row of the table.
range_ = 'A1:F1'  # TODO: Update placeholder value.

value_range_body = {
    # TODO: Add desired entries to the request body.
}

sheet.INSERT_ROWS(["Kung Fu Panda", "July 10, 2020"], 2)

# request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
# response = request.execute()

# TODO: Change code below to process the `response` dict:
# pprint(response)