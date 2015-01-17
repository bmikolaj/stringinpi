#Find String in π
v1.0

##Description

String in Pi searches for the first occurance of any integer string in Pi.

##Dependencies
String in Pi was designed for Linux and uses the following programs;

* Python 2.7+
* Python `pip` (for installation; installed via setup.sh)
* Python module: `sympy` (installed via setup.sh)


##Install
* Clone git archive via the following command; 
  
  `git clone https://github.com/bmikolaj/stringinpi.git stringinpi`
* Change directories via `cd stringinpi`
* Run the following command to install;
  
  `sudo ./setup.sh install`

This will install the two dependancies: `pip` and `sympy`.

* If desired, copy the program to your bin directory via `sudo cp stringinpi.py /usr/local/bin/stringinpi.py`

##Usage
Run via the following command;

`stringinpi.py [-h] <integer>`

####Required parameters
`<integer>` is required.

####Optional parameters
`-h` for help

`--version` will print the version of `stringinpi.py` and exit.

###Example 
`user@computer:$ ./stringinpi.py 123`

`>>Searching for 123 in π`

`>>Starting Position of String: 1925`

`>>047_123_713`


##Uninstall
* Run the following command to uninstall;
  
  `sudo ./setup.sh uninstall`

##Changelog

* v1.0 (17 January 2015)

  Initial Release

##Author
[Brian Mikolajczyk](https://github.com/bmikolaj), brianm12@gmail.com

##Legal
Copyright (c) 2015, Brian Mikolajczyk, brianm12@gmail.com

###Licence
Please see file LICENCE.

###Copying
Please see file COPYING.
