## ChromeDriverBase Class

ChromeDriverBase is a base class that provides a convenient way to create a Chrome web driver instance using the Selenium library. This class can be used as a parent class for implementing custom web driver classes that perform specific tasks on web pages. The class uses the Chrome browser to open URLs and can perform actions on web elements by executing JavaScript code.

### Example usage

```
from base_class.chrome_driver_base import ChromeDriverBase

class MyDriver(ChromeDriverBase):
    pass
```

```
skill_share_login_url = "https://www.skillshare.com/en/login"
driver =  ExampleDriver()
driver.openUrl(skill_share_login_url)
```

In the above example, a custom web driver class named MyDriver is defined that inherits from ChromeDriverBase. Then, an instance of this class is created, and the openUrl() method is used to open a web page in the Chrome browser.


## HandleEventHelper Class

HandleEventHelper is a helper class that provides methods for interacting with web elements on a page using the Selenium library. This class can be used to perform various actions on web elements, such as clicking on buttons, entering text in input fields, etc. The class also provides methods for waiting for web elements to become present on the page before performing any actions.

### Example usage

```
from selenium.webdriver.common.by import By

skill_share_login_url = "https://www.skillshare.com/en/login"
driver =  ExampleDriver()
driver.openUrl(skill_share_login_url)
```

```
def sample_with_attribute():
    driver.handle_event_helper.execute_element_by_attribute("name", "email", "sample@gmail.com")
    driver.handle_event_helper.execute_element_by_attribute("type", "button")
```

```
def sample_with_class_name():
    driver.handle_event_helper.execute_element_by_tag(By.CLASS_NAME, "login-inputs-fields", "sample@gmail.com")
    driver.handle_event_helper.execute_element_by_tag(By.CLASS_NAME, "submit-btn")
```

```
def sample_with_x_path():
    driver.handle_event_helper.execute_element_by_tag(By.XPATH, '//*[@id="page-wrapper"]/div[2]/div/div/form/div[2]/input', "sample@gmail.com")
    driver.handle_event_helper.execute_element_by_tag(By.XPATH, '//*[@id="page-wrapper"]/div[2]/div/div/form/button[4]')
```

```
def sample_with_pure_text():
    time.sleep(5)
    #Have to set a fixed wait time. And the input field have no text content at all
    driver.handle_event_helper.execute_element_have_text("input", 'Email address', "sample@gmail.com")
    driver.handle_event_helper.execute_element_have_text("button", 'Sign In')
```

```
def sample_step_by_step():
    element = driver.handle_event_helper.wait_for_presence(By.CLASS_NAME, "submit-btn")
    driver.handle_event_helper.move_cursor_and_click(element)
```

In the above example, an instance of the Chrome web driver is created, and an instance of HandleEventHelper is initialized with this driver instance. Then, various methods of HandleEventHelper are used to interact with web elements on the page, such as clicking on a button and entering text in an input field. The wait_for_presence() method is also used to wait for an element to become present on the page before performing any action on it.

## Captcha Solver

This section contains the implementation of a captcha solver using computer vision and Selenium WebDriver. The `CaptchaSolver` class has methods to bypass login captchas and solve them using image recognition. The `waiting_for_loading_login_captcha` method waits for the captcha to load before solving it. The `solve_captcha` method downloads the captcha images and uses OpenCV to get the drag position to solve the captcha. The `is_page_source_contains_text` method checks if a given text is present in the page source.

### Example usage
```
while self.captcha_solver.is_waiting_for_sign_up_loading_captcha(): 
    //do something if can not load captcah after TIME_OUT seconds
    pass

self.captcha_solver.bypass_sign_up_captcha()
```
This code snippet runs a loop to continuously check if the sign-up captcha is still loading. If the loading takes too long, the program will proceed to the next line of code after a specified timeout. Once the captcha is loaded, the `bypass_sign_up_captcha()` method is called to solve the captcha and allow the program to proceed with sign-up.


## Remote API helper

The RemoteAPIHelper class provides a convenient method for fetching JSON data from an API endpoint using Selenium. The class takes in a webdriver object during initialization and also initializes an instance of the HandleEnventHelper class which it uses to interact with the web page.

### Example usage

```
def sample_fetch_api():
    api_url = "https://api.usercentrics.eu/translations/translations-en.json"
    json_result =  driver.remote_api_helper.loadJsonFromURL(api_url)
    print(json_result)
```

In the above example, a sample_fetch_api() function has been defined to demonstrate how to use the RemoteAPIHelper class to fetch JSON data from an API endpoint in a Selenium script. This function can be used as a starting point for developers who want to integrate API requests into their Selenium scripts.


## Command Executor

This module provides helper functions to execute commands in Python.

- `execute_command(command)`: This function executes the given command.
- `execute_command_with_root(command, root_password)`: This function executes the given command as root, using the specified root_password.

### Example usage

```
from command_execution_helper import execute_command, execute_command_with_root

# Execute a simple command
execute_command('ls')

# Execute a command as root
execute_command_with_root('apt-get update', 'mypassword')
```


## File IO Helper

This module provides various helper functions to work with file Input/Output (IO) operations. The functions provided are:

- `remove_data_from_file(removedData, file_name)`: This function removes the lines containing the given removedData from the file with the specified file_name. It reads the file into a list, filters out the lines containing the specified removedData, and overwrites the file with the filtered list of lines.

- `get_first_data_from_file(file_name)`: This function returns the first line of the file with the specified file_name. It reads the file, returns the first line as a string, and removes the newline character.

- `get_random_data_from_file(file_name)`: This function returns a random line from the file with the specified file_name. It reads the file, generates a random index within the range of the number of lines, returns the line at that index as a string, and removes the newline character.

- `get_all_data_as_list_from_file(file_name)`: This function returns all lines from the file with the specified file_name as a list of strings. It reads the file, returns all lines as a list of strings, and removes the newline character from each line.

- `save_new_data(data, file_name)`: This function appends the given data as a new line to the file with the specified file_name.

- `keep_log_data(data, additional_data = "", file_name = "data")`: This function appends the given data along with any additional data (if provided) to the log file with the specified file_name. If no file_name is provided, it will use the default value of "data".

- `get_machine_name()`: This function returns the hostname of the machine on which the code is running.

- `create_csv_directory()`: This function creates a directory named csv_file if it does not already exist and returns the path to the directory.

### Example usage

```
import file_io_helper

# create csv directory
csv_directory = file_io_helper.create_csv_directory()

# save new data to file
data = "new data"
file_io_helper.save_new_data(data, "data")

# get first line from file
first_line = file_io_helper.get_first_data_from_file("data")
print(first_line)

# get random line from file
random_line = file_io_helper.get_random_data_from_file("data")
print(random_line)

# get all lines from file as list
all_lines = file_io_helper.get_all_data_as_list_from_file("data")
print(all_lines)

# remove data from file
data_to_remove = "data to remove"
file_io_helper.remove_data_from_file(data_to_remove, "data")

# keep log data
log_data = "log data"
file_io_helper.keep_log_data(log_data, additional_data="some additional data")
```

## DateTimeHelper

A class for handling datetime manipulation in Python.

- `get_time_remain_to(destinated_date_time_str)`: returns the timedelta between the current date and time and the given destination date and time string.
- `get_current_date_time_in_date_time_format()`: returns the current date and time in the format specified in date_time_format.
- `conver_str_date_time_to_hour_time_format(date_time_str)`: converts a datetime string to the hour format specified in hour_time_format.
- `conver_str_date_time_to_date_time_format(date_time_str)`: converts a datetime string to the datetime format specified in date_time_format.
- `conver_str_time_to_another_format(date_time_str, another_date_time_format)`: converts a datetime string to a specified datetime format.
