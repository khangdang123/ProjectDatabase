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

## Non-functional Requirements
1. Compatible on different web browsers.
2. Hashed Passwords for more secure security.

## Use Cases <Add name of who will write (this specific requirement) and implement (in subsequent milestones) the use case below>

#1 Use Case (Andy Neidhart) [Sketch](https://github.com/khangdang123/ProjectDatabaseNoteApp/blob/main/images/Ui1.png)
   - **Use Case Name:** Create Notes
   - **Pre-condition:** User is logged into the note-taking application.
   - **Trigger:** User selects the "Create Notes" option in the application menu.
   - **Primary Sequence:**
      1. User clicks on the "Create Notes" option.
      2. Application opens a new blank note editor.
      3. User enters the content for the note.
      4. User can format the content (optional).
      5. User clicks on the "Save" button.
      6. Application saves the note with a unique identifier.
      7. Application displays a confirmation message indicating the note has been created successfully.
   - **Primary Postconditions:** Note is successfully created and saved in the user's account.
   - **Alternate Sequence:**
     -   Step 3a: User attaches files or images to the note.
     -   Step 5a: If the user chooses not to save, the application prompts for confirmation before closing the note editor.

#2 Use Case (Andy Neidhart) [Sketch](https://github.com/khangdang123/ProjectDatabaseNoteApp/blob/main/images/Ui2.png)
   - **Use Case Name:** Edit Content of Notes
   - **Pre-condition:** User is logged into the note-taking application and has an existing note.
   - **Trigger:** User selects the desired note and clicks on the "Edit" option.
   - **Primary Sequence:**
      1. User selects the note to edit.
      2. User clicks on the "Edit" option.
      3. Application opens the note in edit mode, displaying existing content.
      4. User modifies the content of the note.
      5. User can format the content (optional).
      6. User clicks on the "Save" button.
      7. Application saves the edited note.
      8. Application displays a confirmation message indicating the note has been updated successfully.
   - **Primary Postconditions:** Note is successfully edited and saved with the changes made by the user.
   - **Alternate Sequence:**
      -   Step 4a: User deletes existing content and adds new content.
      -   Step 6a: If the user chooses not to save, the application prompts for confirmation before closing the note editor.

#3 Use Case (Andy Neidhart) [Sketch](https://github.com/khangdang123/ProjectDatabaseNoteApp/blob/main/images/Ui3.png)
   - **Use Case Name:** Delete Notes
   - **Pre-condition:** User is logged into the note-taking application and has one or more existing notes.
   - **Trigger:** User selects the desired note and clicks on the "Delete" option.
   - **Primary Sequence:**
      1. User selects the note to delete.
      2. User clicks on the "Delete" option.
      3. Application displays a confirmation dialog asking the user to confirm the deletion.
      4. User confirms the deletion.
      5. Application removes the note from the user's account.
      6. Application displays a confirmation message indicating the note has been deleted successfully.
   - **Primary Postconditions:** Selected note is permanently deleted from the user's account.
   - **Alternate Sequence:**
     -   Step 3a: User cancels the deletion, and the application returns to the note view without deleting the note.

#4 Use Case (Andy Neidhart) [Sketch](https://github.com/khangdang123/ProjectDatabaseNoteApp/blob/main/images/Ui4.png)
   - **Use Case Name:** Share Notes
   - **Pre-condition:** User is logged into the note-taking application and has an existing note.
   - **Trigger:** User selects the desired note and clicks on the "Share" option.
   - **Primary Sequence:**
      1. User selects the note to share.
      2. User clicks on the "Share" option.
      3. Application generates a shareable link or unique identifier for the selected note.
      4. User copies the shareable link or identifier.
      5. User can share the link via email, messaging apps, or social media platforms.
      6. Recipient clicks on the shared link.
      7. Application displays the shared note to the recipient.a
   - **Primary Postconditions:** User successfully shares the selected note with others, and recipients can view the note using the shared link.
   - **Alternate Sequence:**
     -   Step 3a: User sets specific permissions for the shared note (e.g., read-only access, editing access).
     -   Step 5a: User shares the note directly with specific users within the application by entering their email addresses.

#5 Use Case (Jonathan) [Sketch](https://github.com/khangdang123/ProjectDatabaseNoteApp/blob/main/images/ui5.JPG)
   - **Use Case Name:** Save as Draft
   - **Summary:** The user should be able to save a draft a note for further editing without publishing/sharing said notes woth a title for reference 
   - **Pre-Conditions:** The user should have a saved note, created an account and be in the create note or edit note section.
   - **Trigger:** User presses a button near the top corner that is marked as "Save as Draft".
   - **Primary Sequence:**
     1. User clicks create notes.
     2. Application opens a blank note editor.
     3. User can format the content (optional).
     4. User clicks on the "Save as draft button" button.
     5. Application asks for a name for the draft
     6. User inputs a name in the application and clicks "ok"
     7. Application saves the note with a unique identifier.
     8. Application displays a confirmation message indicating the note has been saved correctly.
   - **Primary Postcondition:** Note is saved under a seperate section of the account titled as "Drafts", this section is by default only viewable by the user.
   - **Alternate Sequence:**
     -   Step 3a: User attaches files or images to the note (optional).
     -   Step 4a: If the user chooses not to save, the application prompts for confirmation before closing the note editor.

#6 Use Case (Jonathan) [Sketch](https://github.com/khangdang123/ProjectDatabaseNoteApp/blob/main/images/ui6.JPG)
   - **Use Case Name:** Add Comments
   - **Summary:** User should be able to add comments on their own notes for reference that show up on the side of their document
   - **Pre-Conditions:** The user should have a saved note, created an account and be in the edit note section.
   - **Trigger:** User is viewing the saved note and clicks the comment section
   - **Primary Sequence:**
     1. User opens a previously saved note.
     2. Application opens the old note.
     3. User presses the comment button on the toolbar
     4. User is able to highlight a section of the note to comment on
     5. Application asks for user input on what to comment on the note
     6. User puts in a text comment and presses ok
     7. Aplication saves the comment on the side of the note with a highlight of the commented section
   - **Primary Postcondition:** Comment is saved on document with a highlight over the commented section.
   -  **Alternate Sequence:**
     -   Step 6a: User presses the x button and the note is deleted.

#7 Use Case (Jonathan) [Sketch](https://github.com/khangdang123/ProjectDatabaseNoteApp/blob/main/images/ui7.JPG)
   - **Use Case Name:** Add Attachments
   - **Summary:** The user should have a saved note, created an account and be in the view/edit note section/
   - **Pre-Conditions:** The user should have a saved note before this action can be completed. 
   - **Trigger:** User is viewing the saved note and clicks the add attachment button
   - **Primary Sequence:**
     1. User opens a previously saved note.
     2. Application opens the saved note.
     3. User presses the add attachment button on the toolbar.
     4. Application pops up a prompt for what attachment to add.
     5. User chooses an attachment from their machine to add to the note.
     6. Application asks for confirmation if this attachment is to be attached.
     8. User clicks ok.
     9. Aplication saves the attachment to the note.
   - **Primary Postcondition:** Attachment is saved on document on the very bottom of the note and can be downloaded by other users if shared.
   - **Alternate Sequence:**
     -   Step 6a: User presses the x button and the attachment is not added to the note.
 
#8 Use Case (Jonathan) [Sketch](https://github.com/khangdang123/ProjectDatabaseNoteApp/blob/main/images/ui8.JPG)
   - **Use Case Name:** Advanced Search
   - **Summary:** User should be able to search their saved/ drafted notes by the title inputted to the note.
   - **Pre-Conditions:** The user should have a saved note, created an account and not in the create, edit or open note section
   - **Trigger:** User is viewing the saved note and clicks the add 'Search' button.
   - **Primary Sequence:**
     1. User is in their profile.
     2. User clicks the search toolbar on the top right corner.
     3. Application expands search text input section.
     4. User searches by the title they want to look for.
     5. User clicks the enter key to send the search in.
     6. Application searches for all notes with or with part of the name typed in.
     7. Application showcases a seperate section for regular saved notes and draft notes within the parameters.
     8. User is able to click the relevant note they were searching for to open the note.
   - **Primary Postcondition:** Relevant files for the search term is presented to the user and able to be access from the advanced search method.
   - **Alternate Sequence:**
     -   Step 5a. The user clicks the X button to delete the previously inputted text.
     -   Step 8a. User does not find the search terms they are looking for and click the X button to go back to profile.

#9 Use Case (Khang Dang) [Sketch](https://github.com/khangdang123/ProjectDatabaseNoteApp/blob/main/images/ui9.png)
- **Use Case Name:** Rename Notes
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
  -   If the user types a new title that exceeds the permitted characters, the system will display a message indicating “Exceeds characters”.
  -   If the user enters a new title that duplicates the existing title of their notes, the system will display a message stating "Cannot use the same title" and prompt the user         to try again.
 
#10 Use Case (Khang Dang) [Sketch](https://github.com/khangdang123/ProjectDatabaseNoteApp/blob/main/images/ui10.png)
- **Use Case Name:** Make an Acoount
- **Summary:** The user should be able to create an account.
- **Pre-condition:** User has accessed the note-taking application.
- **Trigger:** The user clicks on the “Create Account” option.
- **Primary Sequence:**
   1. The user accessed the note-taking application.
   2. The user selects a “Create Account” button in an interface of the note-taking application.
   3. The system displays a message prompting a form of requesting some basic information of the user, including Name,Email Address, Username, and Password. 
   4. The user has filled all the required fields, the user clicks the “Register” button to submit his information.
   5. The system checks the validity of all required fields of the form.
   6. If all required fields are valid, the system proceeds to create an account.
   7. The system sends the notification to the user that the account has been successfully created.
- **Primary Postconditions:** A new user account has been successfully created, granting access to all features of the note-taking application for login and use.
- **Alternate Sequence:**
  -   If one of the required fields has not been filled in the form, the system will prompt the message “Invalid” and request the user try again.
  -   If the system detects that the Email Address duplicates with the existing account, the system will prompt the message “The Email Address has been used” and request the user       try again. 

#11 Use Case (Khang Dang) [Sketch](https://github.com/khangdang123/ProjectDatabaseNoteApp/blob/main/images/ui11.png)
- **Use Case Name:** Connect with any external API
- **Summary:** The user should be able to connect their note-taking application to any external APIs.
- **Pre-condition:** User has successfully logged in and accessed the note-taking application. 
- **Trigger:** The user clicks on the “Connect External API” option.
- **Primary Sequence:**
   1. The user successfully logged in to their account and opened their note.
   2. The user clicks on the “Connect External API” button.
   3. The system displays a message prompting the user to input a URL from which they want to retrieve information.
   4. The system sends a request to a specific external API endpoint that the user provided.
   5. The specific external API endpoint receives the request.
   6. The specific external API endpoint responds back to the system, including the data that the user expected to receive from the endpoint.
   7. The system displays the retrieved information that the user provided URL in a specific external API.
- **Primary Postconditions:** The system is capable of connecting multiple external API endpoints within the note.
- **Alternate Sequence:**
   - If the user enters a URL that the external API endpoints cannot retrieve resources from, the system will generate an error message for the user.

#12 Use Case (Jordan Nguyen) [Sketch](https://github.com/khangdang123/ProjectDatabaseNoteApp/blob/main/images/ui12.jpg)
- **Use Case Name:** Sorting Notes
- **Pre-condition:** The user has logged in
- **Trigger:** User selects the "filter" option
- **Primary Sequence:**
   1. The system prompts a menu for the user to select if they want to sort alphabetically or by the date that it was created.
   2. The user selects which one of the sorting options based on what they want.
   3. The system reorganizes the list of notes according to which option the user selected and shows the updated list to the user.
   4. The user can now view and pick their notes in the newly sorted order.
- **Primary Postconditions:** <The user's notes are sorted the way they want it and they can now view the notes in the newly sorted list>
- **Alternate Sequence:** 
   1. The user selected a sorting option that cannot be done.
      - The system displays an error message to the user
      - The system prompts the user to create a note before using the sorting options.
   
#13 Use Case (Jordan Nguyen) [Sketch](https://github.com/khangdang123/ProjectDatabaseNoteApp/blob/main/images/ui13.jpg)
- **Use Case Name:** Login to Account
- **Pre-condition:** The user has opened up the note-taker on their web browser
- **Trigger:** User selects the "Login" option
- **Primary Sequence:**
   1. The website prompts the user to enter their username and password.
   2. The user enters in their username and password
   3. The user presses the login button which sends the request to the server.
   4. The server checks the credentials with the user's stored data to see if they match.
   5. Upon successful authentication, the website brings the user to the dashboard or their list of notes.
- **Primary Postconditions:** <The user is logged in to their account, and they have access to their list of notes, settings, and any other features within the website.>
- **Alternate Sequence:** 
   1. The user enters incorrect credentials
      - The system displays an error message to the user
      - The system prompts the user to enter their credentials again or press forgot password if they don't remember.
   
#14 Use Case (Jordan Nguyen) [Sketch](https://github.com/khangdang123/ProjectDatabaseNoteApp/blob/main/images/ui14.jpg)
- **Use Case Name:** Log out of account
- **Pre-condition:** The user has logged in to their account on the note-taking service on their browser
- **Trigger:** User selects the "Log out" option
- **Primary Sequence:**
   1. The system prompts the user with a menu to confirm that they want to log out.
   2. The user selects the log out button to confirm that they want to log out.
   3. The website logs the user out and revokes their access to the account and its features.
   4. The app returns to the welcome screen, where the user can either log in with a different account or exit the website.
- **Primary Postconditions:** <The user is successfully logged out of their account, and the website no longer grants them access to their notes or account features.>
- **Alternate Sequence:** 
   1. The internet connection is not stable
      - The system displays an error message to the user
      - The system prompts that their internet connection is unstable and they need to retry logging out.
