from typing import Annotated

import boto3
import typer

app = typer.Typer()


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


def models():
    return ["us.amazon.nova-pro-v1:0", "mistral.mixtral-8x7b-instruct-v0:1"]


@app.command()
def main(
    modelId: Annotated[
        str, typer.Option(autocompletion=models)
    ] = "us.amazon.nova-pro-v1:0",
):

    input_content = typer.prompt("Input")
    print(get_text_response(modelId, input_content))


if __name__ == "__main__":
    typer.run(main)
