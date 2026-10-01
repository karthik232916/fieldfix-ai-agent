import type { IssueResponse } from "@/types/issue";

const API_BASE_URL = "http://192.168.0.2:8000";

export async function createIssue(
  description: string,
  device: string,
  severity: string,
): Promise<IssueResponse> {
  const response = await fetch(`${API_BASE_URL}/issues`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      description,
      device,
      severity,
    }),
  });

  if (!response.ok) {
    throw new Error(`API request failed: ${response.status}`);
  }

  return (await response.json()) as IssueResponse;
}
