Major Issues Identified
Missing users Table: The application failed to start properly due to the absence of the users table in the SQLite database.

Password Hashing Error: The app initially attempted to use bcrypt, but due to missing backend support, password hashing failed.

404 Errors for POST, PUT, DELETE: These endpoints returned 404 due to incorrect route configurations or HTTP method issues.

Authentication Bug: Passwords were not being verified correctly against stored hashes, causing login failures.

 Changes Implemented
Database Initialization: Created an init_db.py script to initialize the database and create the users table automatically.

Password Hashing Updated: Switched to a supported hashing algorithm like sha256_crypt (or another from passlib) that doesn’t require external dependencies.

Route Configuration Fixed: Properly defined all POST, PUT, and DELETE routes to align with Flask's method routing.

Login Logic Corrected: Updated the authentication flow to correctly compare plaintext passwords with hashed values using the chosen hashing scheme (e.g., sha256_crypt.verify()).

 Assumptions and Trade-offs
Minimal Validation: Implemented basic validation; additional constraints like unique email and format checking can be added later.

Password Hashing with Pure Python Backend: Used a built-in hash scheme from passlib (e.g., sha256_crypt, pbkdf2_sha256) to avoid external dependencies like bcrypt. While secure, for production, using stronger algorithms such as argon2 is advisable.

SQLite Chosen for Simplicity: Used SQLite for ease of development. PostgreSQL or MySQL is recommended for scaling in production environments.
 
What I Would Do With More Time
Security Enhancements:

Upgrade password hashing to argon2 for stronger security.

Implement OAuth-based login (e.g., Google or GitHub).

Testing:

Add full unit and integration test coverage for routes and services.

Error Handling:

Improve error responses with custom exceptions and error messages.

Role-Based Access Control:

Add support for user roles (e.g., admin, user) to manage permissions.

Database Optimization:

Switch to PostgreSQL and add indexing to improve performance.

AI Usage
Tools Used:
ChatGPT (OpenAI)

GitHub Copilot

AI Helped With:
Code Refactoring:

Suggested improved structure for route and controller logic.

Bug Fixing:

Helped debug hashing issues and resolve missing table/database errors.

Documentation:

Assisted in summarizing the changes and decisions made throughout the development.

AI-Suggested Code That Was Modified or Rejected:
Modified:

Password hashing logic was updated to use a supported algorithm (sha256_crypt or similar), not bcrypt.

Rejected:

Some route setup and error handling suggestions were adjusted to better fit Flask’s best practices and the project constraints.