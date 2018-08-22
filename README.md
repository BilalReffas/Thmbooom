![](https://imgur.com/DhH1S3P.png)
# Thmbooom
thmbooom is a simple script to download lecture slide from Technical University of Applied Science Gießen [THM Moodle](https://moodle.thm.de/login/index.php)

# Dependencies 
It's important you have Firefox installed on you're local machine to make thmbooom happy, because thmboom is using the Firefox driver.
As well thmbooom is usign some awesome dependecies like selenium to access all functionalities of Selenium WebDriver in an intuitive way and beautifulsoup for easy parsing. 

Make sure to install those dependecies 
* `pip install selenium`
* `pip install beautifulsoup4`
* `pip install lxml`
* `pip install requests`

# Geckodriver
Install geckodriver on your local machine to interact with Gecko-based browsers.

* macOS <br>
  `brew install geckodriver`
* Linux
  ```
  wget https://github.com/mozilla/geckodriver/releases/download/v0.16.1/geckodriver-v0.16.1-linux64.tar.gz
  sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.16.1-linux64.tar.gz -O > /usr/bin/geckodriver'
  sudo chmod +x /usr/bin/geckodriver
  rm geckodriver-v0.16.1-linux64.tar.gz
   ```

# Installation
You can use pip to install the module
```pip install thmbooom```

# Requirement's 
Python 3 +

### Author

  [@reffas_bilal](https://twitter.com/Reffas_Bilal)
  
  [bilalreffas@googlemail.com]()

### Thank you 

  If you like this project please leave a star here on Github and share it.

### License

```
MIT License

Copyright (c) 2018 Bilal Reffas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
