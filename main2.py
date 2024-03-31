from raptor import RetrievalAugmentation

# Initialize with default configuration. For advanced configurations, check the documentation. [WIP]
RA = RetrievalAugmentation()
SAVE_PATH = "demo/workato_recipe_3424670"

RA = RetrievalAugmentation(tree=SAVE_PATH)

question = """
    Describe the following for step 2 in workato recipe code analysis:
    1. Provider: The service provider or platform used to perform the action.
    2. Name: The name or identifier of the action.
    3. Input_Parameters: The input data required for the action, including any configurations or settings.
    4. Output_Parameters: The expected output or result of the action.
    5. Summarize the logic
    Response in JSON format in the following:
    provider
    name
    input
    output
    summary
"""

answer = RA.answer_question(question=question)
print("Answer: ", answer)
