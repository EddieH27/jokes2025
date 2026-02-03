# Copilot Instructions for jokes2025

## Project Overview
This is a simple Python script implementing an interactive knock-knock joke game. The main logic resides in `main.py`, with requirements documented in `notes.py`.

## Architecture
- **Single-script design**: All functionality in `main.py` with no external dependencies
- **Interactive flow**: Uses `input()` for user prompts and `print()` for responses
- **Loop-based gameplay**: `while` loop allows multiple joke iterations
- **Conditional joke selection**: `if/elif` chain for robber/tank/pencil jokes

## Key Patterns
- **Input handling**: Always use `input("prompt text")` for user interaction, e.g., `joke = input("Do you want to hear a joke? ")`
- **Response validation**: Simple string comparison (`== "yes"`, `== "finished"`) without case handling
- **Rating calculation**: Convert 1-10 rating to percentage by multiplying by 10: `final_score = int(rate * 10)`
- **Exit conditions**: Check for `"finished"` to break loops, `"no"` for immediate exit

## Developer Workflows
- **Run the game**: Execute `python main.py` from project root
- **No build process**: Direct Python execution, no compilation or packaging
- **No tests**: Manual testing through interactive runs

## Code Requirements (from notes.py)
- **Input/Output dependency**: All output must respond to user input
- **List justification**: Use lists when picking items or random selections (not currently implemented)
- **Function requirements**: Functions must have parameters, use sequencing, selection, and iteration
- **Path variation**: Code paths should differ based on parameter values

## Common Modifications
- Add new joke categories by extending the `if/elif` chain in the main loop
- Implement list-based random joke selection for variety
- Add input validation (lowercase conversion, yes/no normalization)
- Create functions for joke telling to meet requirements in notes.py