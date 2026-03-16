# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- Answer:
  - The program at execution looked very good at first; I had no issues with the interface or entering my inputs to guess a number. However, once I got to actually playing the game, that is where I ran into some issues. For starters, the hints feature was giving me incorrect hints. Afterwards, I realized that I could enter negative numbers and numbers above the accepted range without the program stopping me.  

  - Bugs
    - Game was accepting negative inputs
    - The "name game" feature was not working
    - The hints were incorrect. When i placed a number lower than the secret number, the hints were telling me to go lower instead of higher
    - The history for the inputs seems to be off
    - Program accepts floating point numbers

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- Answer:
  - The only AI tool I used for this project was the Claude extension on VS Code, which provided great assistance in fixing some of the bugs I found. For instance, when I stumbled upon the issue of the program originally providing reversed hints, I presented it to Claude, and it suggested simply swapping the return output, which turned out to be correct upon testing and playing with the fix. Perhaps luckily for my case, Claude actually did not provide a suggestion that was incorrect or misleading. This is perhaps due in part to my understanding of the code and pointing to where exactly the issue is. However, I can see where AI can provide misleading results, as it has happened in the past. I believe that it all comes down to knowing how to properly use AI as a tool and not just mindlessly accept whatever it suggests.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

- Answer
  - To decide whether a bug was truly fixed, I used pytest, as suggested by the project description, and attempted to break the code. For instance, after fixing the reveresed hints, i used the two pytests that Claude provided and I began toying around with the program which revealed that the hints were working partially correct as i stumbled upon another bug where if the secret number was lower than my current guess, the first hint would tell me to go lower but after inputting another higher number the hint woukd tell me to go higher rather than lower. The use of the tests is what actually led me to go further with "breaking the code," which has also led me to understand the code's design.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

- Answer
  - In my own testing of the game at first hand, I actually did not notice the secret number kept changing throughout a game. I only realized this was an issue upon reading the project's description and asking Claude if this was actually an issue, in which he explained that throughout the debugging, there was something that was causing the secret number to change, and that was "attempts % 2 == 0" which was removed. This part of the code was removed because it was interfering with a bug I found where the game did not allow the user to start a new game at any given time, and from my understanding, this was making the secret number become a string on even attempts, which caused things to break.

 The way I would explain Streamlit's reruns and session state is to look at it as a sort of loop. At each iteration of a loop, like a rerun, allows us to do things in accordance with the iterator, as in the case with Streamlit's inputs.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

- Answer
  - The one habit I would want to reuse in future projects is the ability to properly use AI. By this, I mean not just mindlessly giving an AI tool prompts and accepting whatever it yields, but actually working with the tool and not the tool working for me in a way or alone. I believe this is a skill that could be valuable in the near future with the increase in AI. 
  - Something I would do differently when working with AI, which has also changed the way I think about AI-generated code, prompting correctly. Before this project, my use of AI was essentially giving the tool a brief description of what I needed and just copying and pasting. The issue with this is that sometimes AI will yield misleading suggestions due to the lack of context, and two, I learn nothing. This project and the current CodePath's AI110 course have opened my eyes to the true potential that AI tools carry. They do not merely provide a straight answer to a given problem, but they also bring true teamwork with the one using the tool and deep insights into developing software. 
