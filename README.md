# wardrobe-management
This code is a Python script that creates a graphical user interface (GUI) application for managing a wardrobe database. It utilizes several libraries:

mysql.connector: For connecting to a MySQL database to perform operations like fetching, inserting, and deleting records.
tkinter and tkinter.ttk: For building the GUI components such as windows, buttons, labels, and treeviews.
PIL (Python Imaging Library), specifically Image and ImageTk: To handle and display images within the GUI.
Key Features and Workflow:
Database Connection: Establishes a connection to a MySQL database named 'wardrobe' using credentials provided (host, user, password, and port). It assumes a table structure compatible with the operations defined in the script (e.g., fields for code, type, brand, and colour).

Main Window Setup: Creates the main application window with the title 'YOUR WARDROBE', setting its size to full screen based on the user's screen dimensions. It also sets up the background and other essential UI elements like buttons for different operations (view all records, search, delete, and add new records).
![Screenshot 2024-04-04 010859](https://github.com/youssefaim/wardrobe-management/assets/147152506/1092c163-d67d-4ac0-be66-2eff88dfe496)

Image Handling: Uses images for background and button icons, demonstrating how to resize and display images using PIL. It requires these image files to be present in the specified paths.

CRUD Operations:

View All Records: Displays all records from the wardrobe database in a new window using a treeview. Includes a back button to return to the main window.
![Screenshot 2024-04-04 011040](https://github.com/youssefaim/wardrobe-management/assets/147152506/24c90519-34be-46b1-ac04-0cad9302461e)

Search: Allows searching the database by code, type, brand, or colour. The search results are displayed in a treeview.
![Screenshot 2024-04-04 011231](https://github.com/youssefaim/wardrobe-management/assets/147152506/8945aa71-d3b9-427e-84b6-f26f0a62275f)

Delete Record: Provides a functionality to delete a record based on the item's code. Shows a success message upon successful deletion.
![Screenshot 2024-04-04 011316](https://github.com/youssefaim/wardrobe-management/assets/147152506/10ce363c-d391-4afe-b0a4-ce7cd7103618)

Add New Record: Opens a form to input details for a new wardrobe item (code, type, brand, colour) and adds the record to the database. Shows a success message upon successful addition.![Screenshot 2024-04-04 011412](https://github.com/youssefaim/wardrobe-management/assets/147152506/936cda1a-aa8c-48d4-bec2-25a8d18f6d8e)


User Interaction: Through the main window, users can navigate to different functionalities. Each operation opens in a new window (using Toplevel) to keep the main window accessible.

GUI Customization: Demonstrates basic customization of GUI elements using fonts, colors, and padding for better layout and user experience.

This script is a comprehensive example of using tkinter for building a database management GUI, showcasing CRUD operations, image handling, and the use of MySQL for persistent storage.

