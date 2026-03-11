import { useState } from "react";

type LiftIssue = {
  issue: string;
  severity: string;
  message: string;
};

type LiftAnalysis = {
  exercise_type: string;
  rep_count: number;
  score: number;
  feedback: string;
  issues: LiftIssue[];
};

export default function App() {
  const [result, setResult] = useState<LiftAnalysis | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeLift = async (exerciseType: string) => {
    try {
      setLoading(true);
      setError("");
      setResult(null);

      const response = await fetch("http://127.0.0.1:8000/analyze-lift", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          exercise_type: exerciseType,
          video_url: "test.mp4",
          user_id: "qingyuan",
        }),
      });

      if (!response.ok) {
        throw new Error("Request failed");
      }

      const data: LiftAnalysis = await response.json();
      setResult(data);
    } catch (err) {
      setError("Failed to analyze lift. Make sure the backend is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial, sans-serif" }}>
      <h1>CoachMeAI</h1>
      <p>AI Lift Coach</p>

      <div style={{ display: "flex", gap: "12px", marginBottom: "20px" }}>
        <button onClick={() => analyzeLift("squat")}>Analyze Squat</button>
        <button onClick={() => analyzeLift("deadlift")}>Analyze Deadlift</button>
        <button onClick={() => analyzeLift("bench")}>Analyze Bench</button>
      </div>

      {loading && <p>Analyzing lift...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h2>Results</h2>
          <p><strong>Exercise:</strong> {result.exercise_type}</p>
          <p><strong>Rep Count:</strong> {result.rep_count}</p>
          <p><strong>Score:</strong> {result.score}</p>
          <p><strong>Feedback:</strong> {result.feedback}</p>

          <h3>Issues</h3>
          <ul>
            {result.issues.map((issue, index) => (
              <li key={index}>
                <strong>{issue.issue}</strong> ({issue.severity}) — {issue.message}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}