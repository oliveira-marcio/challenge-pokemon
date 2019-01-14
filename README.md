# Pokémon: Gotta Catch 'Em All

Challenge proposed in a job interview.

## The Challenge

Ash is catching pokémons in a world consisting of an infinite two-dimensional grid of houses. In every house there is exactly one Pokémon. Ash starts by picking up the Pokémon that is in the house where it starts. Next, move to the house immediately north, south, east or west from where you are and pick up the pokémon that is there, and so on. 

**Attention:** if he passes in a house where he has already passed (and therefore where he has already caught a pokémon), there is no more a pokémon for him to catch! What we want to know is: starting with a world full of pokémons (one in each house!), How many pokémons does Ash pick up for a given sequence of moves?

### Input format 

The program should read a line of stdin, which contains a sequence of moves. Each movement is described by a letter **N**, **S**, **E** and **W** (respectively: north, south, east, west).

### Output Format 

The program should write a line for stdout, just with a number: how many pokémons has Ash picked up?

**Examples:**

| **Input** | **Output** |
| --- | --- |
| **E** | 2 |
| **NESW** | 4 |
| **NSNSNSNSNS** | 2 |

### Technical Considerations 
- You can use the technological language / stack you prefer. However, with your source code, you need to provide us with the complete command that lets you compile (if necessary) and run your solution. 
- Your solution must be correct (from a functional point of view) and efficient (time spent, memory occupied, etc.). We suggest that you write tests that test your solution beyond the example inputs (larger inputs, badges, etc.), and include them in the source code you submit. 
- We also give (very) value to how understandable and organized your code is.

## The Solution

I've opted for using Python because of more friendly list operations.

So we have the following files:
- **[pokemon.py](pokemon.py)** - Main app that computates pokémons caught accordingly to provided movement list
- **[tests.py](tests.py)** - Unit tests with some case validations

## To run:

You need to have [Python](https://www.python.org/) installed. Open a terminal and type these commands:
- `python pokemon.py` - Run main app to inform movement list and get total pokémons caught.
- `python tests.py` - Run some unit tests

All code follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.

## Copyright

This app was developed by Márcio Souza de Oliveira.
