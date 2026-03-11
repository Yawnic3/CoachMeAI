import Foundation

struct LiftIssue: Codable, Identifiable {
    let id: UUID()
    let issue: String
    let severity: String
    let message: String

    enum CodingKeys: String, CodingKey {
        case issue
        case severity
        case message
    }
}

struct LiftAnalysis: Codable {
    let exerciseType: String
    let repCount: Int
    let score: Int
    let feedback: String
    let issues: [LiftIssue]

    enum CodingKeys: String, CodingKey {
        case exerciseType = "exercise_type"
        case repCount = "rep_count"
        case score
        case feedback
        case issues
    }
}