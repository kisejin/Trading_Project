def clean_string(string):
	return string.strip().replace('\t', '')

def process_string(string):
	lines = string.split('\n')
	filtered_lines = [line for line in lines if '-----' not in line and 'Note' not in line and 'Filename' not in line]
	return '\n'.join(filtered_lines)


def get_root_cause_error(string):
    messages = [process_string(clean_string(string)) for string in string.split("===================================================")]
    root_error = [m for m in messages if "ROOT CAUSE" in m][0]
    root_error = root_error.split("\n")
    root_error = [root_error[-1].replace(" -->ROOT CAUSE:", "").strip()] + root_error[:-1]
    return root_error