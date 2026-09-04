# We import the libraries
import pandas as pd
import requests
import tkinter as tk
from tkinter import ttk
from io import StringIO

# URL of the webpage
url = "https://en.wikipedia.org/wiki/Dark_(TV_series)"
# User-Agent header to identify our request
headers = {
    "User-Agent": "Mozilla/5.0"
}
#Request and response
response = requests.get(
    url,
    headers=headers,
    timeout=10
)
# Check if the request was successful
response.raise_for_status()
print("Connection successful!")
# Extract HTML tables from the webpage
dark = pd.read_html(StringIO(response.text))
# Select the table containing character information
characters = dark[1]
print(f"Characters found: {len(characters)}")
#Select comlumns of interest
characters = characters[
    [
        "Character",
        "Life stage",
        "Description",
        "Actor"
    ]
]
# Remove unnecessary spaces and line breaks
characters = characters.map(lambda value: " ".join(str(value).split()))
# Replace missing values
characters = characters.replace("nan","N/A")
# Make long descriptions easier to read
characters["Description"] = characters["Description"].apply(
    lambda description:
        description[:100] + "..."
        if len(description) > 100
        else description
)
#GUI Window
def show_table(dataframe):

    # Create main window
    window = tk.Tk()

    window.title("DARK - Character Information")
    window.geometry("1200x600")
    window.minsize(800, 400)


    # ========================================================
    # TITLE
    # ========================================================

    title = tk.Label(
        window,
        text="DARK - Character Information",
        font=("Arial", 20, "bold")
    )

    title.pack(pady=(15, 5))


    subtitle = tk.Label(
        window,
        text=f"{len(dataframe)} characters extracted from Wikipedia",
        font=("Arial", 10)
    )

    subtitle.pack(pady=(0, 15))


    # ========================================================
    # TABLE FRAME
    # ========================================================

    table_frame = tk.Frame(window)

    table_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )


    # ========================================================
    # CREATE INTERNAL COLUMN IDs
    # ========================================================

    # Create simple IDs for Treeview
    column_ids = [f"col{i}" for i in range(len(dataframe.columns))]


    # ========================================================
    # CREATE TREEVIEW
    # ========================================================

    table = ttk.Treeview(
        table_frame,
        columns=column_ids,
        show="headings"
    )


    # ========================================================
    # CONFIGURE COLUMNS
    # ========================================================

    for column_id, column_name in zip(
        column_ids,
        dataframe.columns
    ):

        table.heading(
            column_id,
            text=column_name
        )

        table.column(
            column_id,
            width=180,
            anchor="w"
        )


    # ========================================================
    # CUSTOM COLUMN WIDTHS
    # ========================================================

    table.column(
        "col0",
        width=180
    )

    table.column(
        "col1",
        width=150
    )

    table.column(
        "col2",
        width=600
    )

    table.column(
        "col3",
        width=200
    )


    # ========================================================
    # INSERT DATA
    # ========================================================

    for _, row in dataframe.iterrows():

        table.insert(
            "",
            "end",
            values=list(row)
        )


    # ========================================================
    # SCROLLBARS
    # ========================================================

    vertical_scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=table.yview
    )

    horizontal_scrollbar = ttk.Scrollbar(
        table_frame,
        orient="horizontal",
        command=table.xview
    )

    table.configure(
        yscrollcommand=vertical_scrollbar.set,
        xscrollcommand=horizontal_scrollbar.set
    )


    # ========================================================
    # GRID LAYOUT
    # ========================================================

    table.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

    vertical_scrollbar.grid(
        row=0,
        column=1,
        sticky="ns"
    )

    horizontal_scrollbar.grid(
        row=1,
        column=0,
        sticky="ew"
    )


    table_frame.grid_rowconfigure(
        0,
        weight=1
    )

    table_frame.grid_columnconfigure(
        0,
        weight=1
    )


    # ========================================================
    # CLOSE BUTTON
    # ========================================================

    close_button = ttk.Button(
        window,
        text="Close",
        command=window.destroy
    )

    close_button.pack(
        pady=15
    )


    # ========================================================
    # START GUI
    # ========================================================

    window.mainloop()
# DISPLAY THE RESULTS

show_table(characters)
print("\nExtraction completed successfully!")