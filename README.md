# Testing LLM Code Generation for Accessibility

## Introduction

This project investigates gaps in Large Language Model (LLM) code generation models' knowledge of accessibility best practices. As LLMs become increasingly integrated into developer workflows through tools like GitHub Copilot, ChatGPT, and similar AI assistants, it's critical to understand how well these models generate accessible HTML and whether they can be improved through targeted training.

The goal of this research is to:
- Systematically evaluate how well LLMs generate accessible HTML code for common UI components
- Identify patterns in accessibility errors and omissions
- Develop a methodology for improving LLM code generation through diff-based learning
- Create a framework for ongoing assessment and improvement of accessibility in AI-generated code

## Investigation Details

This project tests a comprehensive set of **common HTML component patterns** across various categories:

- **Form Controls**: Text fields, email fields, select fields, radio groups, checkbox groups, textareas
- **Form States**: Required fields, validation errors, accessible descriptions, placeholders, patterns
- **Navigation Patterns**: Basic navigation, breadcrumbs, table of contents, mobile navigation with toggles
- **Data Display**: Tables with various header configurations, images with alt text, SVG graphics
- **Interactive Elements**: Links, buttons, progressive disclosure (details/summary), modal dialogs, popovers
- **Advanced Patterns**: Form controls with complex ARIA relationships, navigation with submenus, progress indicators

The test suite includes over 60 distinct component patterns, each designed to evaluate different aspects of accessibility implementation.

## Methodology

The testing methodology is designed to capture a wide range of LLM responses and identify consistent patterns in accessibility errors:

### Prompt Design
- **Multiple non-leading prompts** for each component (typically 4-5 variations per component)
- Each prompt uses different phrasing to avoid biasing the model toward specific implementations
- Prompts range from minimal instructions to explicit requests for accessible interfaces
- One prompt in each set specifically requests an "accessible" version to evaluate whether the model understands accessibility requirements

### Response Collection
- **Temperature setting**: Set to 0.95 for maximum variety in responses
- **Top-p sampling**: Set to 0.95 to allow diverse token selection
- **10 iterations per prompt**: Each prompt is run 10 times to collect unique responses
- Duplicate responses are filtered out to focus on unique implementations
- Responses are stored as individual HTML files organized by component and prompt

### Evaluation Process
- Each response is evaluated against an **accessibility rubric** covering:
  - Proper semantic HTML usage
  - ARIA attributes and their correct implementation
  - Form labeling and relationships
  - Error indication and description
  - Keyboard accessibility
  - Screen reader compatibility
- Errors and warnings are categorized and documented
- Common error patterns are identified across multiple responses

## Diff Generation (In Progress)

The diff generation process creates a bridge between error identification and model improvement:

### Individual Commit Workflow
1. Each problematic response is remediated manually to fix accessibility issues
2. Remediation is committed as a separate commit with:
   - Errors listed in the commit message header
   - Warnings included in the commit message
   - Specific accessibility violations documented

### Diff File Creation
The `diff-generator.sh` script:
- Extracts commits containing remediations
- Generates unified diff files for each remediation
- Adds comment headers to diffs that denote:
  - The specific issues found in the original code
  - The remediation needed to fix each issue
  - Best practices for accessible implementation

### Diff File Format
Each diff file includes:
- Error messages at the top explaining what was wrong
- A unified diff showing the exact changes made
- Context about accessibility best practices

Example diff structure:
```
Error: The `form` element was not requested.
Error: Use `aria-describedby` to reference a group description.
Note: For usability, put the description at the top after the label.

diff --git a/output/[Component]/[Prompt]/[UUID].html
--- a/output/[Component]/[Prompt]/[UUID].html
+++ b/output/[Component]/[Prompt]/[UUID].html
[actual diff content]
```

## Re-testing Infrastructure

The re-testing infrastructure demonstrates how diff data can influence future code generation and improve quality:

### System Prompt Enhancement
The `retest.py` script:
- Allows selection of specific component tests to re-run
- Incorporates one or more diff files into the system prompt
- Adds context: "In previous instances, I had to correct your code. Here are the diffs with comments as to what was incorrect:"
- Appends the diff content to help the model learn from past mistakes

### Hypothesis
By providing the LLM with concrete examples of:
- What it generated incorrectly
- Why it was incorrect (through error messages)
- How to fix it (through the diff)

The model should be able to:
- Generate more accessible code in subsequent attempts
- Learn accessibility patterns from the remediation examples
- Reduce common errors across similar components

### Evaluation of Improvement
The re-test outputs are stored separately in the `retest/` directory for comparison with original outputs, allowing measurement of:
- Reduction in specific error types
- Improvement in ARIA usage
- Better semantic HTML structure
- Overall accessibility compliance

---

## Setup and Usage

### Prerequisites

To set up this project, you will need to:

1. Create [an Azure OpenAI resource](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/GalleryItemDetailsBladeNopdl/id/Microsoft.CognitiveServicesOpenAI/)
2. [Set up a deployment of the LLM model](https://oai.azure.com/) of your choosing
3. Put the credentials in a `.env` file in the root of the project (see below)
4. Install the required dependencies

### .env File Setup

Create a `.env` file in the project root with the following variables:

```env
AZURE_OPENAI_API_BASE=https://YOUR_PROJECT.openai.azure.com/
AZURE_OPENAI_API_KEY=*******************
AZURE_OPENAI_API_MODEL=YOUR_DEPLOYMENT_NAME
AZURE_OPENAI_API_VERSION=THE_API_VERSION
```

The best place to get your credentials is in the Playground. Pick the "Chat" playground and then click View Code and choose "Key Authentication" to find the Endpoint (API Base), API Key, and API version (at the end of the ENDPOINT string in the Python code).

### Dependencies

Install the required Python packages:

```bash
pip install python-dotenv requests
```

### Configuring the Tests

Tests are stored in the `tests.json` file. Each test contains:
- `title`: A descriptive name for the component being tested
- `prompts`: An array of prompt variations to test
- `prefix` (optional): Text prepended to each prompt in the test

Example test configuration:

```json
{
  "title": "Radio Group",
  "prefix": "Given the options light, dark, and high contrast, create the HTML only (no JavaScript) for",
  "prompts": [
    "a radio group to choose a theme",
    "a "theme" picker using radio controls",
    "a radio control-based theme chooser",
    "an accessible theme chooser with radio controls"
  ]
}
```

### Running the Tests

Generate LLM responses for all component tests:

```bash
python run_tests.py
```

This will:
- Iterate through all tests in `tests.json`
- Run each prompt 10 times
- Save unique responses to the `output/` directory
- Organize files by component and prompt number

### Re-testing with Diffs

To re-test a component with accessibility corrections:

```bash
python retest.py
```

This interactive script will:
1. Display a list of available tests
2. Prompt you to select a test to re-run
3. Ask you to specify diff files to include in the system prompt
4. Run the selected test with the diff-enhanced prompt
5. Save results to the `retest/` directory

### Generating Diff Files

After remediating responses and committing them:

```bash
./diff-generator.sh <target_commit_hash>
```

This will generate diff files for all commits between HEAD and the target commit, storing them in the `diffs/` directory.
