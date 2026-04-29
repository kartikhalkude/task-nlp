from utils.parse_task import parse_natural_language_task


sample_input = "Finish internship assignment tonight and prepare the decision log"

result = parse_natural_language_task(sample_input)

print(result)