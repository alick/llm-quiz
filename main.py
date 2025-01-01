from langchain_openai import ChatOpenAI
import logging


def main():
    logging.basicConfig(level=logging.DEBUG)
    question = "宫廷玉液酒"
    model = ChatOpenAI(model="gpt-4o", temperature=0, max_tokens=200)
    ai_msg = model.invoke(question)
    logging.debug(f"{ai_msg=}")
    ans = ai_msg.content
    print(ans)


if __name__ == "__main__":
    main()
