# Pi-Order

An automated system for ordering products from Amazon.com

## How To Use

#### 1. Fill Out User Info Form 
* Open a web browser and navigate to [http://joedye.me/pi-order/](http://joedye.me/pi-order/)
* Fill out the requested user information then submit
* The next page will give you a table indicating the traffic light colors for each product (Green Means Go)

#### 2. Connect Pi-Order to Wifi
* Connect Pi-Order to your internet via ethernet cable
* Allow the Pi-Order to boot up
* If a Green Light appears then your Pi-Order is connected to your wifi
* If you see a blinking Red Light there was a error. Make sure wifi info. is correct

#### 3. Reboot Pi-Order 
* Unplug the Pi-Order from the power outlet then from the ethernet connection
* Place Pi-Order where you would like it to reside then plug back into a power outlet
* Green Light means you are good to go, blinking Red Light means there was an error 

#### 4. Select Product for Ordering 
* Spin selection knob until the lighting tree shows the colors corresponding to the product you would like to order
* Press the order button
* The light tree will then change to Red-Yellow Light meaning your order is being processed

#### 5. Watch Traffic Light for Order Status
* The lighting tree will either show a green light or a red light based on whether the order was processed correctly
* If the lighting tree shows red then try submitting the order again and make sure product info is correct

## Deployment

Some notes about creating your own

## Built With
#### Automation
* [Selenium](http://docs.seleniumhq.org/) - Web Driver
* [Pyvirtualdisplay](https://pypi.python.org/pypi/PyVirtualDisplay) - Headless Browser Instances

#### Web App and Server
* [Body-Parser](https://github.com/expressjs/body-parser) - Parse HTTP Requests
* [Express](http://expressjs.com/) - Web Framework
* [Jsonfile](https://www.npmjs.com/package/jsonfile) - Read/Write JSON Data
* [Pug](https://www.npmjs.com/package/pug) - Templating engine
* [Python-Shell](https://github.com/extrabacon/python-shell) - Run Python From Node

#### Raspberry Pi Hardware Control
* [Requests](http://docs.python-requests.org/en/master/) - Handle HTTP Requests
* [Json](https://docs.python.org/2/library/json.html) - Parse JSON Data
* [Pexpect](https://pexpect.readthedocs.io/en/stable/) - Ensure Commands were Executed Properly
* [Wifi](https://wifi.readthedocs.io/en/latest/) - Setting Up Wifi Connections on RPi

#### Languages
* [Python3](https://www.python.org/) - RPi Hardware Control and Web Automation
* [NodeJS](https://www.nodejs.org/) - Web Application Creation and HTTP Request Control

## Authors

* **Jayson Perkins** - Hardware Control, Automation, HTTP Request Control - [jperk51](https://github.com/jperk51)
* **Joe Dye** - Automation, Initial Web Application, Server Management - [dyej](https://github.com/dyej)
* **Corey Ferris** - Final Web Application, Web Application Styling - [cferris32](https://github.com/cferris32)

See also the list of [contributors](https://github.com/dyej/pi-order/graphs/contributors) who participated in this project.


