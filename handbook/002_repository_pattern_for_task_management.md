## Lesson Title
Repository Pattern for Task Management

## Learning Goal
Understand how to create a repository interface for managing tasks, its role in decoupling data access, and implement CRUD operations.

## 1. Concept Explanation
A repository acts as an abstraction layer between data sources (like local storage or API) and business logic. It provides a clean API for data access while hiding implementation details.

## 2. Problem Before The Concept
Before repositories, data access logic was often tightly coupled with business logic, making testing difficult and code harder to maintain. Direct database calls or API requests were scattered throughout the codebase.

## 3. Core Principles
- Encapsulate data access logic
- Provide a consistent API for data operations
- Decouple business logic from data sources
- Enable mocking for testing

## 4. Swift Examples
```swift
protocol TaskRepository {
    func fetchTasks(completion: @escaping (Result<[Task], Error>) -> Void)
    func createTask(_ task: Task, completion: @escaping (Result<Task, Error>) -> Void)
    func updateTask(_ task: Task, completion: @escaping (Result<Task, Error>) -> Void)
    func deleteTask(_ taskId: String, completion: @escaping (Result<Void, Error>) -> Void)
}
```

## 5. Real iOS Usage
In Task Manager, this interface will be implemented for:
- Local storage (Core Data/UserDefaults)
- Cloud synchronization (Firebase/Backend)
- Mock data for testing

## 6. Advantages
- Separation of concerns
- Easier testing with mock implementations
- Centralized data access logic
- Future-proof for changing data sources

## 7. Disadvantages
- Initial setup overhead
- Potential overengineering for simple projects
- Requires careful design to avoid bloating the interface

## 8. Common Mistakes
- Forgetting to handle errors properly
- Mixing repository logic with business rules
- Not following protocol strictly across implementations
- Overcomplicating the interface with unnecessary methods

## 9. Interview Preparation
### Junior Question
What is the purpose of a repository pattern in iOS development?
**Strong Answer:** It abstracts data access, decouples business logic from data sources, and makes testing easier.
**Weak Answer:** It's a way to store data.

### Middle Question
How would you implement a repository for task management?
**Strong Answer:** Define a protocol with CRUD methods, implement it for specific data sources, and inject the implementation where needed.

### Senior Question
What trade-offs should be considered when introducing a repository pattern?
**Strong Answer:** Benefits include testability and separation of concerns, but it adds initial complexity and requires careful interface design.

## 10. Practice Task
1. Create a `TaskRepository` protocol with fetch, create, update, and delete methods
2. Implement it for an in-memory storage solution
3. Add error handling for all operations
4. Write unit tests for the implementation

## 11. Summary
**Cheat Sheet:**
- Repository = abstraction layer for data access
- Use protocols to define interfaces
- Implement for different data sources
- Enables testing and future flexibility
- Follows SOLID principles (especially Dependency Inversion)

**Related Topics:**
- Dependency Injection
- SOLID Principles
- Unit Testing
- Data Layer Architecture

**Recommended Practice:**
Implement the repository pattern for task storage in the Task Manager project.