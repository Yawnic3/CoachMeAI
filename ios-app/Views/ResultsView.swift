import SwiftUI

struct ResultsView: View {
    @State private var analysis: LiftAnalysis?
    @State private var isLoading = false
    @State private var errorMessage: String?

    var body: some View {
        NavigationView {
            VStack(spacing: 16) {
                Button("Analyze Squat") {
                    Task {
                        await fetchAnalysis()
                    }
                }
                .padding()
                .frame(maxWidth: .infinity)
                .background(Color.blue)
                .foregroundColor(.white)
                .cornerRadius(10)

                if isLoading {
                    ProgressView("Analyzing lift...")
                }

                if let errorMessage = errorMessage {
                    Text(errorMessage)
                        .foregroundColor(.red)
                        .multilineTextAlignment(.center)
                }

                if let analysis = analysis {
                    VStack(alignment: .leading, spacing: 12) {
                        Text("Exercise: \(analysis.exerciseType.capitalized)")
                            .font(.headline)

                        Text("Rep Count: \(analysis.repCount)")
                        Text("Score: \(analysis.score)")
                        Text("Feedback: \(analysis.feedback)")
                            .padding(.top, 4)

                        Text("Issues")
                            .font(.headline)
                            .padding(.top, 8)

                        ForEach(analysis.issues) { issue in
                            VStack(alignment: .leading, spacing: 4) {
                                Text(issue.issue.replacingOccurrences(of: "_", with: " ").capitalized)
                                    .font(.subheadline)
                                    .bold()
                                Text("Severity: \(issue.severity.capitalized)")
                                Text(issue.message)
                                    .foregroundColor(.secondary)
                            }
                            .padding()
                            .frame(maxWidth: .infinity, alignment: .leading)
                            .background(Color(.systemGray6))
                            .cornerRadius(10)
                        }
                    }
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .padding()
                }

                Spacer()
            }
            .padding()
            .navigationTitle("CoachMeAI")
        }
    }

    private func fetchAnalysis() async {
        isLoading = true
        errorMessage = nil

        do {
            analysis = try await APIService.shared.analyzeLift(
                exerciseType: "squat",
                videoURL: "https://example.com/test.mp4",
                userID: "qingyuan"
            )
        } catch {
            errorMessage = "Failed to analyze lift: \(error.localizedDescription)"
        }

        isLoading = false
    }
}