#~ libary used for cli parsing 
import click

#~ Loads the csv file and returns the data as a string
def load_cookie_log_file(file: str) -> str:
    with open(file) as f:
        data = f.read()
    return data

#~ Sorts the values into a dictionary with the date as the key and the cookies as the values
def sort_data_as_date_to_cookies(data: str) -> dict[str, list]:
    data_split = data.split("\n") #~ Separate the data by line breaks and store it in a list
    #& Example:
    #& data = """cookie,timestamp
    #& AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
    #& SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
    #& SAZuXPGUrfbcn5UA,2018-12-09T11:13:00+00:00"""
    #& data_split = ["cookie,timestamp", "AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00", "SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00", "SAZuXPGUrfbcn5UA,2018-12-09T11:13:00+00:00"]
    
    #~ dictionary/hashmap to store the data with key: date and value: list of cookies
    log = {}
    
    #~ Iterate over the data_split list starting from the second element as this removes the header
    #TODO
    #! Another approach -> The header might have to be removed at the start via data_split.pop(0)
    
    for i in range(1, len(data_split)): 
        
        #~ Separate the cookie and timestamp by comma
        #& Example: AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00 ->
        #& cookie : AtY0laUfhglK3lC7 timestamp : 2018-12-09T14:19:00+00:00
        cookie, timestamp  = data_split[i].split(",")
        
        #~ Split the timestamp by T and get the date which is the first element
        #& Example: 2018-12-09T14:19:00+00:00 -> 2018-12-09
        date = timestamp.split("T")[0] 
        
        #~ Check if the date is already in the dictionary
        #~ If it is, then append the cookie to the list of cookies
        #~ If not, then create a new key with the date and store the cookie as a list
        #? This ensures that there are no duplicate dates and that each date has all its respective cookies
        #? At the start we have no dates so all unique dates will be added to the dictionary
        #? Then when a repeated date is found, the cookie will be appended to the list of cookies instead of added as a new key
        if date in log:
            log[date].append(cookie)
        else:
            log[date] = [cookie]
            
    return log
    
def find_most_active_cookie(log: dict, date: str):
    #~ List to store the number of times a cookie appears in a date
    max_value_list = [] 
    
    #~ Dictionary to store the cookie and the number of times it appears in a date
    max_cookie_dict = {}
    #~ Iterate over all the cookies in the date list
    for cookie in log[date]:
        #~ Store the number of times a cookie it appears in a date
        #& Example '2018-12-09': ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA', 'SAZuXPGUrfbcn5UA', '5UAVanZf6UtGyKVS', 'AtY0laUfhglK3lC7']
        #& max_value_list = [2, 2, 2, 1, 2]
        #? We do this to work out what the max number of times any cookie appears in a date
        #? This then lets us find any cookie with the matching number of times it appears in said date
        max_value_list.append(log[date].count(cookie))
        
        #~ Store the cookie and the number of times it appears in a dictionary
        #& Example '2018-12-09': ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA', 'SAZuXPGUrfbcn5UA', '5UAVanZf6UtGyKVS', 'AtY0laUfhglK3lC7']
        #& max_cookie_dict = {'AtY0laUfhglK3lC7': 2, 'SAZuXPGUrfbcn5UA': 2, '5UAVanZf6UtGyKVS': 1}
        max_cookie_dict[cookie] = log[date].count(cookie)
    
    #~ Find the max number of times any cookie appears in a date    
    max_cookie_value = max(max_value_list)
    
    most_active_cookies = []
    #~ Iterate over the dictionary and find any cookie that appears the max number of times in a date and store it in a list 
    for k, v in max_cookie_dict.items():
        if v == max_cookie_value:
            most_active_cookies.append(k)
    
    return most_active_cookies


def print_most_active_cookies(cookies: list):
    for cookie in cookies:
        print(cookie)


@click.command()
@click.option('--filename', '-f', required=True, type = str, help="The cookie log file path")
@click.option('--date', '-d', required=True, type = str, help="The date to find the most active cookies")

def main(filename: str, date: str):
    try:
        data = load_cookie_log_file(filename)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error loading file: {e}")
        return

    try:
        log = sort_data_as_date_to_cookies(data)
    except Exception as e:
        print(f"Error sorting values: {e}")
        return

    if date not in log:
        print(f"No data for date: {date}")
        return

    most_active_cookies = find_most_active_cookie(log, date)

    #~ If there are no active cookies then say so for said date
    if not most_active_cookies:
        print(f"No active cookies found for date: {date}")
    else:
        print_most_active_cookies(most_active_cookies)

if __name__ == "__main__":
    main()