import Foundation

final class InMemoryTaskRepository: TaskRepositoryProtocol {
    private var tasks: [Task] = []
    private let queue = DispatchQueue(label: "com.taskmanager.inmemoryrepo")

    func saveTask(_ task: Task) throws {
        queue.sync {
            if tasks.contains(where: { $0.id == task.id }) {
                throw TaskRepositoryError.taskAlreadyExists
            }
            tasks.append(task)
        }
    }

    func getTasks() -> [Task] {
        queue.sync {
            tasks
        }
    }

    func updateTask(_ task: Task) throws {
        queue.sync {
            guard let index = tasks.firstIndex(where: { $0.id == task.id }) else {
                throw TaskRepositoryError.taskNotFound
            }
            tasks[index] = task
        }
    }

    func deleteTask(withId id: String) throws {
        queue.sync {
            guard let index = tasks.firstIndex(where: { $0.id == id }) else {
                throw TaskRepositoryError.taskNotFound
            }
            tasks.remove(at: index)
        }
    }
}

enum TaskRepositoryError: Error {
    case taskAlreadyExists
    case taskNotFound
}