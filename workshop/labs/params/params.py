from typing import Annotated

import boto3
import typer


def get_text_response(model, input_content):

    session = boto3.Session()
    bedrock = session.client(service_name="bedrock-runtime")

    message = {"role": "user", "content": [{"text": input_content}]}

    response = bedrock.converse(
        modelId=model,
        messages=[message],
        inferenceConfig={"maxTokens": 2000, "stopSequences": []},
    )

    return response["output"]["message"]["content"][0]["text"]


# response = get_text_response(sys.argv[1], sys.argv[2])


def main(
    input_content: str,
    modelId: Annotated[str, typer.Argument()] = "us.amazon.nova-pro-v1:0",
):
    print(get_text_response(modelId, input_content))


if __name__ == "__main__":
    typer.run(main)
