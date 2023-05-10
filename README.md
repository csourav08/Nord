This code demonstrates how to use Selenium for web automation in Python. It uses the Chrome web driver to automate the process of filling out a form on a web page and submitting it. The form is located at https://www.provet.cloud/provet-cloud-request-a-demo and is filled out with information from a credentials dictionary.

The **Browser** class provides methods to open a web page, fill in text inputs, click buttons, and select dropdown menus. The login method uses these methods to fill out the form with the information from credentials and submit it.

The main code initializes the **Browser** class, opens the demo page, waits for the "book demo" button to be clickable, clicks it, logs in, waits for 5 seconds, and closes the browser.

Note that there are several time.sleep() calls in the code to pause the execution of the script for a specified number of seconds. These pauses are necessary to allow time for the web page to load and for the browser to render the content before the next action is taken.
