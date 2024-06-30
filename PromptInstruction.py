from utils import *

class PromptInstructions:
    """Prompt and instructions for the task."""
    """This class is used to store the prompt and instructions for the task. It also stores the base strategy, list of indicators, backtrader examples, and custom examples."""
    def __init__(self, base_strategy_path: str, list_indicator_path: str, backtrader_example_path: str, custom_example_path: str):
        self.base_strats = load_file(base_strategy_path)
        self.list_indicators = load_file(list_indicator_path)
        self.backtrader_examples = load_file(backtrader_example_path)
        self.custom_examples = load_file(custom_example_path)
        
        self.prompt = "Please create a strategy that buys when the price moves a certain percentage above the ATR value and sells when the price moves the same percentage below the ATR value"
        self.instruction = f"""
            You are a python developer that intent to make a workable trading strategy. Your task is to create a `BackTestStrategy` class that inherit from the `BaseStrategy` class given below and you MUST ONLY modify the `execute` function to follow human requirements.
            Here is the `BaseStrategy` class : 
            ```python\n{self.base_strats}```

            You are provided with list of indicators and description:
            {self.list_indicators}
            Here are two situations you need to handle :
            - SITUATION 1 : The provided list of indicators CONTAIN the indicator that human required, so you just use it follow this example :
            ```python\n{self.backtrader_examples}```

            - SITUATION 2 : The provided list of indicantors DO NOT CONTAIN the indicator that human required, so you try your best to create custom indicator follow this example :
            ```python\n{self.custom_examples}```
            """
            
def prompt_error(error: str, content: str = None):
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

        # list_content = "\n\n\n\n".join(content)
        # return f"""
        # With the {error}, you must correctly identify the indicator name using its alias, provide the correct function for the indicator, specify the correct input parameters (Params) for the indicator, using close price where applicable, and return the output value (Returns) of the indicator. Below is retrieve list correctly indicators:
        # {list_content}
        # """
        return f"""
        With the {error}, I refer you ignore the indicator by Backtrader package, instead that generate custom indicator following the given descriptions.
        """

    else:
        return f"The code must not obtain the error  {error}"

            
#t = PromptInstructions()
#print(t.prompt)
#print(t.instruction)
#print(t.base_strats)
            
