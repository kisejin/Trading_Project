
def prompt_error(error: str, content: str = None):
    """Returns a prompt for correctly the error."""
    if error:
        show_error = f"{error[0]}. This error occurs in the following function:\n {error[1]}\nError location: {error[-1]}"
        
        if (
            "an unexpected keyword argument" in error
            or "module 'backtrader.indicators" in error
            or "not enough values to unpack" in error
        ):
            # return f"""With the {error}, you must correctly identify the indicator name using its alias, provide the correct function for the indicator, specify the correct input parameters (Params) for the indicator, using close price where applicable, and return the output value (Returns) of the indicator. Below is the list of indicators:
            # - Indicators List:
            # {load_file("/teamspace/studios/this_studio/test_backtrader/cleaned_text.txt")}
            # """

            # list_content = "\n\n\n\n".join(content)
            # return f"""
            # With the {error}, you must correctly identify the indicator name using its alias, provide the correct function for the indicator, specify the correct input parameters (Params) for the indicator, using close price where applicable, and return the output value (Returns) of the indicator. Below is retrieve list correctly indicators:
            # {list_content}
            # """
            
            return f"""
            With the `ERROR MESSEAGE` {show_error}.\n I refer you ignore the indicator by Backtrader package, instead that generate custom indicator following the given descriptions.
            """

        else:
            return f"""
            The code must avoid the {show_error}"""
    return ""
