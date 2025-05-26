import wikipedia                                
import pyttsx3                   

repeater = 1

def speak(string):               
    engine = pyttsx3.init()
    engine.say(string)
    engine.runAndWait()

def search():                                    
    speak("Tell about the word to search")
    text = input("Enter the word you want to search (or type 'stop' to exit): ").strip().lower()

    if text in ["stop", "thank you"]:
        print("Bye")
        return 1
    elif text == "":
        speak("You didn't enter anything. Please try again.")
        return 0
    else:
        print("Searching for:", text)
        try:
            result = wikipedia.summary(text, sentences=1)
            print("Wikipedia search result:", result)
            speak(result)
        except wikipedia.exceptions.DisambiguationError:
            speak("The word is too ambiguous. Try to be more specific.")
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find anything related to that.")
        except Exception as e:
            speak("An error occurred while searching.")
            print(f"Wikipedia error: {e}")
        return 0

speak("Hi, I am your assistant.")                 
while repeater == 1:
    checker = search()
    if checker == 1:
        repeater = 0
speak("It is my pleasure to help you. See you again. Bye.")
