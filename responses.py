from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup", "yo","Who are you?", "help"):
        return "Hey dear customer, how are you? \n\n I am the Kuldeep's Houseplant shop Bot! \n\n Nice to meet You! \n\n Please enter a houseplant you are looking for!"


    if user_message in ("rose", "jasmine", "money plant", "date palm", "daisy", "arrow head", "royal palm"):
        return "Cheers! This plant is currently available in our store \n\nPlease contact us at the given number in description to know more. \n \n\nIf you want to look for more plants, enter another plant name!"

    if user_message in ("palm"):
        return "Which type of palm, specifically?"

    if user_message in ("marijuana"):
        return "No sir! Ours is a lawful business. Please do not make such requests. \n\n Please enter another LEGAL houseplant name!"

    if user_message in ("bye", "exit", "thanks", "ok"):
        return "Sat-Sri-Akaal, Namaste! Please contact us again, dear customer!"

    if user_message in ("time", "time?", "date"):
        now = datetime.now()
        date_time = now.strftime("The date is %d-%m-%y")
        return str(date_time)

    return ("Our apologies, we do not currently have this plant at our store. \n\n But no worries! Contact us at our number so that we can arrange it for you!")
