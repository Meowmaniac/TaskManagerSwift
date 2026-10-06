## Lesson Title
Creating a Task Model in Swift

## Learning Goal
Understand how to create a simple data model in Swift and why it's essential for iOS development.

## 1. Concept Explanation
A data model represents the structure of data in an application. In iOS development, models are used to store and manage information independently of the UI. This allows for clean separation of concerns and makes the application easier to maintain.

## 2. Problem Before The Concept
Before structured data models, developers often stored data in unorganized ways, leading to inconsistencies and difficulty in managing complex data relationships. This made code harder to maintain and scale.

## 3. Core Principles
- Use `struct` for value types (immutable by default)
- Keep models simple and focused on data storage
- Use computed properties for derived values
- Make properties private when appropriate

## 4. Swift Examples
```swift
// Models/Task.swift
import Foundation

struct Task {
    let id: UUID
    let title: String
    let description: String
    var isCompleted: Bool
    let createdAt: Date

    init(title: String, description: String) {
        self.id = UUID()
        self.title = title
        self.description = description
        self.isCompleted = false
        self.createdAt = Date()
    }
}
```

## 5. Real iOS Usage
This model will be used in the `task-manager-core` module as the foundation for storing task data. It will later be integrated with persistence layers and used by ViewModels in the iOS app.

## 6. Advantages
- Clear data structure
- Easy to extend with new properties
- Supports immutability for safer code
- Separates data from UI logic

## 7. Disadvantages
- Not suitable for complex relationships (solved later with associated objects)
- Requires manual updates when requirements change

## 8. Common Mistakes
- Using `class` instead of `struct` for simple data models
- Making all properties public without considering encapsulation
- Forgetting to initialize all properties in the initializer

## 9. Interview Preparation
### Junior Question
What is the purpose of a data model in an iOS app?

### Middle Question
Why would you use a `struct` instead of a `class` for this model?

### Senior Question
How would you modify this model to support task priorities while maintaining immutability?

### Strong Answer Example
"A data model organizes information in a structured way. We use `struct` here because tasks are value types - when they're copied, the new instance has its own data. This makes the model safer and easier to reason about."

### Weak Answer Example
"I don't know, maybe it's just a way to store data."

## 10. Practice Task
Modify the Task model to add a `priority` property with an enum type. Implement it with a default value and update the initializer.

## 11. Summary
- Use structs for simple data models
- Keep models focused on data storage
- Use computed properties for derived values
- Make properties private when appropriate
- Models should be independent of UI logic

Related Topics:
- Swift Structs
- Data Modeling
- Value Types vs Reference Types

Recommended Practice:
Implement the Task model in `task-manager-core/Domain/Models/Task.swift` and test it with sample data.