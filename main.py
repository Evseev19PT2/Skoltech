import threading
from src.core.agent import FSAgent
from src import utils
from src.tools import fs


def main():
    print("🤖✨ File System Agent Initialized ✨🤖")
    print("Enter your request. Type 'exit' or 'quit' to leave.")

    agent = FSAgent()

    while True:
        try:
            prompt = input("👤 User: ")

            if prompt.lower().strip() in ["exit", "quit"]:
                print("🤖 Agent: Goodbye!")
                break

            stop_animation = threading.Event()
            animation_thread = threading.Thread(
                target=utils.animate, args=(stop_animation,)
            )
            animation_thread.start()

            try:
                agent.ask(prompt)
            finally:
                stop_animation.set()
                animation_thread.join()

            print("-" * 30)

        except KeyboardInterrupt:
            print("\n🤖 Agent: Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            print("-" * 30)


if __name__ == "__main__":
    main()
