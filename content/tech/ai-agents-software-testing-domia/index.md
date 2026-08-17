---
title: "How AI Agents Will Replace Software Testers: A Concrete Example"
date: 2026-04-07
relatedProject: "domia"
summary: "Chat, function calling, agent loops — then DOMIA, an autonomous QA agent that tests a live site with no selectors, judges a screenshot with vision, and writes its own evidence to disk."
description: "A practical guide to what AI agents actually are, and DOMIA — an autonomous end-to-end testing agent built on Google ADK and Gemini."
tags: ["AI", "Testing", "Python"]
cover:
    image: "04-domia-architecture.jpg"
    alt: "DOMIA architecture: the agent loop, its tools, and the drivers for web, mobile and desktop"
    relative: true
canonicalOriginal: "https://www.linkedin.com/pulse/concrete-example-how-ai-replace-software-testers-tnv-mellah--9vbxe"
canonicalOriginalName: "LinkedIn"
---

*A practical guide for engineers, QA leads, and managers who want to understand
what AI agents really are — and how they are changing the way we test and
validate software.*

This article is split into two parts. The first part is short — just enough to
understand the building blocks. The second part is where things get interesting:
a real-world example of an AI agent that tests software autonomously. I built it,
it is working well, and I called it **DOMIA**.

## Part 1 — The building blocks

### 1. Chat: the foundation

Everyone has used a chatbot by now. You type something, the model replies. That's
it.

{{< figure src="01-chat.jpg" alt="Diagram of a chat exchange: a prompt goes into the model, a reply comes out" caption="Chat: text in, text out." >}}

The model reads your text, predicts the most likely useful response, and sends it
back. In this code snippet, we see how you can create a chat model using Gemini:

```python
import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="What is the capital of France?",
)
print(response.text)

# ── Expected output
# Paris
```

### 2. Function calling: the AI picks up tools

Chat alone can't look up today's weather, query a database, or click a button. It
only knows what was in its training data. Function calling fixes that. You give
the model a list of tools it can use, and it decides *when* to call them and
*with which arguments* — you don't have to route it manually.

{{< figure src="02-function-calling.jpg" alt="Diagram of function calling: the model returns a tool request, your code executes it and returns the result" caption="The model asks; your code runs the tool and hands back the result." >}}

The key thing that needs to be understood: **the model does not run the tool.**
It returns a request — a JSON object saying "call this function with these args".
Your code runs the actual function and feeds the result back. This is very
powerful because **it allows you to run tools in your environment**.

```python
import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 1. Define the tool
def get_weather(city: str) -> dict:
    """Returns the current weather for a given city."""
    # In a real app this would call a weather API.
    ...

# 2. Ask the model something that requires the tool.
chat = client.chats.create(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(tools=[get_weather]),
)
response = chat.send_message("What's the weather like in Paris right now?")

# ── Expected output ──────────────────────────────────────────────────────────
# Tool called : get_weather({'city': 'Paris'})
# Tool result : {'temp': '18°C', 'condition': 'Cloudy'}
```

### 3. AI agent frameworks: closing the loop

A single tool call is useful. But what if the task requires 10 steps? What if the
model needs to look at the result, decide what to do next, call another tool, and
keep going? That's an **agent**: a model in a loop, with memory and tools, that
keeps acting until it reaches a goal.

{{< figure src="03-agent-loop.jpg" alt="Diagram of the agent loop: plan, act, observe, repeat until the goal is reached" caption="Plan, act, observe, repeat — the agent loop." >}}

A few frameworks that make building agents practical today: **Google ADK** (great
for Gemini-based and multi-agent systems), **OpenAI Agents SDK** (built around
GPT and agent handoffs), **LangChain** (for custom control flow), **Claude Agent
SDK**, and others.

The agent loop handles everything: inject the state, let the model pick the next
tool, run it, feed results back, repeat. You write the tools; the framework runs
the loop.

```python
from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import FunctionTool

# 1. Define what the agent can do (tools)
def navigate(url: str) -> dict:
    """Navigate the browser to a URL."""
    return {"status": "success"}

def click(ref: str) -> dict:
    """Click an element identified by its ARIA ref."""
    return {"status": "success"}

# 2. Build the agent — give it a goal and tools, nothing else
agent = LlmAgent(
    name="web_tester",
    model="gemini-2.0-flash",
    instruction="You are a web testing agent. Use the tools to complete the given task.",
    tools=[FunctionTool(navigate), FunctionTool(click)],
)

# 3. Run it — the agent decides which tools to call and in which order
session_service = InMemorySessionService()
runner = Runner(agent=agent, app_name="demo", session_service=session_service)
session = session_service.create_session_sync(app_name="demo", user_id="user1")

# Expected output:
# → [tool] navigate called with https://example.com
# → [tool] click called with first link ref
# → "I navigated to example.com and clicked the first link."
```

## Part 2 — DOMIA: an agent that tests your software

This is the part that actually matters. Let's talk about a real problem:
**end-to-end (E2E) test automation** — across web, mobile, and desktop apps.

### Why test automation is hard

Traditional E2E tests are written like this:

```python
driver.find_element(By.ID, "submit-btn").click()
assert driver.find(By.CLASS_NAME, "success-msg").is_displayed()
```

Change the button ID, rename the class, add an animation — the test breaks.
Someone has to fix it. On a fast-moving product, that someone ends up spending
more time maintaining tests than catching real bugs.

And the more complex the scenario, the worse it gets. A test that covers sign-up
→ email confirmation → login → onboarding takes a week to write and breaks
constantly.

### What makes AI different here

An AI agent doesn't care about selectors. It looks at the page the way a human QA
engineer does — reading labels, understanding context, figuring out what to
click. If you rename a button from "Submit" to "Continue", the agent still finds
it. This is what we call **self-healing**: the test adapts to the UI instead of
breaking.

Three capabilities make this possible:

- **Visual perception** — the agent reads screenshots the way a human tester
  would, catching visual regressions and layout issues that pure DOM and output
  text data inspection misses.
- **Natural language acceptance criteria** — you describe *what* the
  system-under-test should do, not *how* to drive the browser step by step.
- **Built-in test oracle** — the model itself can judge whether the observed
  state matches the expected outcome, without you hardcoding every assertion.

### Introducing DOMIA

**DOMIA** is an autonomous QA agent. You give it a target system — a URL for web
apps, a mobile app, an Electron window — and a plain-English goal expressed as
acceptance criteria. It navigates, clicks, types, scrolls, reads — and returns a
structured verdict: PASS, FAIL, or UNCERTAIN, with a full execution trace as
evidence.

We'll show three concrete runs: a multilingual UI regression, a visual assertion
that requires a vision-capable model (VLLM), and a cross-layer test that writes a
file to disk using a shell tool.

{{< figure src="04-domia-architecture.jpg" alt="DOMIA architecture: Google ADK agent loop, Gemini with vision, and drivers for Playwright, Appium and Electron" caption="DOMIA under the hood." >}}

Under the hood:

- **Google ADK** manages the agent loop (plan → act → observe → repeat).
- **Gemini** is the model, vision enabled — it sees screenshots, videos, and more.
- The underlying driver — Playwright for web, Appium for mobile, or Electron APIs
  for desktop — controls the actual app, the same SUT your users hit.
- Every action (click, type, navigate, shell command) is a tool the model can
  call.
- Results are stored with full observability: every step, tool call, screenshot,
  and verdict is recorded, so failures are reproducible and debuggable.

### Example 1 — Multilingual UI regression (ibraverse.ca)

**Acceptance criterion:** *"Open ibraverse.ca and verify that the website supports
at least 3 languages — English, French, and one other."*

No selectors. No hardcoded text comparisons. DOMIA navigates the site, finds the
language switcher, cycles through options, and checks that the content actually
changes. A traditional regression test would break every time the language menu
is redesigned. DOMIA doesn't care — it reads the UI the way a human tester would.

{{< figure src="05-demo-multilingual.jpg" alt="Still from the recording of DOMIA cycling through the site's languages and returning PASS" caption="Recording: DOMIA opens ibraverse.ca, cycles through languages and returns PASS. [Watch the recording on LinkedIn](https://www.linkedin.com/pulse/concrete-example-how-ai-replace-software-testers-tnv-mellah--9vbxe)." >}}

### Example 2 — Visual understanding with a VLLM (is Brahim smiling?)

This one can't be done without vision. The acceptance criterion is: *"Look at the
profile photo of Brahim on the page and verify he is smiling."*

No DOM element can answer that. A traditional E2E test has no way to pass. But
DOMIA, running with a vision-capable model, takes a screenshot, looks at the
image, and judges the expression — the same way a human QA reviewer would during
a visual review.

This scenario **passes only when vision is enabled**. With a text-only model,
DOMIA correctly returns FAIL: it can read the alt text, but can't verify the
actual image content.

{{< figure src="06-demo-vision.jpg" alt="Still from the recording of DOMIA judging a photo with a vision model and returning PASS" caption="Recording: DOMIA with a vision model navigates to the page, captures the photo, and returns PASS with the model's reasoning as evidence. [Watch the recording on LinkedIn](https://www.linkedin.com/pulse/concrete-example-how-ai-replace-software-testers-tnv-mellah--9vbxe)." >}}

### Example 3 — Cross-layer test with shell tools (counting articles)

**Acceptance criterion:** *"Count how many articles are published on the website
and write the result into a local file called `article_count.txt` in the desktop
folder."*

This passes **only when the shell tool is enabled**. Without it, DOMIA can see the
article count on screen but has no way to write it to disk. With the shell tool
active, the agent reads the count from the page and calls
`echo "2" > article_count.txt` on its own — no human needed.

This illustrates a broader class of tests: scenarios where the verdict requires
acting on the environment, not just reading it. Think of it as **agentic
reporting** — the agent not only verifies a condition but produces an artifact as
evidence.

{{< figure src="07-demo-shell.jpg" alt="Still from the recording of DOMIA running a shell command and the evidence file appearing on disk" caption="Recording: DOMIA navigates, counts, runs the shell command, and the article_count.txt file appears on disk in real time. [Watch the recording on LinkedIn](https://www.linkedin.com/pulse/concrete-example-how-ai-replace-software-testers-tnv-mellah--9vbxe)." >}}

### The bigger picture

DOMIA is built for E2E and TNV testing across every major app type — the same
goal syntax works everywhere, only the driver changes:

- **Perception** — after every action, DOMIA captures a screenshot (and video)
  and the data, and feeds both to the model. This is what makes self-healing
  work: the agent sees the app the way a human tester does, not through
  hardcoded selectors.
- **Shell tool** — the agent can run terminal commands mid-test: `curl` an API,
  query a database, check a file, write evidence to disk. This is what makes
  cross-layer TNV possible in a single run.
- **Vision** — `--vision` switches the model to multimodal mode. The agent sees
  real screenshots, not just the DOM or text — useful for visual regression,
  image checks, and UI states that aren't exposed in the accessibility tree.
- **Workflows** — define a sequence of test goals in a file and run them as a
  batch. Each step is plain English. Steps can continue on failure so the full
  suite runs even when something breaks.
- **Reports** — `--report html` for a human-readable summary, `--report junit`
  for CI (Jenkins, GitHub Actions, GitLab CI). Every run is also persisted in a
  local SQLite database — re-inspect any step, re-run any scenario, track trends
  over time.
- **Plugins** — drop a JS file into `~/.domia/plugins/` and the agent gets a new
  tool automatically. No recompile needed.

### It's worth being honest about the limits

- **It's not magic.** Complex screens with heavy dynamic content, unusual
  gestures, or non-standard UI patterns — on any platform — can confuse the
  agent.
- **It's not free.** Every LLM call costs tokens. Running a full TNV campaign
  with hundreds of test cases against a cloud model gets expensive. The local
  model option (Example 2) helps bring cost and latency down for any platform.
- **It's best for high-value, complex scenarios.** For simple happy-path smoke
  tests on web, mobile, or desktop, use scripted automation — it's faster and
  cheaper. DOMIA shines on long, stateful user journeys — the UAT scenarios and
  cross-layer regression tests that are too expensive to maintain with
  traditional selector-based automation.

## Conclusion

Building DOMIA from scratch is what actually taught me how agents work — not
reading about them, but writing every line of Python: the tool definitions, the
session loop, the perception pipeline, the failure handling. You only really
understand the limitations when you hit them yourself. If you want to learn
agents, build one. Pick a problem you know well, give the model one tool, and see
what happens.

If you have ideas on how to improve DOMIA — better tools, smarter perception, new
platforms — reach out. I'm always happy to talk.

## Sources

- Google — [Agent Development Kit (ADK)](https://google.github.io/adk-docs/)
- Google — [Gemini API: function calling](https://ai.google.dev/gemini-api/docs/function-calling)
- OpenAI — [Agents SDK](https://openai.com/index/new-tools-for-building-agents/)
- [LangChain](https://www.langchain.com/)
- Anthropic — [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview)
- [Playwright](https://playwright.dev/) · [Appium](https://appium.io/)
