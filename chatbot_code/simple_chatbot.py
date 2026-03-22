from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from config import DefaultConfig

def authenticate_client():
    return TextAnalyticsClient(
        endpoint=DefaultConfig.ENDPOINT_URI,
        credential=AzureKeyCredential(DefaultConfig.API_KEY)
    )

def analyze_sentiment(client, text):
    result = client.analyze_sentiment(documents=[text])[0]
    return result.sentiment

def chatbot():
    print("Azure AI Chatbot is running.")
    print("Type 'help' to see capabilities or 'exit' to quit.\n")

    try:
        client = authenticate_client()
    except Exception as e:
        print("Error connecting to Azure AI Service.")
        print(e)
        return

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        elif user_input.lower() in ["help", "capabilities", "what can you do"]:
            print("Bot: I can chat with you, analyze the sentiment of your text, and handle empty input.")

        elif not user_input:
            print("Bot: I did not understand that. Please type a valid message.")

        else:
            try:
                sentiment = analyze_sentiment(client, user_input)
                print(f"Bot: You said: {user_input}")
                print(f"Bot: Detected sentiment: {sentiment}")

                if sentiment == "positive":
                    print("Bot: That sounds positive. Glad to hear that!")
                elif sentiment == "negative":
                    print("Bot: That sounds negative. I hope things get better.")
                else:
                    print("Bot: That seems neutral.")
            except Exception as e:
                print("Bot: Sorry, I had trouble analyzing your message.")
                print("Error:", e)

if __name__ == "__main__":
    chatbot()