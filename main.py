from tkinter import *

FONT = ("Repa Gobi", 14, "bold")
DOLLAR_TO_CZK = 21.26
EURO_TO_CZK = 26.15


def radio_used():
    """
    function that checking which radiobutton was selected (which currency is active)
    according to selected currency, function calculate with actual exchange change rates
    """
    if entry.get():
        # CZK selected
        if radio_state.get() == 1:
            dollars_return = round(int(entry.get()) / DOLLAR_TO_CZK, 2)
            euros_return = round(int(entry.get()) / EURO_TO_CZK, 2)
            result_czk_label.config(text="")
            result_dollars_label.config(text=f"{dollars_return} $")
            result_euros_label.config(text=f"{euros_return} €")
        # Dollar selected
        elif radio_state.get() == 2:
            czk_return = round(int(entry.get()) * DOLLAR_TO_CZK, 2)
            euros_return = round(int(entry.get()) * DOLLAR_TO_CZK / EURO_TO_CZK, 2)
            result_czk_label.config(text=f"{czk_return} CZK")
            result_dollars_label.config(text="")
            result_euros_label.config(text=f"{euros_return} €")
        # Euros selected
        elif radio_state.get() == 3:
            czk_return = round(int(entry.get()) * EURO_TO_CZK, 2)
            dollars_return = round(int(entry.get()) * EURO_TO_CZK / DOLLAR_TO_CZK, 2)
            result_czk_label.config(text=f"{czk_return} CZK")
            result_dollars_label.config(text=f"{dollars_return} $")
            result_euros_label.config(text="")


app = Tk()
app.title("Currency converter")
app.minsize(width=400, height=300)
app.config(padx=50, pady=50)

entry = Entry(font=FONT, width=15, justify=CENTER)
entry.grid(column=0, row=0)

result_czk_label = Label(text="czk", font=FONT)
result_dollars_label = Label(text="$", font=FONT)
result_euros_label = Label(text="€", font=FONT)
result_czk_label.grid(column=0, row=3)
result_dollars_label.grid(column=0, row=4)
result_euros_label.grid(column=0, row=5)

radio_state = IntVar()
czk = Radiobutton(text="CZK", value=1, variable=radio_state, command=radio_used, font=FONT)
dollars = Radiobutton(text="$ Dollars", value=2, variable=radio_state, command=radio_used, font=FONT)
euros = Radiobutton(text="€ Euro", value=3, variable=radio_state, command=radio_used, font=FONT)
czk.grid(column=1, row=0)
dollars.grid(column=1, row=1)
euros.grid(column=1, row=2)

app.mainloop()
