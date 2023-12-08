Group 7 
- Olatunbosun Balogun
- Kabir Lawal


CODES FUNCTIONS 

1. Nhousingproj.ipynb:In this file we created:- 
- A data base with Sqlite3 "Nig_Housing.db" 
- Created a table called "housing" to insert our data into
- Inserted our data file "Nig_Housing_Data.csv" into the table "housing"
- Quarry the table to confirm our data set was inserted in the right order
- "Commited and Closed the cursor" to save our data and table on the data base  

2. build_db_fillin.py :
- The code uses `pathlib` to find the current working directory.
- It defines a function, `create_db`, to make and populate a SQLite database from a CSV file.
- The function takes parameters for the database name, CSV filename, and table name.
- The CSV file path is created with `pathlib.Path.cwd()` and the provided filename.
- It establishes a connection to SQLite and creates a cursor.
- Data from the CSV is loaded into a Pandas DataFrame named `housing`.
- The DataFrame is written to the SQLite table using `to_sql()`.
- An SQL query fetches all records from the specified table, and the results are printed.
- Changes are committed, and the connection is closed.
- The main script sets parameters db_name = "Nig_Housing.db", filename = "Nig_Housing_Data.csv", table_name = "housing" 
and calls the `create_db` function.  

3. app.py:
- The code creates a Flask web application for displaying Nigerian housing data.
- It uses Flask's `render_template` to render HTML templates.
- The SQLite database path and name are defined using `pathlib`.
- Three routes are defined: "/" for the home page, "/about" for an about page, and "/data" to display housing data in a table.
- The `/data` route connects to the SQLite database, retrieves housing data, and renders an HTML template with the data displayed in a table.
- When executed as the main script, the Flask app runs in debug mode.  

4.about.html:
- The HTML code represents the "About" page for the 7th Floor Housing web application.
- It provides a clean and centered design with specific styling for body, heading, and paragraphs.
- The content introduces "7th Floor Housing" and emphasizes its role as a premier destination for Nigerian housing data.
- Variable descriptions are presented in an ordered list, including details such as state, town, house type, bathrooms, bedrooms, toilets, and price.
- A reference link is included, pointing to the "Nigeria Houses Price Dataset" on data.world.
- The page encourages exploration of the Nigerian real estate world with 7th Floor and emphasizes the platform as a trusted partner in housing data.

5.data_table_fillin.html:
- This HTML code defines a webpage presenting housing data in a tabular format.
- The page title is set to "My Website," and the overall styling centers the content.
- A table is styled with a margin, border-collapse, and width properties to improve readability.
- Table headers (th) and data cells (td) are given a border and padding for a structured appearance.
- The content includes an h1 heading "Housing Data" to provide context.
- A table is created with headers for State, Town, House Type, Bedrooms, Bathrooms, Toilets, and Price.
- The table body uses a template loop to dynamically populate data from the "housing" variable.
- For each row in the dataset, values are inserted into the corresponding table cells.
- The structure ensures a clean presentation of the housing data, making it easy to read and navigate on the webpage.

6.Index_fillin.html:
- The HTML code defines a webpage with styling to create a visually appealing and centered layout.
- The title of the webpage is set to "My Website."
- The overall styling centers the content and adjusts the appearance of certain elements.
- An h2 heading, "Welcome To Nigeria's Largest Housing Website," is styled with a specific font size and margin for emphasis.
- The styling for an unordered list (ul) includes removing default list styling, setting padding to zero, and using flex display for centering list items.
- Each list item (li) is given a margin for spacing.
- Hyperlinks (a) within list items are styled to remove underlines for a cleaner look.
- The unordered list contains two list items, each linking to a different page using Flask's `url_for` function: "About page" linked to the 'about' route and "Data page" linked to the 'data' route.
- The structure creates an organized and visually appealing welcome page with easy navigation links to other sections of the website.
