import openai

openai.api_key = "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"

def generate_text(user_question):
    completions = openai.Completion.create(
        engine="text-curie-001",
        #engine="davinci",
        prompt=user_question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    response = generate_text(user_input)
    print("GPT-3: " + response)



# import openai

# # Set the API key
# openai.api_key = "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"

# # Generate text
# model_engine = "text-davinci-002"
# prompt = "Hello, my name is Claudio. I am interested in learning about your questions"

# completions = openai.Completion.create(
#     engine=model_engine,
#     prompt=prompt,
#     max_tokens=1024,
#     n=1,
#     stop=None,
#     temperature=0.5,
# )

# message = completions.choices[0].text
# print(message)
