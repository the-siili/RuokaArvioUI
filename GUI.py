import tkinter as tk
import time, requests, json




def pressed(txt, rating):
    
    try:
        url = 'https://ksyk-food-rating-average.onrender.com/receive_post'  # Update with the correct URL

        data_to_send = rating

        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, data=json.dumps(data_to_send), headers=headers)
        txt.config(text=response.text)
        time.sleep(1)
        txt.config(text='Kiitos Vastauksesta!')
    except:
        txt.config(text='Lähettämisessä oli ongelma!')

    time.sleep(2)

    txt.config(text="Miten arvioisit tämän päivän ruoan?")






root = tk.Tk()
root.geometry("800x480")

text = tk.Label(text="Miten arvioisit tämän päivän ruoan?",font=("Arial", 35))
desc = tk.Label(text="Vastaathan vain kerran päivässä. \nArviot eivät mitenkään vaikuta koulun tuleviin ruokavalintoihin.",font=("Arial", 15), fg="grey")





text.place(x=30, y=140)
desc.place(x=120, y=220)

root.mainloop()