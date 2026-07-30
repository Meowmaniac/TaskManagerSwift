# iOS Learning Roadmap

## Project Overview

### Goal

Build a complete Task Manager application while gradually learning modern iOS development and software engineering.

This roadmap combines **product development** with **engineering education**. Every new programming concept must appear naturally as a solution to a real problem encountered during development.

The project should evolve incrementally. Avoid introducing abstractions or architectural patterns until they become necessary.

---

# Learning Principles

Throughout the course we follow these principles:

* Learn by building.
* Architecture must evolve with the application.
* Every lesson introduces one or two new concepts only.
* Every concept must solve a real engineering problem.
* Prefer understanding over memorization.
* Prefer simple code over clever code.
* Every milestone must produce a working application.
* Every important topic should prepare for iOS interviews.

---

# Development Philosophy

The application should grow in complexity.

Do **not** start with Clean Architecture.

Do **not** start with Repository.

Do **not** start with Dependency Injection.

Instead:

Problem → Discussion → Solution → Refactoring → Better Architecture

This mirrors real software development.

---

# Final Application

By the end of the course the application should support:

* Create Task
* Read Tasks
* Update Task
* Delete Task
* Mark Task Completed
* Priority
* Due Date
* Due Time
* Local Persistence
* Search
* Sorting
* Filtering
* Notifications
* Unit Tests
* UI Tests

---

# Architecture Evolution

The application intentionally evolves through several architectural stages.

MVC

↓

MVVM

↓

MVVM + Coordinator

↓

Repository

↓

Dependency Injection

↓

Clean Architecture

Each transition should happen because the previous solution becomes difficult to maintain.

---

# BLOCK 1 — Project Foundation

## Product Goal

Create the project foundation.

## Engineering Goal

Learn Swift fundamentals and understand the repository structure.

### Lesson 1.1

Project overview

Repository structure

Git workflow

Swift Package Manager

### Lesson 1.2

Swift basics

* Variables
* Constants
* Types
* Functions

Practice

Create first Swift files.

### Lesson 1.3

Struct

Stored Properties

Computed Properties

Methods

Practice

Create the first Task model.

### Lesson 1.4

Enum

Access Control

Extensions

Practice

Improve Task model.

### Lesson 1.5

Protocols (Introduction)

Understand contracts.

Create a simple protocol.

No architecture yet.

### Milestone

Project builds successfully.

Task model exists.

---

# BLOCK 2 — First Working Application (MVC)

## Product Goal

Build the first complete Task Manager.

## Engineering Goal

Understand Apple's original MVC architecture.

### Lesson 2.1

MVC overview

Responsibilities

Model

View

Controller

### Lesson 2.2

Task List

Display all tasks.

### Lesson 2.3

Create Task

Title

Description

Date

Time

Priority

### Lesson 2.4

Edit Task

Update existing task.

### Lesson 2.5

Delete Task

Confirmation flow.

### Lesson 2.6

Complete Task

Checkbox

Completed state

### Lesson 2.7

Review MVC

Discuss Massive View Controller.

Identify problems.

### Milestone

Complete CRUD using MVC.

---

# BLOCK 3 — MVVM

## Product Goal

Refactor application.

## Engineering Goal

Separate presentation logic from UI.

### Lesson 3.1

Why MVC becomes difficult.

### Lesson 3.2

MVVM overview.

### Lesson 3.3

ViewModel responsibilities.

### Lesson 3.4

Data Binding.

### Lesson 3.5

Observable State.

### Lesson 3.6

Refactor CRUD.

Move business logic.

### Lesson 3.7

MVVM review.

Advantages

Disadvantages

Interview discussion.

### Milestone

Application fully migrated to MVVM.

---

# BLOCK 4 — SOLID & Repository

## Product Goal

Improve maintainability.

## Engineering Goal

Learn abstraction.

### Lesson 4.1

SOLID overview.

### Lesson 4.2

Single Responsibility Principle.

### Lesson 4.3

Dependency Inversion.

### Lesson 4.4

Repository Pattern.

### Lesson 4.5

Protocol-Oriented Programming.

### Lesson 4.6

Local Storage abstraction.

### Lesson 4.7

Repository implementation.

### Lesson 4.8

Refactor ViewModels.

### Milestone

ViewModels no longer communicate directly with storage.

---

# BLOCK 5 — Navigation & Coordinator

## Product Goal

Improve navigation.

## Engineering Goal

Separate navigation from presentation.

### Lesson 5.1

Navigation problems.

### Lesson 5.2

Coordinator Pattern.

### Lesson 5.3

Navigation flow.

### Lesson 5.4

Passing dependencies.

### Lesson 5.5

Deep linking overview.

### Lesson 5.6

Refactor navigation.

### Milestone

Navigation fully managed by Coordinator.

---

# BLOCK 6 — Clean Architecture

## Product Goal

Separate application layers.

## Engineering Goal

Understand scalable architecture.

### Lesson 6.1

Clean Architecture overview.

### Lesson 6.2

Entities.

### Lesson 6.3

Use Cases.

### Lesson 6.4

Repository interfaces.

### Lesson 6.5

Data Layer.

### Lesson 6.6

Dependency Injection.

### Lesson 6.7

Infrastructure layer.

### Lesson 6.8

Final architecture review.

### Milestone

Core application follows Clean Architecture.

---

# BLOCK 7 — Modern Swift

## Product Goal

Improve application quality.

## Engineering Goal

Master modern Swift.

### Lesson 7.1

Async/Await.

### Lesson 7.2

Tasks.

### Lesson 7.3

Actors.

### Lesson 7.4

MainActor.

### Lesson 7.5

Error Handling.

### Lesson 7.6

Swift Testing.

### Lesson 7.7

Performance basics.

### Milestone

Application uses modern Swift concurrency.

---

# BLOCK 8 — Production Features

## Product Goal

Finish MVP.

## Engineering Goal

Learn real-world engineering.

### Lesson 8.1

Search.

### Lesson 8.2

Sorting.

### Lesson 8.3

Filtering.

### Lesson 8.4

Notifications.

### Lesson 8.5

Accessibility.

### Lesson 8.6

App polishing.

### Lesson 8.7

Interview preparation.

### Lesson 8.8

Final code review.

### Milestone

Production-ready educational project.

---

# Technologies

Swift

SwiftUI

Swift Package Manager

Swift Testing

Swift Concurrency

Git

Markdown

---

# Engineering Topics

Swift Fundamentals

Protocol-Oriented Programming

SOLID

MVC

MVVM

Coordinator

Repository Pattern

Dependency Injection

Clean Architecture

Concurrency

Testing

Code Review

Documentation

Git Workflow

---

# Deliverables

By completing this roadmap the repository should contain:

* Complete Task Manager application.
* Cross-platform Swift Package.
* Native iOS application.
* Architecture documentation.
* Lesson handbook.
* Example implementations.
* Unit tests.
* Interview notes.
* Git history showing architectural evolution.

---

# Success Criteria

The course is complete when:

* The application is fully functional.
* Every architectural decision can be explained.
* Every implemented pattern is understood.
* The repository demonstrates professional engineering practices.
* The project is suitable as both an interview portfolio and a long-term reference for future iOS development.
