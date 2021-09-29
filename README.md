
# Kush's Utils Tool
![Logo For Utils Tool](https://i.ibb.co/wS77tRZ/utils-logo.png)
**Kush's Utils Tool** is my personal collection of scripts which is used to automated daily tasks. It is a evergrowing collection of scripts and will continue to evolve till the day I program. This is also my first python project.
> Ever evolving project. May see major rework at at anypoint of time
> Current version - 0.0.1

## Features
* Project Structure creator for a given language (currently cpp only)
* More scripts will be added soon and the tool will be extended as and when need be...

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

***For Creating a Project - Second Level Arguments***
Usage : ```python kush-util.py create [opt-args]```

| CLI Arguments |  Type  | Description|
| ------------- | :----: |-------------:|
| -h, --help    |opt-args| Show help for create | 
| --plang		|opt-args| Specify Projects Programming Language| 
| --pname		|opt-args| Specify Projects Name|
| --pname		|opt-args| Specify Projects Path|

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

## Contributing
> **NOTE:** Check the TODO before opening issues to check if it is detected and is being worked upon.

This project is open to and encourages contributions! Feel free to discuss any bug fixes/features in the **issues**. If you wish to work on this project and extend it with your own daily usage scripts:

1.  Fork this project
2.  Create a branch (`git checkout -b new-branch`)
3.  Commit your changes (`git commit -am 'add new feature'`)
4.  Push to the branch (`git push origin new-branch`)
5.  Submit a pull request!
