# Turing Machine Simulation with Pygame

This is a Turing Machine simulation program implemented using the `pygame` library. The program displays a tape of symbols, which the Turing Machine reads and modifies according to the provided set of instructions.

## How It Works

The Turing Machine is a mathematical model of computation that uses an infinite tape to read and write symbols, based on a series of rules defined in a text file. The tape is represented as a series of cells, and the read/write head moves across the tape according to the instructions.

## Features
- **Tape Display:** The tape of symbols is graphically represented and can move left or right.
- **Read/Write Head:** The head is visually represented by a triangle and moves along the tape.
- **Custom Instructions:** The instructions and initial tape configuration are loaded from text files.
- **Final Message:** The program displays a message indicating whether the machine accepted or rejected the input.

- The tape (`tape.txt`) and instructions (`instructions.txt`) are loaded at runtime, and the machine will modify the tape according to the instructions.
- In this example, the initial tape is `110011`, and the machine will perform its steps, modifying the tape and moving left or right based on the instructions in order to solve the problem.


## Requirements

- Python 3.x
- Pygame Library

To install Pygame, use pip:

```bash
pip install pygame
```

## How to run it

```bash
Upload you string in tape.txt
Example: 11011
```


Upload the machine turing code in instructions.txt
It should lokk something like that:

```bash
current_state, symbol_read
new_state, symbol_write, head_movement
```


```bash
python3 turing.py <running speed>
```

In instructions.txt you have an example for checking is a string is palindrome



