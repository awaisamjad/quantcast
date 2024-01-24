#~ libary used for cli parsing 
import typer 

#~ Loads the csv file and returns the data as a string
def load_csv(file: str) -> str:
    with open(file) as f:
        data = f.read()
    return data

#~ Sorts the values into a dictionary with the date as the key and the cookies as the values
def sort_values(data: str) -> dict[str, list]:
    data_split = data.split("\n") #~ Separate the data by line breaks and store it in a list
    #& Example:
    #& data = """cookie,timestamp
    #& AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
    #& SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
    #& SAZuXPGUrfbcn5UA,2018-12-09T11:13:00+00:00"""
    #& data_split = ["cookie,timestamp", "AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00", "SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00", "SAZuXPGUrfbcn5UA,2018-12-09T11:13:00+00:00"]
    
    log = {} #~ dictionary/hashmap to store the data with key: date and value: list of cookies
    for i in range(1, len(data_split)): 
        
        #~ Separate the cookie and timestamp by comma 
        cookie, timestamp  = data_split[i].split(",")
        
        #~ Split the timestamp by T and get the date which is the first element
        #& Example: 2018-12-09T14:19:00+00:00 -> 2018-12-09
        date = timestamp.split("T")[0] 
        
        #~ Check if the date is already in the dictionary
        #~ If it is, then append the cookie to the list of cookies
        #~ If not, then create a new key with the date and store the cookie as a list
        #? This enusres that there are no duplicate dates and that each date has all its respective cookies
        #? At the start we have no dates so all unique dates will be added to the dictionary
        #? Then when a repeated date is found, the cookie will be appended to the list of cookies instead of added as a new key
        if date in log:
            log[date].append(cookie)
        else:
            log[date] = [cookie]
            
    #~ Return the dictionary
    return log
    
def find_most_active_cookie(log: dict, date: str):
    
    max_value_list = []
    max_cookie_dict = {}
    for cookie in log[date]: #~ Iterate over all the cookies in the date list
        max_value_list.append(log[date].count(cookie))
        max_cookie_dict[cookie] = log[date].count(cookie)
    max_cookie_value = max(max_value_list)
    
    most_active_cookies = []
    for k, v in max_cookie_dict.items():
        if v == max_cookie_value:
            most_active_cookies.append(k)
    return most_active_cookies

def print_most_active_cookies(cookies: list):
    for cookie in cookies:
        print(cookie)

def main(filename: str, date: str):
    data = load_csv(filename)
    log = sort_values(data)
    most_active_cookies = find_most_active_cookie(log, date)
    print_most_active_cookies(most_active_cookies)

if __name__ == "__main__":
    main("cookie_log.csv", "2018-12-09")