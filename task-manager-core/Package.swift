// swift-tools-version: 6.3
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "task-manager-core",
    products: [
        // Products define the executables and libraries a package produces, making them visible to other packages.
        .library(
            name: "task-manager-core",
            targets: ["task-manager-core"]
        ),
    ],
    targets: [
        // Targets are the basic building blocks of a package, defining a module or a test suite.
        // Targets can depend on other targets in this package and products from dependencies.
        .target(
            name: "task-manager-core"
        ),
        .testTarget(
            name: "task-manager-coreTests",
            dependencies: ["task-manager-core"]
        ),
    ],
    swiftLanguageModes: [.v6]
)
