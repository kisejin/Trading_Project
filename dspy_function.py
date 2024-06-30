import dspy

class FinanceStrategyGenerator(dspy.Signature):
    question = dspy.InputField(desc="Query of the finance strategy.")
    answer = dspy.OutputField(desc="The ```python``` code block.")

#FinanceStrategyGenerator.__doc__= instruction
    
class CSVDataset:
    def __init__(self, file_path, instruction=None) -> None:
        
        # Load the CSV file
        df = pd.read_csv(file_path)
        
        # Change name of the columns
        df.columns = ['question', 'answer']
        
        df = df.drop(columns=['answer'])
        
        # df = df.sample(frac=1).reset_index(drop=True)
        
        
        self.train = self._change_input(df.iloc[:30].to_dict(orient='records'))
        self.dev = self._change_input(df.iloc[30:].to_dict(orient='records'))
        
    
    def _change_input(self, input_data):
        
        ds = []
        for d in input_data:
            ds.append(dict(
                question=d['question'],
                # answer=d['answer']
            ))
        d = [dspy.Example(**x).with_inputs("question") for x in ds]
        return d
    
class GenerateCodeWithAssert(dspy.Module):
  def __init__(self, list_ohcl_data):
    super().__init__()
    self.generate_result = dspy.ChainOfThought(FinanceStrategyGenerator)
    self.ohcl_data = list_ohcl_data
    self.num_retry = 0
    self.flag = 0
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
    check, error = check_valid_code(BackTestStrategy, self.ohcl_data)
    # dspy.Assert(check, f"Fix error {error}")

    p_error = prompt_error(error=error)
    dspy.Suggest(check, f"{p_error}")
    # dspy.Suggest(check, f"The code must not obtain the error {error}")
    
    ex['num_retry'] = self.num_retry
    self.num_retry, self.flag = 0, 0
    # self.content_retrieve = None

    return ex

    