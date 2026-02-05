# Copilot Instructions for jokes2025

## Project Overview
This is a simple Python script implementing an interactive knock-knock joke game. The main logic resides in `main.py`, with requirements documented in `notes.py`.

## Architecture
- **Single-script design**: All functionality in `main.py` with no external dependencies
- **Interactive flow**: Uses `input()` for user prompts and `print()` for responses
- **Loop-based gameplay**: `while` loop allows multiple joke iterations
- **Dictionary-based joke storage**: Centralized `joke_data` dict replaces sequential if/elif branches for scalability

## Key Patterns
- **Input handling**: Always use `input("prompt text")` for user interaction, e.g., `joke = input("Do you want to hear a joke? ")`
- **Dictionary-based data structure**: Jokes stored in `joke_data` dict with keys (robbers/tanks/pencils) and values containing setup/response/punchline fields
- **Response validation**: Use `in` operator for collection checks (e.g., `if question in joke_data`, `if friend in ["yes", "maybe"]`)
- **Rating calculation**: Convert 1-10 rating to percentage by multiplying by 10: `final_score = int(rate * 10)`
- **Exit conditions**: Check for `"finished"` to trigger rating flow, `"no"` for immediate exit
- **Function design**: `tell_joke(setup, response, punchline)` uses unpacking from dict and conditional printing; `get_rating()` handles rating and recommendation logic

## Developer Workflows
- **Run the game**: Execute `python main.py` from project root
- **No build process**: Direct Python execution, no compilation or packaging
- **No tests**: Manual testing through interactive runs

## Code Requirements (from notes.py)
- **Input/Output dependency**: All output must respond to user input via `input()`
- **List/Dict data structures**: Uses `joke_data` dict for scalable joke management (justifies dict usage for structured data with multiple properties)
- **Function requirements**: All functions must have parameters, use sequencing, selection, and iteration; code paths differ based on parameter values
  - `tell_joke(setup, response, punchline)`: sequencing (loop + multiple inputs), selection (if punchline/response), iteration (for loop even if range(1))
  - `get_rating()`: selection (if/elif for friend recommendations), sequencing (input → process → output)

## Common Modifications
- Add new joke categories by adding entries to `joke_data` dict with setup/response/punchline keys
- Add input validation (e.g., `.lower()` for case-insensitive comparison)
- Implement random joke selection from `joke_data.items()`
- Add logging or error handling for invalid rating inputs
- Extend `get_rating()` to store results to a file or database