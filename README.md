# DiceDecide: Your Personal Decision-Maker
Application Name: DiceDecide

**Participants Name(s):**
ABDULRAHMAN HERSI, BAT-OCHIR ARTUR ,YOUNES SLAOUI

**Short Bio Of Developer(s):**
- Younes Slaoui:
  - B.S. in computer science, University of New Mexico, class of 2025, currently in 3rd year.
  - Software engineer at Indica Labs working on biomedical software.
  - Leveraged machine learning and AI techniques to detect criminal activity during a Data Science internship with the U.S. Department of Homeland Security in summer 2023.
- Bat-Ochir Artur:
  - Personal Website: https://batochirajil.pythonanywhere.com
  - B.S. in computer science, University of New Mexico, class of 2025, currently in 3rd year.
  - Experienced self-learner with over 40 certifications from reputable institutions such as Stanford University, Google, SoloLearn and much more.
- Abdulrahman Hersi:
  - B.S. in economics and political science, University of New Mexico, class of 2026, currently in 2rd year.
  - Worked with marketing team for SABANTA, bio-tech company based in Saudi Arabia.

**Contact Information**
- Younes Slaoui:
  - Phone: (505)412-0866
  - Email: yslaoui@unm.edu
- Bat-Ochir Artur:
  - Phone: (505)303-6921
  - Email: bartur1@unm.edu
- Abdulrahman Hersi:
  - Phone: (505)523-5553
  - Email: ahd2035@unm.edu

# Introduction:
Welcome to DiceDecide, the app where your choices meet destiny. With the power of voice commands, visual inputs, and AI integration, decision-making becomes an interactive and engaging experience. Whether it's choosing an outfit, picking a dinner spot, or planning your day, DiceDecide is your go-to for making choices with a touch of fun.

# Capabilities:
* **_Voice Command Feature:_**
"Should I go for a run or read a book?" Just ask aloud. DiceDecide's voice recognition allows you to speak your options into existence. The app listens, understands, and rolls the virtual dice, delivering a decision with a clear educated text response.

* **_Visual Decision-Making:_**
Can't decide between the red dress or the blue one? Take a picture of both, and let DiceDecide choose for you. The app's visual recognition capabilities analyze the images and, with a roll of the AI dice, select the outfit that suits your day best.

* **_Personalization feature:_**
DiceDecide's "Personalization" section allows you to personalize your decision-making experience using data integration. With one tap you can sync your data for more personalized decisions. DiceDecide can use calendar, emails, live location and more to choose the optimal decision in any scenario. For example, sync your email for quick decision-making on invitations, sync your calendar to help choose between events, or provide your location for tailored decisions based on weather and time of day. This optional personalization allows DiceDecide to consider your schedule, preferences, and current situation when making decisions for you.
_We are dedicated to boosting your productivity through schedule integration all the while maintaining user privacy._ 

# Prototype _(Figma)_:
* Link for Figma prototype:

[Figma Prototype of DiceDecide](https://www.figma.com/file/NB4CRy1cHBQgNuOeH00CWF/Dice-Decide?type=design&node-id=0%3A1&mode=design&t=B4ohOpvabfwmjJUl-1) 

<sub>Raw Link: https://www.figma.com/file/NB4CRy1cHBQgNuOeH00CWF/Dice-Decide?type=design&node-id=0%3A1&mode=design&t=B4ohOpvabfwmjJUl-1<sub/>

* _Screenshots_:

<img width="200" alt="DiceDecide_Screenshot1" src="https://github.com/Enerep/App-Contest/assets/47132106/768d1f48-5d16-4682-a199-82cbd6de3e91">

<img width="200" alt="DiceDice_Screenshot2" src="https://github.com/Enerep/App-Contest/assets/47132106/72f90c0d-395e-453e-b502-bfb3b2c9ce5a">

<img width="177" alt="DiceDecide_Screenshot3" src="https://github.com/Enerep/App-Contest/assets/47132106/883e970a-9e64-4816-b815-c92973a180c8">

* _Video_:

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
  
- **AI-Powered Insights**: Not just a game of chance, DiceDecide uses the OpenAI API to provide a brief rationale for your decision, combining randomness with a touch of AI intelligence.
  
- **Multi-Option Flexibility**: Whether it's two choices or twenty, DiceDecide can handle multiple options with ease, ensuring every possibility gets a fair roll.
    
- **Decision Archives**: Keep a log of past decisions and outcomes to track the path of your choices over time.

# Description:

**Audience:**
DiceDecide is crafted for the modern individual who faces a world brimming with choices. Understanding that each user is unique, the app is designed to cater to a diverse audience with its adaptable features. 
Designed for, but not limited to: 
- The Decisive and Indecisive: Whether you're someone who relishes making quick decisions or you often find yourself hesitating at the crossroads of daily choices, DiceDecide is your ally.
- The Tech-Savvy and the Tech-Curious: It appeals to both the tech-savvy user who is at home with AI integration and the tech-curious who are just beginning to explore the possibilities of technology-enhanced decision-making.
- The Fashion-Forward and the Style-Seeker: Fashion enthusiasts can use DiceDecide to choose between outfits, accessories, or makeup styles, making it a valuable tool for those looking to refine their look.
- The Planner and the Spontaneous: The "Personalization" section is a haven for planners who love to have their life organized and in sync, and just as useful for spontaneous souls who prefer on-the-fly decisions.
- The Privacy-Conscious: Built with privacy at its core, it serves the needs of users who prioritize the security of their personal information with an optional "Personalization" section for personalized control.
  
**Security and Privacy:**
Your choices are yours alone. DiceDecide is built with a commitment to privacy, ensuring that all decisions are processed securely, with end-to-end encryption, and never stored longer than necessary. The "About Me" section is entirely optional and protected with robust security measures. Sync your details with peace of mind, knowing that DiceDecide values your privacy above all.

**Design:**
DiceDecide features a polished interface with fluid animations that simulate the thrill of rolling dice. Designed for intuitiveness, the app ensures a seamless and enjoyable experience across voice, or image inputs.

**User Experience:**
Upon launching Dice Decide, you're immediately immersed in a streamlined interface designed for clarity and ease of use. Input your options using the voice, or image inputs, and with a simple swipe, the virtual dice roll to determine your choice. The tactile feedback enhances the experience, adding a sense of physical interaction.
After the roll, the chosen option is displayed alongside a "Learn More" button. Tapping this reveals a concise explanation from the OpenAI API, providing insights into the decision-making process. This feature enriches the user experience by offering a clear rationale behind the AI's choice, tailored to your personal context and preferences.

**Conclusion:**
DiceDecide isn't just an app! It's a decision-making partner that adds a dash of excitement to your daily choices. It's perfect for the indecisive, the adventurous, and everyone in between. Say goodbye to decision paralysis and hello to DiceDecide – where every roll is a new adventure! Embrace the power of choice with DiceDecide – where your voice, your images, and your life help shape your destiny.

**Future Plans**
We are committed to continuous improvement and innovation. DiceDecide will evolve through continuous iteration, integrating user feedback and preferences to enhance decision-making. We aim to expand third-party integrations for richer, more informed choices. We will be consistently working on new features and updates to enhance the functionality of DiceDecide. We envision DiceDecide evolving into more than just a personal assistant. We aim to create a versatile tool that can be used for a variety of purposes, such as education, entertainment, and productivity. Our vision is to transform DiceDecide into a comprehensive AI assistant, fully in sync with your schedule, crafting daily or weekly plans aligned with your objectives and data. We are excited about the future of DiceDecide and we are committed to providing our users with the best possible experience.
