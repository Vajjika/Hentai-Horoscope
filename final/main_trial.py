import cfscrape
import webbrowser
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

#dateOfBirth = input("Enter your date of birth(DD/MM/YY): ")
dateOfBirth = 0



def submit():
    global dateOfBirth
    dateOfBirth = entry.get()
    window.destroy()

window = tk.Tk()
window.title("Hentai Horoscope")
window.geometry("300x200")

style = ThemedStyle(window)
style.set_theme("adapta")  # Set the theme to "arc" for a modern look

label = ttk.Label(window, text="Enter your date of birth (DDMMYY):")
label.pack(pady=10)

entry = ttk.Entry(window)
entry.pack(pady=10)
entry.bind("<Return>", submit)  # Bind the Enter key to the submit() function



button = ttk.Button(window, text="Submit", command=submit)
button.pack(pady=10)

window.mainloop()

print("Date of Birth:", dateOfBirth)


url = f"https://nhentai.net/g/{dateOfBirth}/1/"

# Create a Cloudflare scraper
scraper = cfscrape.create_scraper()

# Make a request using the scraper
response = scraper.get(url)

# Print the response content
print(response.content)

webbrowser.open(url)