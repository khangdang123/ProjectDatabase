## <remove all of the example text and notes in < > such as this one>

## Functional Requirements
1. Create Notes <The user should be able to create a new empty note>
2. Edit Content of notes <The user should be able to edit the content of the notes that they created>
3. Delete Notes <The user should be able to delete any notes that they created>
4. Share Notes <The user should be able to share their notes by creating a link or a download file>
5. Save as draft <The user should be able to save an in-progress note as a draft before it is shared publicly or privately>
6. Add comments <The user should be able to add comments on their notes>
7. Add attachments <The user should be able to add certain types of attachments to their notes>
8. Advanced Search <The user should be able to search for titles of notes and or keywords in their notes>
9. Rename Notes <The user should be able to rename the title of their notes after setting it>
10. Make an account <The user should be able to create an account>
11. Connect with any external API <Note taking app should be able to connect to any external API>
12. Sorting Notes <The user should be able to sort their notes by the date they were created or alphabetically>
13. Login to account <The user should be able to login to their account>
14. Log out of account <The user should be able to log out of their account>

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
1. Compatible on different web browsers.
2. Hashed Passwords for more secure security.

<each of the 14 requirements will have a use case associated with it>
## Use Cases <Add name of who will write (this specific requirement) and implement (in subsequent milestones) the use case below>
1. Use Case Name (Should match functional requirement name)
- **Pre-condition:** <can be a list or short description>
- **Trigger:** <can be a list or short description>
- **Primary Sequence:**
1. Ut enim ad minim veniam, quis nostrum e
2. Et sequi incidunt
3. Quis aute iure reprehenderit
4. ...
5. ...
6. ...
7. ...
8. ...
9. ...
10. <Try to stick to a max of 12 steps>
- **Primary Postconditions:** <can be a list or short description>
- **Alternate Sequence:** <you can have more than one alternate sequence to
describe multiple issues that may arise and their outcomes>
1. Ut enim ad minim veniam, quis nostrum e
2. Ut enim ad minim veniam, quis nostrum e
3. ...
- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>

1. Ut enim ad minim veniam, quis nostrum e
2. Ut enim ad minim veniam, quis nostrum e
3. ...
   
#9 Use Case (Khang Dang)
1. Use Case Name: Rename Notes
- **Summary:** The user should be able to rename the title of their notes after setting it
- **Pre-condition:** The user has logged in to their account on the note-taking application and has named the title to their notes.
- **Trigger:** The user clicks on the “Rename” option.
- **Primary Sequence:**
   1. The user successfully logged into their account of note-taking application.
   2. The user clicks on the note that the user expects to rename it.
   3. The user clicks on the button “Rename” in the note and the system prompts them the display window.
   4. The display window prompts the text input, allowing the user to input the expected name for renaming.
   5. The user clicks the “Save” button in the display window after renaming for saving.
   6. The note-taking application displays a confirmation message for confirming the user has successfully updated the title.
- **Primary Postconditions:** The system will reflect the new name provided by the user after displaying a confirmation message successfully.
- **Alternate Sequence:**
   1. If the user types a new title that exceeds the permitted characters, the system will display a message indicating “Exceeds characters”.
   2. If the user enters a new title that duplicates the existing title of their notes, the system will display a message stating "Cannot use the same title" and prompt the user         to try again.

  
#12 Use Case <Jordan Nguyen>
1. Use Case Name: Sorting Notes
- **Pre-condition:** <The user has logged in>
- **Trigger:** <User selects the "filter" option>
- **Primary Sequence:**
1. The system prompts a menu for the user to select if they want to sort alphabetically or by the date that it was created.
2. The user selects which one of the sorting options based on what they want.
3. The system reorganizes the list of notes according to which option the user selected and shows the updated list to the user.
4. The user can now view and pick their notes in the newly sorted order.
- **Primary Postconditions:** <The user's notes are sorted the way they want it and they can now view the notes in the newly sorted list>
- **Alternate Sequence:** 
1. The user selected a sorting option that cannot be done.
   -The system displays an error message to the user
   -The system prompts the user to create a note before using the sorting options.


