
import streamlit as st


st.title("🔥 Cook Your Coding Skills")

st.subheader("🤖 Hey, this is your AI Coding Chatbot")

st.markdown("Ask me anything about coding and I will help you!")

st.divider()

# User details
name = st.text_input("Enter your name:")

age = st.number_input(
    "Enter your age:",
    min_value=1,
    max_value=100
)

about_you = st.text_area(
    "Tell me about yourself:"
)

rating = st.slider(
    "Rate your coding skills:",
    min_value=1,
    max_value=10
)

interests = st.multiselect(
    "Select your interests:",
    options=[
        "Development",
        "AI related concepts",
        "Frontend",
        "Full Stack",
        "Backend",
        "Python",
        "DSA",
        "SQL"
    ]
)

level = st.radio(
    "Select your level of knowledge:",
    options=[
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

st.divider()

# Select Ollama model
model = st.text_input(
    "Enter Ollama model:",
    value="llama3.2"
)

# User question
question = st.text_area(
    "💬 Enter your coding question:",
    placeholder="Example: Explain for loop in Python"
)

# Submit button
button = st.button("🚀 Ask AI")

if button:

    if question == "":
        st.warning("Please enter a question.")

    else:

        response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        st.success("🤖 AI Response:")

        st.write(response["message"]["content"])
