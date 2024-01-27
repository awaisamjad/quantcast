import quantcast as q
import unittest
class Test_QuantCast (unittest.TestCase) : 
    # def test_load_cookie_log_file(self) :
    #     self.assertEqual(q.load_cookie_log_file("cookie_log.csv"), "cookie_log.csv")
    
    def test_sort_data_as_date_to_cookies(self) :
        load_cookie_log_file = q.load_cookie_log_file("cookie_log.csv")
        self.assertEqual(
            q.sort_data_as_date_to_cookies(load_cookie_log_file),
            "{'2018-12-09': ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA', 'SAZuXPGUrfbcn5UA', '5UAVanZf6UtGyKVS', 'AtY0laUfhglK3lC7'], '2018-12-08': ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG'], '2018-12-07': ['4sMM2LxV07bPJzwf']}")
    
    def test_find_most_active_cookie(self) :
        sort_data_as_date_to_cookies = q.sort_data_as_date_to_cookies(q.load_cookie_log_file("cookie_log.csv"))
        
        self.assertEqual(
            q.find_most_active_cookie(sort_data_as_date_to_cookies, "2018-12-09"), ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA'])
        
if __name__ == "__main__" :
    unittest.main()
    
    