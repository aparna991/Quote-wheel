import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Quote Wheel")

# Label for the Quote Wheel
quote_wheel_label = tk.Label(root, text="Quote Wheel", font=("Helvetica", 20,"underline"))
quote_wheel_label.pack()

# Function to switch to the Quote categories menu
def show_quote_categories():
    start_button.pack_forget()
    quote_button.pack()
    caption_button.pack()
    inspirational_button.pack_forget()    
    funny_button.pack_forget()   
    happy_button.pack_forget()    
    sad_button.pack_forget() 
    back_button.pack_forget()
    quote_label.config(text="")

# Start button
start_button = tk.Button(root, text="Start", command=show_quote_categories, highlightthickness=0, bd=2, font=("Lucida", 16), bg="yellow")
start_button.pack(pady=20)

# Function to show Inspirational or Funny quotes
def show_quote_category():
    start_button.pack_forget()
    quote_button.pack_forget()
    caption_button.pack_forget()

    inspirational_button.pack()
    funny_button.pack()
    back_button.pack()

# Function to show Positive or Negative captions
def show_caption_category():
    start_button.pack_forget()
    quote_button.pack_forget()
    caption_button.pack_forget()

    happy_button.pack()
    sad_button.pack()
    back_button.pack()

# Buttons for Quotes and Captions
quote_button = tk.Button(root, text="Get Quote", command=show_quote_category)
quote_button.pack_forget()

caption_button = tk.Button(root, text="Get Caption", command=show_caption_category)
caption_button.pack_forget()


# Buttons for Quote categories
inspirational_button = tk.Button(root, text="Inspirational", command=lambda: display_quote(inspirational_quotes))
funny_button = tk.Button(root, text="Funny", command=lambda: display_quote(funny_quotes))
happy_button = tk.Button(root, text="happy", command=lambda: display_quote(happy_captions))
sad_button = tk.Button(root, text="sad", command=lambda: display_quote(sad_captions))

# List of quotes for different categories
inspirational_quotes = [
"Success is not the key to happiness, Happiness is the key to success, If you love what you are doing, you will be successful.",
"Your time is limited, don't waste it living someone else's life." ,
"Strive not to be a success, but rather to be of value." ,
"The future belongs to those who believe in the beauty of their dreams." ,
"Don't watch the clock; do what it does. Keep going.",
"It always seems impossible until it's done." ,
"The only limit to our realization of tomorrow will be our doubts of today.", 
"Success is not final, failure is not fatal: It is the courage to continue that counts.",
"Don't be pushed around by the fears in your mind. Be led by the dreams in your heart.",  
"The only way to achieve the impossible is to believe it is possible.", 
"Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
"In the middle of difficulty lies opportunity.", 
"Your attitude, not your aptitude, will determine your altitude.", 
"Do not wait to strike till the iron is hot, but make it hot by striking.", 
"The only person you are destined to become is the person you decide to be.", 
"Success is stumbling from failure to failure with no loss of enthusiasm.", 
"You are never too old to set another goal or to dream a new dream.", 
"If you want to achieve greatness stop asking for permission.", 
"You miss 100% of the shots you don't take.", 
"Don't be afraid to give up the good to go for the great.", 
]

funny_quotes = [
    "I'm writing a book. I've got the page numbers done.", 
"Why don't scientists trust atoms? Because they make up everything!" ,
"I asked the librarian if the library had any books on paranoia. She whispered, 'They're right behind you.'", 
"I'm not lazy, I'm on energy-saving mode.", 
"I told my wife she should embrace her mistakes. She gave me a hug.", 
"I used to play piano by ear, but now I use my hands.", 
"I'm not arguing, I'm just explaining why I'm right.", 
"Why do they call it rush hour? Nothing moves.", 
"I'm not clumsy. It's just the floor hates me, the tables and chairs are bullies, and the walls get in my way." ,
"My wife told me to stop impersonating a flamingo. I had to put my foot down.", 
"I asked the waiter, 'Is this milk fresh?' He said, 'Lady, three hours ago, it was grass.'", 
"I'm not a vegetarian because I love animals. I'm a vegetarian because I hate plants.", 
"I told my computer I needed a break, and now it won't stop sending me vacation ads.", 
"I used to be a baker because I kneaded dough.", 
"I'm not lazy, I'm in energy-saving mode.", 
"I told my wife she was drawing her eyebrows too high. She looked surprised.",
"I'm not saying I'm Wonder Woman. I'm just saying no one has ever seen me and Wonder Woman in the same room.", 
"I'm not arguing, I'm just explaining why I'm right.", 
"I told my wife she was drawing her eyebrows too high. She looked surprised.",
"I used to be a baker because I kneaded dough.",
"I asked the librarian if the library had any books on paranoia. She whispered, 'They're right behind you.", 
"I'm not lazy, I'm on energy-saving mode.",
"Why don't scientists trust atoms? Because they make up everything!", 
"I told my wife she should embrace her mistakes. She gave me a hug.", 
"I'm not clumsy. It's just the floor hates me, the tables and chairs are bullies, and the walls get in my way.", 
"My wife told me to stop impersonating a flamingo. I had to put my foot down.", 
"I used to play piano by ear, but now I use my hands.", 
"I'm not a vegetarian because I love animals. I'm a vegetarian because I hate plants.", 
"I asked the waiter, 'Is this milk fresh?' He said, 'Lady, three hours ago, it was grass.'", 
"I'm not arguing, I'm just explaining why I'm right.", 
"Why do they call it rush hour? Nothing moves.", 
"I'm not lazy, I'm on energy-saving mode.",
"I told my wife she should embrace her mistakes. She gave me a hug.", 
"I used to play piano by ear, but now I use my hands.", 
"I'm not arguing, I'm just explaining why I'm right.", 
"My wife told me to stop impersonating a flamingo. I had to put my foot down.", 
"I'm not a vegetarian because I love animals. I'm a vegetarian because I hate plants.", 
"I asked the waiter, 'Is this milk fresh?' He said, 'Lady, three hours ago, it was grass.'", 
"I'm not saying I'm Wonder Woman. I'm just saying no one has ever seen me and Wonder Woman in the same room.", 
"I used to be a baker because I kneaded dough.", 
"I'm not lazy, I'm in energy-saving mode.", 
"I told my computer I needed a break, and now it won't stop sending me vacation ads.", 
"I'm not saying I'm Wonder Woman. I'm just saying no one has ever seen me and Wonder Woman in the same room.", 
"I asked the waiter, 'Is this milk fresh?' He said, 'Lady, three hours ago, it was grass.'", 
"I used to play piano by ear, but now I use my hands.", 
"I told my wife she should embrace her mistakes. She gave me a hug.", 
"I'm not arguing, I'm just explaining why I'm right.", 
"Why don't scientists trust atoms? Because they make up everything!", 
"I'm not clumsy. It's just the floor hates me, the tables and chairs are bullies, and the walls get in my way.", 
"I'm not a vegetarian because I love animals. I'm a vegetarian because I hate plants.",
"I'm not saying I'm Wonder Woman. I'm just saying no one has ever seen me and Wonder Woman in the same room.",
"I asked the librarian if the library had any books on paranoia. She whispered, 'They're right behind you.'", 
"I used to play piano by ear, but now I use my hands.", 
"I told my wife she was drawing her eyebrows too high. She looked surprised.", 
"I'm not arguing, I'm just explaining why I'm right.", 
"I'm not lazy, I'm on energy-saving mode.", 
"My wife told me to stop impersonating a flamingo. I had to put my foot down.", 
"I used to be a baker because I kneaded dough.",
"I asked the waiter, 'Is this milk fresh?' He said, 'Lady, three hours ago, it was grass.'", 
"Why do they call it rush hour? Nothing moves.",
]

happy_captions = [
 "Radiate positivity and watch the world brighten up around you.",
 "Embrace the journey, and let positivity be your compass.",
 "Smile often, it's a universal welcome.",
 "Be the reason someone believes in the goodness of people.",
 "Positivity is a superpower; let it shine.",
 "Your vibe attracts your tribe—keep it positive.",
 "See the good in every moment and share it with the world.",
 "Spread positivity like confetti wherever you go.",
  "A positive mind finds opportunity in every challenge.",
 "Choose joy, spread love, radiate positivity.",
 "Life is better when you're laughing. Stay positive.",
 "Surround yourself with those who bring out the best in you.",
 "Your positive action combined with positive thinking results in success.",
 "Positivity is a magnet for miracles.",
 "Let the beauty of what you love be what you do.",
 "Wake up with determination, go to bed with satisfaction.",
 "Every day may not be good, but there's something good in every day.",
 "Shine so bright that you make others feel like they can do the same.",
 "Happiness is not by chance but by choice.",
 "Your positive energy is contagious; let it inspire others.",
 "Surround yourself with those who see greatness in you, even when you don't see it in yourself.",
 "Find joy in the ordinary.",
 "Your attitude determines your direction.",
 "Stay positive, work hard, make it happen.",
 "Kindness is free; sprinkle that stuff everywhere.",
 "The best way to predict the future is to create it.",
 "In a world where you can be anything, be kind.",
  "The only limit is the one you set for yourself.",
 "Chase your dreams with a heart full of positivity.",
 "Positivity is the key to unlock the doors of success.",
 "Surround yourself with those who uplift you.",
 "Your positive thoughts create positive actions.",
 "Start each day with a grateful heart.",
 "You are capable of amazing things.",
 "Success is a journey, not a destination.",
 "Be a voice, not an echo. Spread positivity.",
 "Let your smile change the world, but don't let the world change your smile.",
 "Believe you can, and you're halfway there.",
 "Positivity: because every little thing is gonna be alright.",
 "The more you praise and celebrate your life, the more there is in life to celebrate.",
 "Surround yourself with those who make you happy.",
 "Dream big, work hard, stay focused.",
 "Good vibes only: let go of anything that doesn't make you feel alive.",
 "Your journey is just as important as your destination.",
 "You are never too old to set another goal or to dream a new dream.",
 "Stay positive, work hard, make it happen.",
"Positivity is a choice that becomes a lifestyle.",
 "Embrace the glorious mess that you are.",
 "See the good. Be the good.",
 "Your positive action combined with positive thinking results in success.",
 "Every day may not be good, but there's something good in every day.",
 "Shine so bright that you make others feel like they can do the same.",
 "Surround yourself with those who see greatness in you, even when you don't see it in yourself.",
"Find joy in the ordinary.",
 "Your attitude determines your direction.",
 "Stay positive, work hard, make it happen.",
 "Kindness is free; sprinkle that stuff everywhere.",
 "The best way to predict the future is to create it.",
 "In a world where you can be anything, be kind.",
 "Your positive thoughts create positive actions.",
]

sad_captions = [
"In a world of happiness, their heart whispered the language of sorrow.",
"Silent tears tell a story words can't express.",
"Sometimes, the weight of the world becomes too heavy to bear.",
"Behind their smile, a universe of pain was concealed.",
"When the rain falls, it echoes the tears within.",
"Lost in a crowd, but drowning in solitude.",
"The echoes of laughter couldn't silence the screams within.",
"In the garden of life, their soul wilted like forgotten petals.",
"The colors of their world faded to shades of gray.",
"They collected shattered pieces of their heart, hoping to rebuild.",
"Every goodbye carried the weight of an unfinished story.",
"Gazing into the abyss, finding reflections of their shattered dreams.",
"Happiness lingered like a distant memory, slipping through their fingers.",
"In the silence, the echoes of a broken heart were the loudest.",
"Whispers of the past haunted their every step.",
"They stitched a smile with threads of despair.",
"The shadows of sorrow danced in the moonlight of their soul.",
"Heartbeats synchronized with the rhythm of their silent tears.",
"In the canvas of life, the brush strokes of sadness painted their story.",
"Fading away like a sunset, leaving behind a melancholic horizon.",
"The echoes of laughter couldn't silence the screams within.",
"They became a ghost in their own life story, fading with each chapter.",
"A symphony of tears played in the concert hall of their solitude.",
"Wandering in a desert of emotions, thirsting for a drop of solace.",
"Lost in the labyrinth of their thoughts, seeking an escape.",
"The sunsets mirrored the descent of hope in their world.",
"Caged in their emotions, the key to freedom lost in the abyss.",
"A melody of sadness played in the background of their existence.",
"In the book of life, their chapters were written in ink of sorrow.",
"The stars witnessed their silent cries in the lonely nights.",
"Raindrops mirrored the tears they couldn't shed.",
"Beneath the smile, a river of sadness flowed silently.",
"In the garden of emotions, weeds of sorrow overtook the blooms.",
"Echoes of laughter couldn't drown the silence of their soul.",
"They wore a mask of strength, hiding the vulnerability within.",
"The moon witnessed their tears, reflecting the pain in its glow.",
"Drowning in the ocean of their thoughts, gasping for breath.",
"The canvas of their heart painted with strokes of melancholy.",
"In the symphony of life, their notes were played in a minor key.",
"Clouds of sadness overshadowed the sunshine in their soul.",
"Whispers of heartbreak echoed in the corridors of their mind.",
"They navigated through the storm, hoping for a glimpse of sunlight.",
"Silent tears wrote poems on the parchment of their cheeks.",
"In the tapestry of life, threads of sadness woven with care.",
"The mirror reflected a smile, but the eyes told a different tale.",
"They danced with shadows, partners in the ballroom of solitude.",
"A symphony of tears played in the concert hall of their solitude.",
"The echoes of laughter couldn't silence the screams within.",
"They became a ghost in their own life story, fading with each chapter.",
"A melody of sadness played in the background of their existence.",
"In the book of life, their chapters were written in ink of sorrow.",
"The stars witnessed their silent cries in the lonely nights.",
"Raindrops mirrored the tears they couldn't shed.",
"Beneath the smile, a river of sadness flowed silently.",
"In the garden of emotions, weeds of sorrow overtook the blooms.",
"Echoes of laughter couldn't drown the silence of their soul.",
"They wore a mask of strength, hiding the vulnerability within.",
"The moon witnessed their tears, reflecting the pain in its glow.",
"Drowning in the ocean of their thoughts, gasping for breath.",
]

# Function to display a random quote from the given list
def display_quote(quote_list):
    quote = random.choice(quote_list)
    quote_label.config(text=quote)


# Label to display quotes
quote_label = tk.Label(root, text="", wraplength=400, justify="center")
quote_label.pack()

#Back Button
back_button = tk.Button(root, text="Back", command=show_quote_categories)

root.mainloop()