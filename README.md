
# Kush's Utils Tool
![Logo For Utils Tool](https://i.ibb.co/wS77tRZ/utils-logo.png)
**Kush's Utils Tool** is my personal collection of scripts which is used to automated daily tasks. It is a evergrowing collection of scripts and will continue to evolve till the day I program. This is also my first python project.
> Ever evolving project. May see major rework at at anypoint of time

> Current version - 0.0.2

## Features
* Project Structure creator for a given language (currently cpp only)
* Amazon.in Price Tracker with Email alert (from Hacktober Contribution)
* Random Dice Rolls and Coin Toss (from Hacktober Contribution)
* More scripts will be added soon and the tool will be extended as and when need be...

> NOTE: Some Hacktober contributions though pulled have been held for integration later. Check back at later to see their integration.

## Usage
> ```kush-util.py``` is the entry point. Other files are helpers.

***First Level Arguments***

Usage : ```python kush-util.py <command> [opt-args]```
| CLI Arguments |  Type  | Description|
| ------------- | :----: |-------------:|
| -h, --help    |opt-args| Show help for commands | 
| -v, --version |opt-args| Show version for the utils program| 
| create 		|pos-args| Create project from templates|
| modify 		|pos-args| Modify project templates metadata|
| delete		|pos-args| Delete project folder created using utils|
| hackto		|pos-args| Utility scripts by community during Hacktober|

***For Creating a Project - Second Level Arguments***

Usage : ```python kush-util.py create [opt-args]```

| CLI Arguments |  Type  | Description|
| ------------- | :----: |-------------:|
| -h, --help    |opt-args| Show help for create | 
| --plang		|opt-args| Specify Projects Programming Language| 
| --pname		|opt-args| Specify Projects Name|
| --pname		|opt-args| Specify Projects Path|

***For Accessing Hacktober Contributions - Second Level Arguments***

Usage : ```python kush-util.py hackto <hackto_command> [opt-args]```

| CLI Arguments |  Type  | Description|
| ------------- | :----: |-------------:|
| -h, --help    |opt-args| Show help for create | 
| random		|pos-args| Random Chance Things| 
| price_alert	|pos-args| Get Price alert for Amazon.in products|

***For Accessing Price Alert Scripts - Third Level Arguments***

Usage : ```python kush-util.py hackto price_alert <command> [opt-args]```

| CLI Arguments |  Type  | Description|
| ------------- | :----: |-------------:|
| -h, --help    |opt-args| Show help for create | 
| url			|pos-args| URL for the product | 
| eprice		|pos-args| Expected price in INR for the product|
| --s_email		|opt-args| Sender Email (set default in globals)|
| --s_pass		|opt-args| Sender Password (set default in globals)|
| --r_email		|opt-args| Receiver Email (set default in globals)|

***For Accessing Random Generators Scripts - Third Level Arguments***

Usage : ```python kush-util.py hackto random [opt-args]```

| CLI Arguments |  Type  | Description|
| ------------- | :----: |-------------:|
| -h, --help    |opt-args| Show help for create | 
| --roll_dice	|opt-args| Roll a Double Dice!|
| --toss_coin	|opt-args| Toss a Coin!|
| --sort_hat	|opt-args| Get sorted at Hogwartz!|

## Running
1. Create a virtualenv
2. Get the required packages through pip from requirements.txt
3. Run the ```kush-util.py``` script with the required args.

## Requirements

* [pathlib](https://docs.python.org/3/library/pathlib.html) - ```Approach for pathlib usage:```
	* create directory if not exist
	* create file if not exist and populate specific filetype with predefined templates
	* basically filesystem related tasks.
* [anytree](https://pypi.org/project/anytree/) - ```Approach for anytree usage:```
	* store project and directory structure as tree
	* check if leaf is file then create the file with a predefined template
	* if the leaf is a directory keep the directory empty
* [argparse](https://docs.python.org/3/library/argparse.html) - ```Approach for argparse usage:```
	* multiple sub-parser for major commands
	* args in the sub-parsers for major commands specific feature
	* inspiration for chained arguments taken from ***git*** cli.
* [requests](https://pypi.org/project/requests/) - ```Approach for requests usage:```
	* get the webpage locally in a machine readable format
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) - ```Approach for beautifulsoup4 usage: ```
	* for the webpage from requests scrap required ids and classes
* [smtplib](https://docs.python.org/3/library/smtplib.html) - ```Approach for smtplib usage:```
	* sending emails - currently gmail only using smtp
* [cowsay](https://pypi.org/project/cowsay/) - ```Approach for cowsay usage```
	* for adding fun element in printing on CLI screen.

## Contributing
> **NOTE:** Check the TODO before opening issues to check if it is detected and is being worked upon.

This project is open to and encourages contributions! Feel free to discuss any bug fixes/features in the **issues**. If you wish to work on this project and extend it with your own daily usage scripts:

1.  Fork this project
2.  Create a branch (`git checkout -b new-branch`)
3.  Commit your changes (`git commit -am 'add new feature'`)
4.  Push to the branch (`git push origin new-branch`)
5.  Submit a pull request!
