def get_code_from_text(text):
    """Extracts the Python code segment from the provided text."""
    # print("Text",text)
    code_segment = text
    if "```" in text:
        code_segment = code_segment.split("```")[1]
    if "python" in text:
        code_segment = code_segment[code_segment.find("python")+6:]
    return code_segment.strip()

def load_base_strategy(file_path):
    """Loads the base strategy code from the base_strategy.py file."""
    with open(file_path, "r") as f:
        base_strats = "\n".join(f.readlines())
    return base_strats

def extract_error_message(error):
    error_lines = str(error).split('\n')
    for line in error_lines:
        if 'Error' in line or 'Exception' in line:
            return line.strip()
    return error_lines[-1].strip()

def load_file(file: str):
    """Loads content of file."""
    with open(file, "r", encoding='utf-8') as f:
        contents = "\n".join(f.readlines())
    return contents



#text = load_file("cleaned_text.txt")

#texts = text.split("\n\n\n\n")
#print(texts)