✅ Major Issues Identified
Missing users Table: The app initially crashed due to the users table not being present in the SQLite database.

Password Hashing Issue: Password hashing failed because the app was not properly configured to use a secure and available hashing backend.

404 Errors on POST, PUT, DELETE: These routes were unreachable due to misconfigured Flask route declarations or missing method handlers.

Authentication Failure: The login system wasn’t properly comparing plaintext passwords with hashed ones stored in the database.

🔧 Changes Made
Database Initialization: Created an init_db.py script to set up the SQLite database and create the required users table.

Password Hashing Fix: Replaced previous insecure or broken hashing logic with pbkdf2_sha256 via passlib. This uses a secure KDF and doesn’t require external system dependencies.

Route Fixes: Corrected Flask route definitions to ensure POST, PUT, DELETE, and other HTTP methods are registered and work as intended.

Login Fix: Updated login logic to use pwd_context.verify() for secure password checking using the pbkdf2_sha256 scheme.

⚖️ Assumptions and Trade-offs
Minimal Validation: Assumed simple form validation. Future improvements could include email uniqueness, password strength policies, and input sanitization.

Password Security: pbkdf2_sha256 provides strong password protection, with wide support and no system-level dependencies. For even stronger security, argon2 may be considered later.

SQLite Use: Chosen for development simplicity. Not ideal for production due to concurrency and scalability limitations — PostgreSQL is a better production choice.

🚀 With More Time, I Would...
Improve Security: Migrate to argon2 or integrate OAuth (e.g., Google, GitHub) for secure third-party login.

Add Tests: Write unit tests for authentication, CRUD operations, and error handling.

Handle Errors Better: Return structured JSON error responses and proper HTTP codes.

Role Management: Implement role-based access (e.g., admin, user) to restrict access to certain endpoints.

Optimize Database: Migrate to PostgreSQL with proper indexing and migrations using Alembic.

🤖 AI Usage Summary
Tools:
ChatGPT (by OpenAI)

GitHub Copilot

How AI Helped:
Code Refactoring: Assisted in writing and optimizing Flask routes and database interaction functions.

Troubleshooting: Helped debug missing table errors, password hashing issues, and HTTP method misconfigurations.

Documentation: Helped summarize issues and solutions for this CHANGES.md.

AI Code Review:
Rejected: All bcrypt-related code was removed due to unnecessary dependency issues.

Modified: Password handling logic was updated to use pbkdf2_sha256 from passlib, with CryptContext handling both hashing and verification.