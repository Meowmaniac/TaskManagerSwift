# PROJECT CONTEXT

---

# Project Name

Task Manager

---

# Project Purpose

This repository is an educational iOS project.

Its primary purpose is to learn modern Swift development while building a real application from scratch.

The project serves three goals:

- learn modern iOS development;
- prepare for technical interviews;
- create a professional portfolio project.

Learning quality is always more important than development speed.

---

# Development Philosophy

The application is intentionally built gradually.

Architecture evolves together with the project.

Do not introduce abstractions before they solve a real problem.

Follow:

- KISS
- YAGNI
- SOLID
- Protocol-Oriented Programming
- Composition over inheritance

Avoid overengineering.

---

# Repository Structure

ios-learning/

├── handbook/
│
├── prompts/
│
├── agents/
│
├── examples/
│
├── scripts/
│
├── task-manager-core/
│
└── task-manager-ios/

---

# Responsibilities

task-manager-core

Contains platform-independent business logic.

Must compile as a Swift Package.

Contains:

- Domain
- Data
- Infrastructure
- Shared

Must NOT depend on:

- SwiftUI
- UIKit
- AppKit
- CoreLocation
- AVFoundation
- MapKit

Only Foundation and other cross-platform APIs are allowed unless explicitly approved.

---

task-manager-ios

Contains the Apple platform application.

Responsible for:

- SwiftUI
- Navigation
- ViewModels
- UI Components
- App lifecycle
- Platform integrations

Must depend on task-manager-core.

Core must NEVER depend on task-manager-ios.

Dependency direction is strictly one-way.

task-manager-ios

↓

task-manager-core

---

# Current Scope

Current application:

Simple Task Manager.

This is intentionally a small application.

Only implement features listed in this document.

Avoid adding extra functionality.

---

# Functional Requirements

The application manages personal tasks.

Each task contains:

- unique identifier;
- title;
- additional description;
- due date;
- due time;
- priority;
- completion status.

Priority supports:

- Low
- Medium
- High

Completion status:

- Completed
- Not completed

---

# CRUD Requirements

The application must support:

Create task

Read task

Update task

Delete task

No additional operations should be implemented unless added later to the roadmap.

---

# Main Screen

The application starts with a Task List screen.

Responsibilities:

Display all tasks.

Display task title.

Display due date.

Display priority.

Display completion checkbox.

Allow navigation to task details.

Allow creating a new task.

Allow editing an existing task.

Allow deleting a task.

Allow marking task as completed.

This screen represents the primary workflow.

---

# Task Details Screen

Displays complete task information.

Allows:

Edit

Save

Delete

Cancel

---

# Create Task Screen

Allows entering:

Title

Description

Date

Time

Priority

Validation:

Title is required.

---

# Data Persistence

At the beginning of the project:

Simple local storage only.

No cloud synchronization.

No authentication.

No networking.

Persistence technology will be introduced later according to the roadmap.

---

# Non Functional Requirements

Code must be:

Readable

Maintainable

Testable

Small

Modular

Scalable

Educational

---

# Architecture Goals

The project gradually introduces:

Protocols

SOLID

Dependency Injection

Repository Pattern

MVVM

Coordinator

Clean Architecture

Concurrency

Testing

Each concept is introduced only when required.

---

# Learning Strategy

Every new concept should satisfy three conditions:

1.

Solve a real project problem.

2.

Appear naturally during development.

3.

Become part of interview preparation.

Avoid introducing concepts only for demonstration.

---

# Coding Standards

Prefer:

small files

single responsibility

explicit naming

value semantics

dependency injection

protocol abstractions

Avoid:

God objects

Singleton abuse

Massive ViewModels

Deep inheritance

Premature optimization

Hidden dependencies

---

# Project Evolution

The project intentionally evolves.

Future features will be introduced gradually.

Examples:

Search

Sorting

Filtering

Categories

Notifications

Recurring tasks

Widgets

Cloud synchronization

Offline cache

These features are NOT part of the current milestone.

---

# Current Milestone

MVP

The goal is a fully working task manager.

Required functionality:

✓ Task list

✓ Create task

✓ Edit task

✓ Delete task

✓ Mark completed

✓ Local persistence

Everything else is postponed.

---

# Testing Strategy

Testing will be introduced gradually.

Eventually the project should include:

Unit Tests

Repository Tests

Business Logic Tests

ViewModel Tests

UI Tests

Only after the corresponding concepts are learned.

---

# Documentation

Every important architectural decision must be documented.

Every completed milestone must be summarized.

Every new pattern should have:

- lesson;
- implementation;
- documentation.

---

# Git Workflow

Development should be incremental.

Small commits.

Small pull requests.

Clear commit messages.

Never rewrite large parts of the project without architectural approval.

---

# Success Criteria

The project is successful if:

- it demonstrates modern iOS development;
- it is understandable by another developer;
- every architectural decision has a clear reason;
- every implemented concept can be explained during an interview;
- the application remains simple while demonstrating professional engineering practices.

The repository should be suitable as both a learning resource and a portfolio project.