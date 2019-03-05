# honorifics
Swaps terms in ass subtitles with alternatives, useful for handling Japanese honorifics.

## scripts/

Scripts can run by in-system Python. All scripts reads from stdin and output to stdout.

### subtitles.py

Read line by line.
If in line is text between marks {\*}...{\*...} then swap it. 
Marks can be changed by providing arguments to class TextSwapperInMark constructor in script.

### Example

`python3 ./scripts/subtitles.py < input > output`
