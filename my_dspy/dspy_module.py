import dspy
from my_dspy.dspy_signature import FinanceStrategyGenerator


class GenerateCodeWithAssert(dspy.Module):
    def __init__(self, list_ohcl_data):
        super().__init__()
        self.generate_result = dspy.ChainOfThought(FinanceStrategyGenerator)
        self.ohcl_data = list_ohcl_data
        self.num_retry = 0
        self.flag = 0
        self.list_answer_retry = []
        # self.retrieve = dspy.Retrieve(k=3)
        # self.content_retrieve = None

    def forward(self, question):

        # if not self.content_retrieve:
        # self.content_retrieve = self.retrieve(question).passages
        # list_content = "\n\n\n\n".join(self.content_retrieve)

        ex = self.generate_result(question=question)

        if self.flag == 0:
            self.flag = 1
        else:
            self.num_retry += 1

        exec(get_code_from_text(ex.answer), globals())
        self.list_answer_retry.append(ex.answer)
        check, error = check_valid_code(BackTestStrategy, self.ohcl_data)
        # dspy.Assert(check, f"Fix error {error}")

        p_error = prompt_error(error=error)
        dspy.Suggest(check, f"{p_error}")
        # dspy.Suggest(check, f"The code must not obtain the error {error}")

        ex["num_retry"] = self.num_retry
        ex["list_answer_retry"] = self.list_answer_retry
        self.list_answer_retry = []
        self.num_retry, self.flag = 0, 0
        # self.content_retrieve = None

        return ex
