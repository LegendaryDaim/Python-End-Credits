import gspread
import config as c

def get_sheet():
    link_to_sheet = c.link
    # todo Make a Try here. If no internet connection.
    gc = gspread.oauth() # this token is in %APPDATA%\gspread!    New file be created in the same directory called authorized_user.json
    sh = gc.open_by_url(link_to_sheet)     # opens link and gets the title of the sheet document.
    worksheet = sh.get_worksheet(0)   # Selecting the worksheet. If only one sheet then it's ok to do this
    list_of_lists = worksheet.get_all_values()  # gets all values from the sheet
    print("Fetching Google Sheet        DONE 100%")
    sheet_name = str(sh).split("'")[1]
    c.tot_rows = len(worksheet.col_values(1))
    return list_of_lists, sheet_name
