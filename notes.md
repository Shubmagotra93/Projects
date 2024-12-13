- Using **`webdriver_manager`** is the most reliable and recommended approach. It ensures you have the compatible **`chromedriver`** version for your Chrome and avoids issues with multiple versions on your system.
    - **`pip install --upgrade webdriver-manager`**
    - **`driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))`**
- If you're unsure which Chrome version you have, use `google-chrome --version` in your terminal to check.
- Check path for downloaded chromedriver from webdriver manager:
  - **`/home/shubham/.wdm/drivers/..`**

***
- **XPATH**:
    
    - `//tagname[@attribute='value']`
    - `//input[@id='username']`
- **XPATH by text:**
    
    - `//tagname[text()='value']`
    - `//span[text()='Admin']`
- **XPATH by contains : when xpath is dynamic**
    
    - `//tagname[contains(text(), 'value')]`
    - `//a[contains(text(),'Books')]`
    - `(//a[contains(text(),Books)])[1]`
- **Child to Parent XPATH**
    
    - `(//a[text()='API Docs'])/../../..//p[text()='.NET/C#']`\- https://www.selenium.dev/downloads/
- **Parent to Child XPATH**
    
    - `//p[text()='.NET/C#']/..//a[text()='API Docs']`

* * *

**Link Text and Partial Link Text:**

- `driver.find_element(By.LINK_TEXT, "Log in")` - take name from DOM
    
- `driver.find_element(By.PARTIAL_LINK_TEXT,"Log in")` - take name displayed in screen
    

* * *

**Traversing: Xpath axes : following sibling and preceding sibling**

- `//td//following::input[1]`
- `//td//preceding::input[2]`
- `//td/..` - from parent

* * *

**CSS Selectors: nth child pending**

- By id -  use  hash(#)
    - `#username`
- By class  - use  dot(.)
    - `.password`
- tag_name\[attribute='value'\]
    - `input[id='username']`

* * *

**Select class for dropdowns**

- `from selenium.webdriver.support.ui import Select`
    
- `element = driver.find_element("")`
    
- `select = Select(element)`
    
- `select.select_by_index(3)`
    
- `select.deselect_by_all()`\- when multi dropdown options are available - we can deselect them
    

* * *

**ActionChains Class - for mouse hover interactions**

- `element = driver.find_element("")`
- `action = ActionChains(driver)`
- `action.move_to_element(element).perform()` - moving to element
- `action.context_click(element).peform()` - Right click
- `source = driver.find_element(""), target = driver.find_element("")`
- `action.drag_and_drop(source, target).perform` - Drag and Drop
- `action.double_click(element).perform()` - Double click

* * *

**Javascript Alert**

- `alert = Alert (driver)`
- `alert.accept()` - to accept the alert
- `alert.dismiss()` - to dismiss the alert
- `alert.send_keys("")` - to send text to alerts

* * *

**Handle Alerts through Expected Conditions as EC**
```python
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
a = wait.until(EC.alert_is_present() # True/False
a.send_keys("")
a.accept()
```
* * *

**Scroll through ActionChains class:**

- `ActionChains(driver).scroll_to_element(element).perform()`

**Scroll through JavaScript executor:**

- Scroll to a specific position: use scrollTo()
    - `element.rect` - check **dimensions** (height, width) and **coordinates** (x,y) of the referenced element
    - `element.location` - provides x and y **coordinates**
    - `driver.execute_script("window.scrollTo(225, 3628);")` - scroll To specific position
    - `driver.execute_script("window.scrollTo(0, 0);")` - scroll To top
- Scroll to a specific element:  scrollIntoView()
    - `driver.execute_script("arguments[0].scrollIntoView();", element)`
- Clicking Elements: Click on an element that's not directly clickable:
    - `driver.execute_script("arguments[0].click();", element)`

* * *

**Switching to Frames:**

- By Web-Element
    
    - `web_element = driver.find_element(By.XPATH, "//iframe[@id= 'mce_0_ifr']")`
        
    - `driver.switch_to.frame(web_element)`
        
- By Index
    
    - `driver.switch_to.frame(0)`
- By id or name attribute
    
    - `driver.switch_to.frame("frame_id")`
- Switch back to main content
    
    - `driver.switch_to.default_content()`
- child to parent frame
    
    - `driver.switch_to_parent_frame()`

* * *

**Window Handle:**

https://www.selenium.dev/documentation/webdriver/interactions/windows/#windows-and-tabs

- **Store the ID of the original window**

  - `original_window = driver.current_window_handle`
- **Click the link which opens in a new window**
    
    - `driver.find_element(By.XPATH, "(//div[@id='new_window']").click()`
- **Wait for the new window or tab**
    
    - `wait.until(EC.number_of_windows_to_be(2))`

- **Loop through until we find a new window handle**

```python
for child_window in driver.window_handles:
  if child_window != original_window:
    driver.switch_to.window(child_window)
    break
```
**OR write below line of code, it is in list comprehension way:**
```python
[child_window for child_window in driver.window_handles if child_window != original_window][0]:
driver.switch_to.window(child_window) 

or 

[driver.switch_to.window(child_window) for child_window in driver.window_handles if child_window != original_window][0]
``` 
- **Wait for the new tab to finish loading content**
    
    - `wait.until(EC.title_is("DEMOQA"))`
- **Switched back to main window**
    
    - `driver.switch_to.window(original_window)`
- **Get window size : Access each dimension individually**
    
    - `width = driver.get_window_size().get("width")`
        
    - `height = driver.get_window_size().get("height")`
        
- **Set window size: Restores the window and sets the window size.**
    
    - `driver.set_window_size(1024, 768)`
- **Get window position : Access each dimension individually**
    
    - `x = driver.get_window_position().get('x')`
        
    - `y = driver.get_window_position().get('y')`
        
- **Set window position : Move the window to the top left of the primary monitor**
    
    - `driver.set_window_position(0, 0)`
- **Fullscreen window**
    
    - `driver.fullscreen_window()`
- **Save Screenhot**
    
    - `driver.save_screenshot('./image.png')`
- **TakeElementScreenshot**
    
    - `ele = driver.find_element(By.CSS_SELECTOR, 'h1')`
        
        `ele.screenshot('./image.png')`
        

* * *

**Synchronisation Waits:**

- **Implicit Waits**: An implicit wait value can be set either with the timeouts capability in the browser options, or with a driver method
    
    - https://www.selenium.dev/documentation/webdriver/drivers/options/#timeouts
        
    - `options = webdriver.ChromeOptions()`  
        `options.timeouts = { 'implicit': 5000 }`  
        `driver = webdriver.Chrome(options=options)`
        
    - `driver.implicitly_wait(2)`
        
- **Explicit Wait:** https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html
    
    - `from selenium.webdriver.support import expected_conditions as EC`
    - `wait= WebDriverWait(driver, 10)`
- Passing Locator:
    
    - `locator = (By.NAME, "username")`
    - `wait.until(EC.visibility_of_element_located(locator)).send_keys("Admin")`
- Passing Web Element:
    
    - `element = driver.find_element(By.NAME, "username")`
    - `wait.until(EC.visibility_of(driver.find_element(locator[0],locator[1]))).send_keys("Admin")`
    - `# wait.until(EC.visibility_of(element))`
- https://www.selenium.dev/documentation/webdriver/waits/
    
- `errors = [NoSuchElementException, ElementNotInteractableException]`
    
- `wait = WebDriverWait(driver, 20, poll_frequency=.2, ignored_exceptions=errors)`
    

* * *

**Framework:**
```python
@pytest.mark.regression
@pytest.mark.login
def test_select_city(setup):
    pass

- pytest -m "not smoke" test_new.py  # run only smoke cases
- pytest -m "regression and login" test_new.py - test cases with both markers are executed
- pytest -m "regression or login" test_new.py - both regression and login cases will be executed
```
* * *

**Allure Installation:** https://allurereport.org/docs/install/

- download allure > Uncompressed the archive into an installation directory of your choice.
    
- Add allure's /bin path to environment variables according to Windows system but in Linux add it in permanent PATH, so that we can execute allure from anywhere
    
  - `nano ~/.bashrc` - edit `.bashrc` file and add path or directly run below command:
        
  - `export PATH=$PATH:/home/shubham/Shubham_QA/drivers/allure-2.22.0/bin`
      
  - `PATH="$PATH:$HOME/bin:$ALLURE_HOME"` - update PATH as well
      
  - `source ~/.bashrc` - refresh the `.bashrc` file
      
  - `echo $PATH` - print the paths

**OR if above steps won't work try below steps:**

- Create a Correct Symlink
```
- sudo ln -s /home/shubham/Shubham_QA/drivers/allure-2.22.0/bin/allure /usr/bin/allure`
```
- Verify Symlink
```
- ls -l /usr/bin/allure - to list symlink
- sudo rm /usr/bin/allure - to remove symlink
```
- Install below packages for allure
```
- allure-pytest
- allure-python-commons
```
- Commands to run allure
```
- pytest --alluredir=reports test2.py
- allure serve reports  - Run command in directory under which reports are generated
```
- Attach screenshot to allure
```
- allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
- request.node.name` - is used to fetch current test case name
```
* * *
**Parameterization in pytest:**
```python
@pytest.mark.parametrize(argnames, argvalues)

Sample Example:
@pytest.mark.parametrize("input,expected", [(2, 4), (3, 9), (4, 16)])
def test_square(input, expected):
	assert input ** 2 == expected
```
* * *
```python
@pytest.mark.parametrize(
    "username, password",
[
        ("Admin", "admin123"), # Valid credentials
        ("invalid_user", "admin123"), # Invalid username
        ("Admin", "wrongpassword"), # Invalid password
        ("", ""), # Empty credentials
]
)

def test_login(params, username, password):
	username_field = driver.find_element(By.NAME, "username")
	username_field.send_keys(username)
	password_field = driver.find_element(By.NAME, "password")
	password_field.send_keys(password)
	login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
	login_button.click()
```
* * *
- **Reading data from yaml file:**
```
- pip install pyyaml
```

- **Create config.yaml file in the project directory and add below data:**
```YAML
url: https://opensource-demo.orangehrmlive.com/
username: Admin
password: admin123
```
******- Create separate fixture in conftest file for handling **YAML** file:******
```python
@pytest.fixture(scope="session")
def config_data():
	with open("config.yaml", "r") as file:
		return yaml.safe_load(file) # Returns the content as a dictionary

 def test_example(params, config_data):
	# Use data from the YAML configuration
    url = config_data["url"]
    username = config_data["username"]
    password = config_data["password"]
    driver.get(url)
    time.sleep(2)
```
- **For JSON - add config.json file with below syntax:**
```json
{
	"url": "https://opensource-demo.orangehrmlive.com/",
	"username": "Admin",
	"password": "admin123"
}
```
- **JSON file handling function:** 
 ```python
def config_data():
	with open("config.json", "r") as file:
	   return json.load(file) # Returns the content as a dictionary
```
- Calling methods is same like we did in yaml
* * *
**Cucumber Framework - BDD Framework (Behave)**
```
- pip install behave-to-cucumber
- pip install behave
```
- To install reports  
```
- pip install behave-html-formatter`
```
- To run the reports  
```
- behave --format behave_html_formatter:HTMLFormatter --outfile=reports/report.html`
```
* * *
**API Testing: GET, POST, PUT,  PATCH**
- **Reading data from payload.json file:**
```json
{
  "create": {
      "firstname": "Shubham",
      "lastname": "Magotra",
      "totalprice": 150,
      "depositpaid": true,
      "bookingdates": {
          "checkin": "2024-12-01",
          "checkout": "2024-12-10"
      },
      "additionalneeds": "Green Tea"
  },
  "update": {
      "firstname": "Jane",
      "lastname": "Smith",
      "totalprice": 200,
      "depositpaid": false,
      "bookingdates": {
          "checkin": "2024-12-05",
          "checkout": "2024-12-15"
      },
      "additionalneeds": "Wi-Fi"
  },
   "headers": {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
  }
}
 ```
- **Method to read json data from json file and parse it in request data**
```python
with open("./payload.json", 'r') as file:
        json_data = json.load(file)

payload = json_data['create']
response = requests.post(endpoint, headers=headers, json=payload)

print(type(response.text)) - <class 'str'>
res = response.json()
print(type(res)) - <class 'dict'>

# dumps(object)  #json.dumps(res, indent=4)
# json.dump(object, file)- serialize a Python object (e.g., dictionary or list) to a JSON-formatted string and write it directly to a file.
# load(file) — This method deserializes the data from a file and returns the object.
# Serialization is the process of converting an object’s state to a byte stream,and deserialization is the reverse process of reconstructing the object from a byte stream.
#############################################################
# json parsing through string using LOADS method
data = '{"name":"Shubham", "languages":["java","Python"]}'
dict_data = json.loads(data)
print(dict_data)
print(dict_data["name"])
print(dict_data["languages"][0])

# json parsing through JSON file using LOAD method
with open("C:\\Users\\Shubham Magotra\\Desktop\\testfile.json") as f:
    data = json.load(f)
    print(data)
```
* * *
- **Reading data from Excel file:**
```python
def get_payloads_from_excel(file_path):
    data = pd.read_excel(file_path)
    payloads = []
    for _, row in data.iterrows():
        payload = {
            "firstname": row["firstname"],
            "lastname": row["lastname"],
            "totalprice": int(row["totalprice"]),
            "depositpaid": row["depositpaid"] in [True, "True", 1],
            "bookingdates": {
                "checkin": row["checkin"],
                "checkout": row["checkout"]
            },
            "additionalneeds": row["additionalneeds"]
        }
        payloads.append(payload)
    print("TTTT", payloads)
    return payloads
====================================================
def get_payloads_from_excel(file_path):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path, sheet_name="API2")
    pd.read_csv(file_path)
    # Convert the DataFrame into a list of dictionaries (one per row)
    payloads = df.to_dict(orient="records")
    print(payloads)
    return payloads
```
* * *
- **CSV file reading** : Read using panda as pd : 
- We can use this function as well refer excel data :
  - `pd.read_csv(file_path)`
```python
with open('./payload.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)  # dictionary data
        payload = {
            "firstname": row['firstname'],
            "lastname": row['lastname'],
            "totalprice": int(row['totalprice']),
            "depositpaid": row['depositpaid'] == 'True', 
            "bookingdates": {
                "checkin": row['checkin'],
                "checkout": row['checkout']
            },
            "additionalneeds": row['additionalneeds']
        }
        response = requests.post(endpoint, headers=headers, json=payload)
```

GIT COMMANDS:
- `git config --list --global`
- `git config --list --local`
- `git config --list --system`
- `git config --list` - View All Configurations Combined
- `git config --list --show-origin` - Identify the Configuration File Paths - `/home/shubham/.gitconfig`


- **To set enviromnet varibales from CLI**
```PYTHON
export API_KEY =123

export HOST=12.12.1313
printenv - to print all env varibales on system
###############################################
How to unset them:
unset API_KEY, unset HOST

How to use env varibales in code:
API_KEY =os.environ["API_KEY"]
TIMEOUT = os.environ.get('TIMEOUT', 10)
print(API_KEY)
 
 To create virtual enviroment and activate it
 python3 -m venv env
 source env/bin/activate
 
 nano env/bin/activate - open this
 and at the end place env varibales like 
 API_KEY, so that each time we run vir env we get that key
```

