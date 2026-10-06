## Lesson Title
In-Memory Repository Implementation in Swift

## Learning Goal
Understand how to implement a simple in-memory repository pattern for task management in the Task Manager project.

## 1. Concept Explanation
A repository acts as an abstraction layer between your application and data storage. For our MVP, we'll implement an in-memory repository that:
- Provides a centralized place to manage tasks
- Encapsulates data access logic
- Enables easy replacement with other storage solutions later

## 2. Problem Before The Concept
Before repositories, we would:
- Directly manipulate data in ViewModels
- Repeat data access code across features
- Make testing difficult
- Create tight coupling between UI and data

## 3. Core Principles
A good repository should:
- Be protocol-oriented
- Use value types where possible
- Follow single responsibility principle
- Provide consistent API
- Be testable

## 4. Swift Examples
```swift
// TaskRepository.swift
protocol TaskRepository {
    func getAll() -> [Task]
    func save(_ task: Task)
    func delete(_ task: Task)
}

// InMemoryTaskRepository.swift
final class InMemoryTaskRepository: TaskRepository {
    private var tasks: [Task] = []

    func getAll() -> [Task] {
        tasks
    }

    func save(_ task: Task) {
        if let index = tasks.firstIndex(where: { $0.id == task.id }) {
            tasks[index] = task
        } else {
            tasks.append(task)
        }
    }

    func delete(_ task: Task) {
        tasks.removeAll(where: { $0.id == task.id })
    }
}
```

## 5. Real iOS Usage
In production apps, repositories are used for:
- Managing local cache
- Handling network requests
- Implementing business rules
- Providing data to multiple features

## 6. Advantages
- Decouples data access from business logic
- Makes testing easier
- Enables switching storage solutions
- Improves code maintainability

## 7. Disadvantages
- Not persistent (data lost on restart)
- Not scalable for large datasets
- Doesn't handle concurrency

## 8. Common Mistakes
Beginners often:
- Forget to make repository protocol-oriented
- Implement business logic in repositories
- Mix data access with UI logic
- Don't handle edge cases properly

## 9. Interview Preparation
### Junior Question
What is the purpose of a repository pattern?

### Middle Question
Implement a simple in-memory repository for a Task model

### Senior Question
Discuss trade-offs between in-memory repositories and persistent storage solutions

### Strong Answer Example
"A repository provides abstraction for data access. In our case, it allows us to centralize task management, make testing easier, and prepare for future storage solutions. However, it's not persistent and doesn't handle concurrency, which would require additional implementation."

### Weak Answer Example
"It's just a way to store data in memory."

## 10. Practice Task
Implement an in-memory repository for a new entity (e.g., Category) in the Task Manager project.

## 11. Summary
**Repository Pattern Cheat Sheet**
- ✅ Abstraction layer
- ✅ Centralized data access
- ✅ Easy to test
- ⚠️ Not persistent
- ⚠️ Limited scalability

Later in Task Manager this concept will be used for:
- Implementing local persistence
- Adding network storage
- Introducing dependency injection
- Building clean architecture

Related Topics:
- Protocol-Oriented Programming
- Dependency Injection
- Clean Architecture
- Unit Testing

Recommended Practice:
1. Implement the repository for tasks
2. Create a test that verifies repository functionality
3. Try adding a new feature that uses the repository
4. Explore how to make it persistent later