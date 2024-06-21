def load_file(file: str):
    """Loads content of file."""
    with open(file, "r") as f:
        contents = "\n".join(f.readlines())
    return contents



def prompt_error(error: str, content: str):
    """Returns a prompt for correctly the error."""
    if (
        "an unexpected keyword argument" in error
        or "module 'backtrader.indicators" in error
        or "not enough values to unpack" in error
    ):
        # return f"""With the {error}, you must correctly identify the indicator name using its alias, provide the correct function for the indicator, specify the correct input parameters (Params) for the indicator, using close price where applicable, and return the output value (Returns) of the indicator. Below is the list of indicators:
        # - Indicators List:
        # {load_file("/teamspace/studios/this_studio/test_backtrader/cleaned_text.txt")}
        # """
        
        list_content = "\n\n\n\n".join(content)
        return f"""
        With the {error}, you must correctly identify the indicator name using its alias, provide the correct function for the indicator, specify the correct input parameters (Params) for the indicator, using close price where applicable, and return the output value (Returns) of the indicator. Below is retrieve list correctly indicators:
        {list_content}
        """
        
    else:
        return f"The code must not obtain the error  {error}"
