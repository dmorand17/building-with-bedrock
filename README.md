# Building with Amazon Bedrock

Training assets, notebooks, and notes produced while working through the AWS
[**Building with Amazon Bedrock**](https://catalog.workshops.aws/building-with-amazon-bedrock/en-US)
workshop. This is a personal learning repo — code here is for experimentation
and reference, not production use.

The workshop covers invoking foundation models, prompt engineering,
retrieval-augmented generation (RAG) with Knowledge Bases, embeddings and
semantic search, image generation, and building agents — all on Amazon Bedrock.

## 🚀 Quick start

```bash
# Create a virtual environment and install dependencies
uv sync

# Authenticate to AWS (Bedrock model access must be enabled in your region)
aws sso login   # or: aws configure

# Confirm Bedrock access and list available models
uv run aws bedrock list-foundation-models --region us-east-1
```

## 📋 Prerequisites

- **Python 3.13+** and [`uv`](https://docs.astral.sh/uv/) for dependency and environment management
- **AWS account** with [Bedrock model access enabled](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)
  for the models used in each lab (Anthropic Claude, Amazon Titan, etc.)
- **AWS CLI v2** and **boto3 ≥ 1.34** — older versions lack the Converse API and Agents support
- Credentials configured for a role with least-privilege Bedrock permissions
  (avoid `AmazonBedrockFullAccess`; scope to the actions and model ARNs each lab needs)

## 📚 Labs

Assets are added per lab as I work through the workshop. Each lab lives in its
own subfolder with a short README describing what it demonstrates.

| Lab | Topic | Key Bedrock feature |
|-----|-------|---------------------|
| Text playground | Prompt engineering fundamentals | `bedrock-runtime` Converse API |
| Text generation | Summarization, Q&A, entity extraction | Converse API, prompt templates |
| Chatbot | Conversational memory | Multi-turn Converse |
| Embeddings | Semantic search over documents | Titan Embeddings V2 |
| RAG | Retrieval-augmented generation | Knowledge Bases |
| Image generation | Text-to-image | Titan Image Generator |
| Agents | Tool-using agents | Bedrock Agents / AgentCore |

## 💡 Usage

Invoke a model from the CLI to sanity-check access:

```bash
aws bedrock-runtime converse \
  --model-id us.anthropic.claude-sonnet-4-6 \
  --messages '[{"role":"user","content":[{"text":"Hello, Bedrock!"}]}]' \
  --inference-config '{"maxTokens":1024}' \
  --region us-east-1
```

> Always set `maxTokens` explicitly — leaving it unset defaults to the model's
> maximum and silently reserves far more quota than needed, a common cause of
> `ThrottlingException`.

Use the `us.` (or region-appropriate) inference-profile prefix on the model ID
for cross-region availability.

## 🔗 Resources

- [Building with Amazon Bedrock workshop](https://catalog.workshops.aws/building-with-amazon-bedrock/en-US)
- [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
- [Bedrock supported models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html)
- [Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)

## 📄 License

Personal learning repository. Workshop content and any referenced AWS materials
remain the property of Amazon Web Services.
