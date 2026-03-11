import Foundation

struct AnalyzeLiftRequest: Codable {
    let exerciseType: String
    let videoURL: String?
    let userID: String?

    enum CodingKeys: String, CodingKey {
        case exerciseType = "exercise_type"
        case videoURL = "video_url"
        case userID = "user_id"
    }
}

final class APIService {
    static let shared = APIService()

    private init() {}

    private let baseURL = "http://127.0.0.1:8000"

    func analyzeLift(exerciseType: String,
    videoURL: String? = nil,
    userID: String? = nil,) async throws -> LiftAnalysis {
        guard let url = URL(string: "\(baseURL)/analyze-lift") else {
            throw URLError(.badURL)
        }
    }

    let request = AnalyzeLiftRequest(exerciseType: exerciseType, videoURL: videoURL, userID: userID)

    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    request.httpBody = try JSONEncoder().encode(request)

    let (data, response) = try await URLSession.shared.data(for: request)

    guard let httpResponse = response as? HTTPURLResponse else {
        throw URLError(.badServerResponse)
    }

    guard 200..<300 ~= httpResponse.statusCode else {
        throw URLError(.badServerResponse)
    }

    let decoder = JSONDecoder()
    
    return try decoder.decode(LiftAnalysis.self, from: data)
}
