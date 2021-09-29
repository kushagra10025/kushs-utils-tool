
## TODO
* Detect File type and write the template for that file in there ```directory.py```
* Command Line Args Support ```kush-util.py``` - DONE
	* Improve the support with more detailed documentation
* Multiple Progamming Language Support
```kush-util.py > cmd line```
* Custom Structre Generator for difference languages ```template.py```
	* Use Json to store the tree structs with a unique language identifier
	* Modify this Json file to change the structre of the project
	* Load Json at runtime
	* create a tool to make json through commandline
* Change default paths depending on OS ```globals.py```
* Allow for ability to customize default through a json file ```globals.py```
* Define Parser Groups ```cli_args_parser.py```
* Determine a way to find if the Project has been created by the Util Program

## Resources
* Argparse Nester Parser - https://www.youtube.com/watch?v=3tSq5Yo2e2o&ab_channel=CodingWisdom
* PyInstaller Packaging - https://www.youtube.com/watch?v=s-lKHA9o_pY&ab_channel=SouravJohar
	
## Learnings from this project
* Chaining different optional arguments with a positional argument like in git
	* Use SubParser and SubCommands
	
* Positional arguments are compulsory ones, Eg:```curl <url>``` <url> - Positional Arguments

* Optional Arugments are optional, Eg:
	```
	curl --version
	curl --help
	```

* Group - Visual Representation of differentiating data "Does not make subcommands"
* SubParser - Parser withing a parser for Chaining commands