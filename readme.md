# Pygame RPG-SDK

This is a work-in-progress SDK for building tile based RPGs using pygame.

## Requirements
* python 2.7+
* virtualenv
* pygame==1.9.2a0
* [Tiled](http://www.mapeditor.org/) - I'm currently using Tiled for map editing.

## Installation
I use virtual environements with all python projects, and have been doing so with this one.
To create a virtual environment, [follow these instructions](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

Once you have everything installed, create a virtual environment for this project: `virtualenv rpg-sdk`.

Now, `cd` into your virtualenv: `cd rpg-sdk` and clone this repository: `git clone git@github.com:jmbarne3/pygame-rpg-sdk.git src`.

Once everything has been cloned down you can install your python dependencies. `cd` into your `src` directory, activate your virtualenv and install dependencies:
```
cd src/
source ../bin/activate
pip install -r requirements.txt
```
If you have any problems installing pygame, see [the pygame website](http://www.pygame.org/download.shtml) for troublshooting tips.

## Running the game
Provided everything is installed properly, run `python app.py` to see whatever I currently have set as the default GameScreen

## Editing Maps
Due to the way Tiled saves references to the tilesets, I've written into the code a method that ignores the specific directory Tiled thinks a tileset image is. To make sure everything is working properly, just make sure your tileset is in the `res/tilesets/` directory and named the same thing as when you created the map. The name must be the same, or the code will be unable to load the image.

## Adding much more!
As I continue to develop this, I will add more information on the classes developed, as well as expand upon the comments in the code.
