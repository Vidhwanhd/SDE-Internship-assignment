Major Issues Identified
Missing users Table: The app was throwing an error due to the absence of the users table in the SQLite database.

Password Hashing Issue: passlib couldn't find the bcrypt backend, causing password hashing failures.

404 Errors for POST, PUT, DELETE: These routes were not working due to route misconfigurations or method mismatches.

Authentication Issues: The login logic was not correctly verifying passwords against the hashed values stored in the database.

Changes Made
Database Initialization: Created an init_db.py script to initialize the database and create the users table.

Password Hashing Fix: Installed bcrypt and configured passlib to use it as the backend.

Corrected Routes: Ensured routes for POST, PUT, and DELETE methods were properly defined and mapped.

Login Logic Update: Implemented correct password verification using check_password from passlib.

Assumptions and Trade-offs
Basic Data Validation: Assumed simple validation for user data; could be expanded with more checks like unique email.

Password Security: Used bcrypt for password hashing. While secure, it might be less performant for large-scale systems. Could consider Argon2 for future improvements.

SQLite for Simplicity: SQLite was used for simplicity, but a more scalable database like PostgreSQL is preferred for production.

What I Would Do with More Time
Improve Security: Implement Argon2 for password hashing, and consider adding OAuth for external logins.

Write Tests: Add unit and integration tests for routes and services.

Error Handling: Improve error handling across the app.

Role Management: Implement user roles (admin, user) for better access control.

Database Optimization: Migrate to PostgreSQL and add indexing for performance.



AI Usage
Tools Used:
ChatGPT (by OpenAI)

GitHub Copilot

What AI Was Used For:
Code Suggestions & Refactoring:

Assisted in refactoring and optimizing code, such as reorganizing service functions and creating helper functions.

Helped clean up route definitions and ensured proper HTTP method handling.

Troubleshooting:

Used ChatGPT to troubleshoot issues related to password hashing and database initialization.

Helped debug errors like MissingBackendError and 404 Not Found by providing solutions for missing dependencies and incorrect route setup.

Documentation:

Assisted in writing the CHANGES.md file, summarizing major issues, changes, and future considerations.

AI-Generated Code Modified or Rejected:
Code Rejected:

Some of the initial suggestions for route setup and error handling were modified to better align with Flask best practices and project structure.

Code Modified:

AI-suggested code for hashing passwords was modified to ensure it worked with passlib's bcrypt backend.