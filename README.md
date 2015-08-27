# easy-selenium

Selenium is a powerful tool for web automation. But its APIs is a little bit complex for tester, and many developers are fighting for TimeoutException when page is slow.

To fix these, I created this module. It's a pretty small file but includes many features below:

* Use XPath to locate element
* Suport dynamic id
* Safely control page and elements
* Safely switch to Window, Frame and Lightbox

## Setup environment

First, you need to install selenium for python.

```
pip install selenium
```

Then put webdriver to your system environment path. I provided Chrome Driver for Mac OS X in drivers folder.

import easy-selenium module and use it!

``` python
from easyselenium import *

open('http://www.bing.com')
inputText('//*[@id=\"sb_form_q\"]', 'easyselenium')
click('//*[@id="sb_form_go"]')

```
