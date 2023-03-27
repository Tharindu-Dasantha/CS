import pyperclip
import copy


# add a list to a clipboard

# Paste text from the clipboard
text = pyperclip.paste()

# Separate lines and add stars
lines = list(text.split("\n"))
corrected = []
for line in lines:
    line = copy.deepcopy(f"* {line}")
    corrected.append(line)
    
new_text = '\n'.join(corrected)
pyperclip.copy(new_text)