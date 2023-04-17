import random
import matplotlib.pyplot as plt

# Define the survey questions and possible responses
questions = [
    "How concerned are you about crime?",
    "How concerned are you about murder?",
    "How concerned are you about global warming?",
    "How concerned are you about technology?",
    "How concerned are you about privacy?",
    "How concerned are you about healthcare?",
    "How concerned are you about education?",
    "How concerned are you about income inequality?",
    "How concerned are you about political corruption?",
    "How concerned are you about terrorism?"
]
responses = [
    "Very concerned",
    "Somewhat concerned",
    "Not very concerned",
    "Not at all concerned"
]

# Prompt the user for the number of participants
num_participants = int(input("Enter the number of participants: "))

# Initialize a list to store the responses
all_responses = []

# Generate random responses for the specified number of people
for i in range(num_participants):
    print(f"Participant {i+1}")
    participant_responses = []
    for question in questions:
        response = random.choice(responses)
        print(f"{question} {response}")
        participant_responses.append(response)
    all_responses.append(participant_responses)

# Count the number of each type of response
counts = {
    "Very concerned": 0,
    "Somewhat concerned": 0,
    "Not very concerned": 0,
    "Not at all concerned": 0
}
for participant_responses in all_responses:
    for response in participant_responses:
        counts[response] += 1

# Print the number of each type of response
for response, count in counts.items():
    print(f"{response}: {count}")

# Create a pie chart of the results
labels = list(counts.keys())
values = list(counts.values())
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Survey Results")

# Save the pie chart to a specific directory
# Choise your directory before last /
#plt.savefig("/survey_results.png") 

# Show the pie chart
plt.show()

# Analyze the results using comparatives
print("Compared to the other concerns in the survey, people are:")
if counts["Very concerned"] > counts["Somewhat concerned"]:
    print("More people are very concerned than somewhat concerned.")
elif counts["Very concerned"] < counts["Somewhat concerned"]:
    print("More people are somewhat concerned than very concerned.")
else:
    print("Equally many people are very concerned and somewhat concerned.")
if counts["Not very concerned"] > counts["Not at all concerned"]:
    print("More people are not very concerned than not at all concerned.")
elif counts["Not very concerned"] < counts["Not at all concerned"]:
    print("More people are not at all concerned than not very concerned.")
else:
    print("Equally many people are not very concerned and not at all concerned.")
