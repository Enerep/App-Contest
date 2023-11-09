import openai
openai.api_key = "sk-*********" # Secret OpenAI API key

# Funtion for making text requests to an OpenAI text generation model 
def chat(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-4-0314",
        messages = [{"role": "user", "content": prompt},
                    {"name": "DiceDecide","role": "system", "content": "CONSTRAINTS: If the input is not a prompt for different decisions, respond with a '--' and nothing else. You: The AI powering an app called DiceDecide. Task: Make a decision for the user, choose one of the options they propose. If applicable, base the decision off of logic, otherwise just for fun (a decision must be made). Format: Provide the chosen option (phrase or word). On a new line, a short fun explanation with an emoji if needed."}]
    )
    return response.choices[0].message.content.strip()

# Generating decision based on user's prompt
user_input = input("User: ")
response = chat(user_input)
print("Decision: ", response)

# Generating image prompt based on the decision DiceDecide made
imagePrompt = "Create a fun unrealistic image in connection to the object of this phrase: " + response.split('\n')[0]

# Feeding image prompt to an OpenAI image generation model
image = openai.Image.create(
  model="dall-e-3",
  prompt=imagePrompt,
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = image.data[0].url
print(image_url)
