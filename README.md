# DiceDecide: Your Personal Decision-Maker
Application Name: DiceDecide

**Participants Name(s):**
ABDULRAHMAN HERSI, BAT-OCHIR ARTUR ,YOUNES SLAOUI

# Introduction:
Welcome to Dice Decide, the app where your choices meet destiny. With the power of voice commands, visual inputs, and AI integration, decision-making becomes an interactive and engaging experience. Whether it's choosing an outfit, picking a dinner spot, or planning your day, Dice Decide is your go-to for making choices with a touch of fun.

# Capabilities:
* **_Voice Command Feature:_**
"Should I go for a run or read a book?" Just ask aloud. Dice Decide's voice recognition allows you to speak your options into existence. The app listens, understands, and rolls the virtual dice, delivering a decision with a clear educated text response.

* **_Visual Decision-Making:_**
Can't decide between the red dress or the blue one? Take a picture of both, and let Dice Decide choose for you. The app's visual recognition capabilities analyze the images and, with a roll of the AI dice, select the outfit that suits your day best.

* **Personalization feature**
DiceDecide's "Personlization" section allows you to personalize your decision-making experience using data integration. With one tap you can sync your data for more personalized decisions. DiceDecide can use calendar, emails, live location, past data, and more to choose the optimal decision in any scenario. For example, sync your email for quick decision-making on invitations, sync your calendar to help choose between events, or provide your location for tailored decisions based on weather and time of day. This optional personalization allows DiceDecide to consider your schedule, preferences, and current situation when making decisions for you.
_We are dedicated to boosting your productivity through schedule integration all the while maintaining user privacy._ 

# Prototype _(Figma)_:
[Figma Prototype of DiceDecide](https://www.figma.com/file/NB4CRy1cHBQgNuOeH00CWF/Dice-Decide?type=design&node-id=0%3A1&mode=design&t=B4ohOpvabfwmjJUl-1)

https://github.com/Enerep/App-Contest/assets/47132106/090875a2-b71c-4a8b-b39e-c90babc51f92

**DiceDecide API Code:**
```python
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
```
# Key Features:

- **Roll the Dice**: Simply enter your options and let the virtual dice roll. The outcome? An educated selected choice to keep things exciting and spontaneous.
  
- **AI-Powered Insights**: Not just a game of chance, DiceDecide uses the ChatGPT API to provide a brief rationale for your decision, combining randomness with a touch of AI intelligence.
  
- **Multi-Option Flexibility**: Whether it's two choices or twenty, Dice Decide can handle multiple options with ease, ensuring every possibility gets a fair roll.
    
- **Decision Archives**: Keep a log of past decisions and outcomes to track the path of your choices over time.
  
**Security and Privacy:**
Your choices are yours alone. Dice Decide is built with a commitment to privacy, ensuring that all decisions are processed securely, with end-to-end encryption, and never stored longer than necessary. The "About Me" section is entirely optional and protected with robust security measures. Sync your details with peace of mind, knowing that Dice Decide values your privacy above all.

**Design:**
The app boasts a sleek, intuitive interface with rich animations that bring the excitement of rolling dice to your fingertips. The app's design ensures that whether you're using voice, text, or images, the process is intuitive and enjoyable.

**User Experience:**
Upon launching DiceDecide, you're greeted with a minimalist interface prompting you to input your options. Once entered, a simple swipe gestures the dice to roll with a satisfying tactile feedback. The screen then elegantly transitions to present the chosen option, accompanied by a concise, informative blurb from ChatGPT that might just make you see your choice in a new light.

**Conclusion:**
DiceDecide isn't just an app; it's a decision-making partner that adds a dash of excitement to your daily choices. It's perfect for the indecisive, the adventurous, and everyone in between. Say goodbye to decision paralysis and hello to DiceDecide – where every roll is a new adventure! Embrace the power of choice with DiceDecide – where your voice, your images, and your life help shape your destiny.

**Future Plans**
We are committed to continuous improvement and innovation. We will be consistenly working on new features and updates to enhance the functionality of DiceDecide. We envision DiceDecide evolving into more than just a personal assistant. We aim to create a versatile tool that can be used for a variety of purposes, such as education, entertainment, and productivity. We are excited about the future of DiceDecide and we are committed to providing our users with the best possible experience
