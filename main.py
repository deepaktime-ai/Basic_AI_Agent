from agent import Agent
import time


def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)
    print()


def main():
    print("=" * 50)
    print("🚀 Local AI Agent (Ollama + Llama3)")
    print("Type 'exit' to quit")
    print("=" * 50)

    agent = Agent()

    while True:
        try:
            user_input = input("\n🧑 You: ")

            if user_input.lower() in ["exit", "quit"]:
                print("👋 Goodbye!")
                break

            if not user_input.strip():
                print("⚠️ Empty input")
                continue

            print("\n⏳ Thinking...\n")

            response = agent.run(user_input)

            print("🤖 Agent:", end=" ")
            slow_print(response)

        except KeyboardInterrupt:
            print("\n👋 Stopped")
            break

        except Exception as e:
            print("❌ Error:", e)


if __name__ == "__main__":
    main()