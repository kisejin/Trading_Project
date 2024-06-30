import dspy



class FinanceStrategyGenerator(dspy.Signature):
    question = dspy.InputField(desc="Query of the finance strategy.")
    answer = dspy.OutputField(desc="The ```python``` code block.")