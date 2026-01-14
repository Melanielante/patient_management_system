🏥 Patient Management System
Project Status: In Progress

This repository contains a Patient Management System being developed as part of a Junior Developer Technical Assessment.
The project focuses on secure healthcare data access, patient consent enforcement, and audit logging, following best practices.

✅ What Has Been Implemented
🔧 Backend (FastAPI + MariaDB)
1. Project Setup

FastAPI project initialized

MariaDB configured

SQLAlchemy ORM in use

Alembic migrations set up and working

Environment variables managed via .env

2. Database Models & Migrations

The following models are implemented and migrated:

User

Roles: patient, healthcare_worker, admin

Password hashing

Email verification flag

Patient

Linked to User

National ID encrypted at rest

Personal details stored locally

Consent

Consent types: view, edit, share

Expiration & revocation supported

Status tracking (active, expired, revoked)

AccessLog

Logs all patient data access attempts

Stores who, what, when, and result

3. Authentication & Authorization

JWT-based authentication implemented

Login endpoint working

Role-based access control via FastAPI dependencies

Protected routes using require_role

4. Consent Enforcement Logic

Centralized ConsentService

Validates:

Active consent

Expiration

Permission hierarchy

Used before accessing patient data

5. Audit Logging

Access log logic implemented

Logs both allowed and denied access attempts

6. Encryption

Sensitive fields (e.g. National ID) encrypted at rest

Encryption isolated in utility logic

7. Mock Registry Integration (Backend Logic)

Registry verification service stub created

Patient registration validates against registry data

🚧 What Is Still To Be Done
🧱 Backend

Complete Mock Registry Service as a standalone container

Add API key authentication for registry access

Seed realistic registry data (20+ patients)

Add rate limiting middleware

Finalize refresh token rotation logic

🎨 Frontend (React + TypeScript)
Partially Started

React project initialized with TypeScript

Axios instance configured

Authentication context created (AuthProvider)

Token handling via localStorage

Still Pending

Fix Fast Refresh export issue (split hooks vs components)

Login/Register UI

Patient Dashboard:

View consents

Grant/Revoke consent

View access logs

Healthcare Worker Dashboard:

Search patient by National ID

View patient data (with consent)

Admin dashboard (optional)

🐳 Docker & Deployment

Dockerfiles still pending

docker-compose setup pending

Automatic migrations & seed data on startup

📄 Documentation

API documentation (Swagger/Postman)

Architecture diagram

Test scenarios documentation

📝 Notes

Core backend logic (auth, consent, access control) is functional

Security-first approach followed throughout implementation

Project prioritizes correctness and clarity over UI polish

Remaining work primarily involves frontend completion and containerization

🏁 Summary

This project currently delivers a working backend MVP with:

Secure authentication

Consent-based access control

Audit logging

Encrypted sensitive data

Frontend and deployment layers are in progress and planned as next steps.