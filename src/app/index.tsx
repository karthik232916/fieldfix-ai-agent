import { createIssue } from "@/services/api";
import { useState } from "react";
import {
    Pressable,
    SafeAreaView,
    ScrollView,
    StyleSheet,
    Text,
    TextInput,
    View,
} from "react-native";

export default function HomeScreen() {
  const [issue, setIssue] = useState("");
  const [device, setDevice] = useState("");
  const [severity, setSeverity] = useState("medium");
  const [responseMessage, setResponseMessage] = useState("");

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.content}>
        <Text style={styles.title}>FieldFix AI 🔧</Text>

        <Text style={styles.subtitle}>
          AI-powered technical support for field engineers
        </Text>

        <View style={styles.card}>
          <Text style={styles.cardTitle}>What's wrong?</Text>

          <Text style={styles.description}>
            Describe the problem you're experiencing and FieldFix AI will help
            diagnose it.
          </Text>

          <TextInput
            style={styles.input}
            placeholder="Example: The warehouse scanner stopped working"
            placeholderTextColor="#888"
            multiline
            value={issue}
            onChangeText={setIssue}
          />

          <Text style={styles.description}>Device Name</Text>

          <TextInput
            style={styles.input}
            placeholder="Example: Warehouse Scanner"
            placeholderTextColor="#888"
            value={device}
            onChangeText={setDevice}
          />

          <Text style={styles.fieldLabel}>Severity</Text>

          <View style={styles.severityContainer}>
            {["low", "medium", "high"].map((level) => (
              <Pressable
                key={level}
                style={[
                  styles.severityButton,
                  severity === level && styles.severityButtonSelected,
                ]}
                onPress={() => setSeverity(level)}
              >
                <Text
                  style={[
                    styles.severityText,
                    severity === level && styles.severityTextSelected,
                  ]}
                >
                  {level.toUpperCase()}
                </Text>
              </Pressable>
            ))}
          </View>

          <Pressable
            style={[styles.button, !issue.trim() && styles.buttonDisabled]}
            disabled={!issue.trim()}
            onPress={async () => {
              try {
                const result = await createIssue(issue, device, severity);

                console.log("API response:", result);

                setResponseMessage(result.message);
              } catch (error) {
                console.error("Failed to create issue:", error);
                setResponseMessage(
                  "Unable to connect to the FieldFix AI server.",
                );
              }
            }}
          >
            <Text style={styles.buttonText}>Diagnose Issue</Text>
          </Pressable>

          {responseMessage ? (
            <View style={styles.responseContainer}>
              <Text style={styles.response}>{responseMessage}</Text>

              <Text style={styles.responseDetail}>Device: {device}</Text>

              <Text style={styles.responseDetail}>
                Severity: {severity.toUpperCase()}
              </Text>
            </View>
          ) : null}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#F5F7FA",
  },

  content: {
    padding: 24,
  },

  title: {
    fontSize: 32,
    fontWeight: "700",
    color: "#111827",
    marginBottom: 8,
  },

  subtitle: {
    fontSize: 16,
    color: "#6B7280",
    marginBottom: 32,
    lineHeight: 24,
  },

  card: {
    backgroundColor: "#FFFFFF",
    padding: 24,
    borderRadius: 16,
  },

  cardTitle: {
    fontSize: 22,
    fontWeight: "600",
    color: "#111827",
    marginBottom: 10,
  },

  description: {
    fontSize: 15,
    color: "#6B7280",
    lineHeight: 22,
    marginBottom: 20,
  },

  input: {
    minHeight: 120,
    borderWidth: 1,
    borderColor: "#D1D5DB",
    borderRadius: 10,
    padding: 14,
    fontSize: 16,
    color: "#111827",
    textAlignVertical: "top",
    marginBottom: 16,
  },

  button: {
    backgroundColor: "#111827",
    padding: 16,
    borderRadius: 10,
    alignItems: "center",
  },

  buttonDisabled: {
    opacity: 0.4,
  },

  buttonText: {
    color: "#FFFFFF",
    fontSize: 16,
    fontWeight: "600",
  },
  response: {
    marginTop: 16,
    fontSize: 15,
    color: "#166534",
    textAlign: "center",
  },
  fieldLabel: {
    fontSize: 15,
    fontWeight: "600",
    color: "#111827",
    marginBottom: 8,
  },
  severityContainer: {
    flexDirection: "row",
    gap: 8,
    marginBottom: 16,
  },

  severityButton: {
    flex: 1,
    padding: 12,
    borderWidth: 1,
    borderColor: "#D1D5DB",
    borderRadius: 8,
    alignItems: "center",
  },

  severityButtonSelected: {
    backgroundColor: "#111827",
    borderColor: "#111827",
  },

  severityText: {
    fontSize: 13,
    fontWeight: "600",
    color: "#374151",
  },

  severityTextSelected: {
    color: "#FFFFFF",
  },
  responseContainer: {
    marginTop: 16,
  },

  responseDetail: {
    marginTop: 6,
    fontSize: 14,
    color: "#4B5563",
    textAlign: "center",
  },
});
