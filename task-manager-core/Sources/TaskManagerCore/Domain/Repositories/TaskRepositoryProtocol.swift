import Foundation

public protocol TaskRepositoryProtocol {
    func saveTask(_ task: Task) throws
    func getTasks() -> [Task]
    func updateTask(_ task: Task) throws
    func deleteTask(withId id: String) throws
}