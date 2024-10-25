# Testing LLM for quality accessibility code recommendations

To set this up, you will need to

1. Create [an Azure OpenAI resource](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/GalleryItemDetailsBladeNopdl/id/Microsoft.CognitiveServicesOpenAI/)
2. [Set up a deployment of the LLM model](https://oai.azure.com/) of your choosing
3. Put the credentials & such in an [.env file](#env-file-setup) in the root of the project
4. [Install the dependencies](#dependencies)

# .env File Setup

```env
AZURE_OPENAI_API_BASE=https://YOUR_PROJECT.openai.azure.com/
AZURE_OPENAI_API_KEY=*******************
AZURE_OPENAI_API_MODEL=YOUR_DEPLOYENT_NAME
AZURE_OPENAI_API_VERSION=THE_API_VERSION
```

The best place to get your credentials is in the Playground. Pick the "Chat" playground and then click View Code and choose "Key Authentication" to find the Endpoint (API Base), API Key, and API version (at the end of the ENDPOINT string in the Python code).

# Dependencies

You’ll need to install dotenv to pull in the environment variables:

```bash
pip install python-dotenv
```

# Configuring the Tests

Tests are stored in the `tests.json` file. Each test contains a `title` string, `prompts` array of prompt strings, and an optional `prefix` string that will be added before each prompt in the test. For example:

```json
{
  "title": "Radio Group",
  "prefix": "Given the options light, dark, and high contrast, create the HTML only (no JavaScript) for",
  "prompts": [
    "a radio group to choose a theme",
    "a “theme” picker using radio controls",
    "a radio control-based theme chooser",
    "an accessible theme chooser with radio controls"
  ]
}
```

# Running the Tests

You run the project by typing `python run_tests.py`
