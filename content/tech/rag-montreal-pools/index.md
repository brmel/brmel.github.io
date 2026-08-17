---
title: "Generative AI, LlamaIndex, RAG and ChainLit: Finding the Next Available Pool in Montréal"
date: 2024-09-03
summary: "Montréal publishes every indoor pool schedule and no way to search them by time. A RAG chatbot over the scraped schedules, built in one afternoon — and why the result still made me uncomfortable."
description: "Building a retrieval-augmented chatbot over Montréal's indoor pool schedules with LlamaIndex, embeddings and ChainLit."
tags: ["Python", "LLM", "AI"]
cover:
    image: "05-chatbot-demo.jpg"
    alt: "The finished chatbot answering a question about pool availability, citing the pool's page as its source"
    relative: true
canonicalOriginal: "https://www.linkedin.com/pulse/how-i-used-generative-ai-llamaindex-rag-chainlit-create-mellah--ffmre"
canonicalOriginalName: "LinkedIn"
---

In this article, I will demonstrate how to use a Large Language Model (LLM) to
create a chatbot that can answer questions about pool availability in Montréal.

Using LLMs in a business can be highly beneficial, but allowing an LLM to operate
unchecked and make decisions can be risky, potentially leading to significant
issues and financial losses. For example, you can read about how Air Canada was
compelled to pay compensation due to a misleading response from an LLM:
[Washington Post article](https://www.washingtonpost.com/travel/2024/02/18/air-canada-airline-chatbot-ruling/).

This article is intended only for educational purposes, showcasing the power of
AI, generative models, and the tools that are developed very quickly.

I understand that this solution may seem overly engineered, and I agree. A
simpler, less expensive solution could address this problem. However, with more
advanced LLMs available, implementing a solution using an LLM can be achieved
with just a few lines of code, allowing the LLM to analyze all the data.

I truly felt this while tackling this challenge:

> Software ate the world. Now AI is eating software.

## I — The problem

I started swimming a couple of weeks ago, and fortunately, Montréal has many
indoor swimming pools. The city's website lists all the indoor pools along with
their availability:
[Indoor swimming pools](https://montreal.ca/lieux?mtl_content.lieux.available_activities.code=ACT0&mtl_content.lieux.installation.code=PISI).

The downside is that you cannot search for an available pool at a specific time,
as each pool has its own schedule, which varies significantly. Some pools have
their schedules embedded as a table on the website, like this one:
[Bain Émard](https://montreal.ca/en/places/bain-emard).

However, for other pools, you have to leave the city website and visit a
[Facebook page](https://www.facebook.com/photo?fbid=410463438816703&set=a.107090795820637)
to see the pool's schedule:
[Complexe Sportif de Saint-Laurent](https://montreal.ca/en/places/pools-complexe-sportif-de-saint-laurent).

Since I didn't have a fixed time to go to the pool, I found myself constantly
navigating through pool websites to find the next available slot, which was
time-consuming and very manual.

## II — Large language models

I decided to use a Large Language Model (LLM) like ChatGPT to address this
problem. LLMs excel at understanding complex text — such as pool schedules — and
grasping concepts related to time and space, like pool opening and closing times,
or pools nearest to a particular address.

One challenge is that pool schedules change frequently, and recent schedules were
not included in the LLMs' training data. So, how can we solve this problem?

Here are three possible solutions:

- **Fine-tune the model using recent data.** Fine-tuning involves updating the
  model's weights by training it with a new dataset. This is effective if you
  have a large, "static" dataset that was not available during the initial
  training of the LLM — by *static*, I mean data that does not change over time.
  However, this approach can be costly and resource-intensive.
- **Provide the entire database alongside the user's query.** This technique
  involves including the entire database with the user's query as a prompt,
  rather than retraining the model. It works well if the dataset is relatively
  small. Current LLMs support a large context window, but if the dataset is too
  large, this approach becomes impractical because the LLM can only process a
  limited portion of the prompt and will only consider the most recent part.
- **Use retrieval-augmented generation.** RAG enhances the capabilities of LLMs
  by integrating them with specific knowledge databases, without the need for
  retraining the model. This approach is cost-effective and helps maintain the
  relevance, accuracy, and usefulness of the LLM's output in various contexts.
  RAG works by first searching through a large database to find relevant
  information related to a query. Then, it uses this information to generate a
  more accurate and informative response.

{{< figure src="01-rag-pipeline-diagram.jpg" alt="Diagram of an advanced RAG pipeline, from documents through indexing and retrieval to the language model" caption="An advanced RAG pipeline. Source: [DeepLearning.AI — Building and Evaluating Advanced RAG](https://learn.deeplearning.ai/courses/building-evaluating-advanced-rag/lesson/2/advanced-rag-pipeline)." >}}

## III — The design and implementation

The pipeline has two halves that run at different times. Everything on the left
happens once, offline, when the schedules are collected. Everything on the right
happens per question:

{{< rawhtml >}}
<svg class="workflow" viewBox="0 0 860 300" role="img"
     aria-label="Workflow diagram. Offline: Montréal pool pages are scraped into one text file per pool, embedded with an embedding model, and stored as vectors. Per query: the user question is embedded with the same model, matched against the stored vectors by semantic search, the retrieved schedules are combined with the question into a prompt, and the LLM answers with a link to the source page.">
  <defs>
    <marker id="wf-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
    </marker>
  </defs>
  <g class="wf-lane">
    <text x="20" y="26" class="wf-lane-label">OFFLINE · ONCE</text>
    <rect x="20" y="40" width="170" height="56" rx="8"/>
    <text x="105" y="63" class="wf-t">Montréal pool pages</text>
    <text x="105" y="82" class="wf-s">HTML tables · Facebook</text>

    <rect x="20" y="126" width="170" height="56" rx="8"/>
    <text x="105" y="149" class="wf-t">One text file per pool</text>
    <text x="105" y="168" class="wf-s">schedule · address · closures</text>

    <rect x="20" y="212" width="170" height="56" rx="8"/>
    <text x="105" y="235" class="wf-t">Embedding model</text>
    <text x="105" y="254" class="wf-s">text → vectors</text>
  </g>

  <rect x="250" y="126" width="150" height="56" rx="8" class="wf-store"/>
  <text x="325" y="149" class="wf-t">Vector store</text>
  <text x="325" y="168" class="wf-s">LlamaIndex</text>

  <g class="wf-lane">
    <text x="460" y="26" class="wf-lane-label">PER QUESTION</text>
    <rect x="460" y="40" width="170" height="56" rx="8"/>
    <text x="545" y="63" class="wf-t">User question</text>
    <text x="545" y="82" class="wf-s">ChainLit chat UI</text>

    <rect x="460" y="126" width="170" height="56" rx="8"/>
    <text x="545" y="149" class="wf-t">Same embedding model</text>
    <text x="545" y="168" class="wf-s">semantic search</text>

    <rect x="460" y="212" width="170" height="56" rx="8"/>
    <text x="545" y="235" class="wf-t">Prompt = context + question</text>
    <text x="545" y="254" class="wf-s">retrieved schedules</text>
  </g>

  <rect x="690" y="212" width="150" height="56" rx="8" class="wf-out"/>
  <text x="765" y="235" class="wf-t">LLM answer</text>
  <text x="765" y="254" class="wf-s">+ link to the source</text>

  <g class="wf-edge" marker-end="url(#wf-arrow)">
    <path d="M105 96 L105 126"/>
    <path d="M105 182 L105 212"/>
    <path d="M190 240 L250 240 L250 182"/>
    <path d="M545 96 L545 126"/>
    <path d="M400 154 L460 154"/>
    <path d="M545 182 L545 212"/>
    <path d="M630 240 L690 240"/>
  </g>
</svg>
{{< /rawhtml >}}

### A. Prepare the dataset

We need to collect data on all the indoor pools. I tried to automate this process
as much as possible, but there is room for improvement to handle more complex
websites.

Using some Python packages, I was able to successfully create a text that
contains the pool schedule for each pool:

{{< figure src="02-pools-dataset.jpg" alt="Directory listing of one text file per Montréal indoor pool" caption="Montréal indoor pools dataset — one file per pool." >}}

To achieve this, we need to extract all tables and relevant information from each
pool's HTML page, such as the pool's address and any exceptional closures.

There are tools that can help automate this process, such as LlamaIndex's web
readers — see
[data connectors](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/)
and the [web reader package](https://llamahub.ai/l/readers/llama-index-readers-web).

Each pool has its own file with a schedule that looks something like this:

{{< figure src="03-pool-schedule-example.jpg" alt="Extracted pool schedule as plain text, with days, times and activity types" caption="Example of a pool schedule after extraction." >}}

### B. Create the embeddings

When a user asks a question about a specific pool, we need to search the database
for relevant information, combine this information — also known as context — with
the user's query, and then use the LLM to generate a response.

To find relevant information in the database, we can use various search methods,
such as semantic search or keyword search.

Semantic search finds data based on the intent and contextual meaning of a query,
rather than an exact match on query words.

So, once the dataset of text files is ready, we need to represent each word or
phrase with a special vector in a high-dimensional vector space, where words with
similar meanings will be close to each other.

[LlamaIndex](https://www.llamaindex.ai/) was used to handle data preprocessing.

{{< figure src="04-embeddings.jpg" alt="Diagram of text being converted into vectors in a high-dimensional embedding space" caption="Text becomes vectors; similar meanings land close together." >}}

To create an embedding, we need an embedding model, which is an LLM used to
convert text into vectors. This same model will later be used to embed the user's
query and search the database. It's important to use the same model for both the
user query and the database embeddings.

### C. Prepare the prompt

With the embeddings ready, we need to obtain the user query, create an embedding
for it, search the database for relevant documents, and prepare the prompt for
the LLM. Tools like [ChainLit](https://docs.chainlit.io/get-started/overview) can
be used to create the chatbot, handling server creation, message history, themes,
parsing, and more.

## IV — Demo

I will not say anything here, and let you see this beauty of an LLM alive:

{{< figure src="05-chatbot-demo.jpg" alt="The chatbot answering a question about which pool is open next, and linking to the pool's page on the city website" caption="ChatGPT used in a RAG system to answer questions about Montréal pools." >}}

## V — The lesson

- As a software developer, I always aim to find exact solutions that are
  deterministic and proven through mathematics, physics, and science. Working
  with LLMs made me uncomfortable because I couldn't fully trust them, even
  though the responses were accurate in my case. There is no guarantee — that I
  am aware of — that the model will consistently perform well and continue to
  provide reliable results. This is why in my demo I provide the URL to the pool
  website as a source.
- Due to the AI boom, there are countless tools available, with many attempting
  to achieve similar objectives. The internet is flooded with numerous tools that
  often overlap in functionality, making it challenging to navigate all the
  technologies. Standards and interfaces are not yet well defined, and code that
  works today may become obsolete in a few months. However, this rapid evolution
  might be a natural part of progress.
- I completed this project in one afternoon, using an LLM as a coding partner to
  create an app that utilizes LLMs to answer questions. :)
- I was occasionally banned from accessing pool websites due to intensive data
  collection for the database. My apologies to Ville de Montréal for the load. :)

## Sources

- Washington Post — [Air Canada must honor refund policy invented by its chatbot](https://www.washingtonpost.com/travel/2024/02/18/air-canada-airline-chatbot-ruling/)
- Ville de Montréal — [indoor swimming pools](https://montreal.ca/lieux?mtl_content.lieux.available_activities.code=ACT0&mtl_content.lieux.installation.code=PISI)
- [LlamaIndex](https://www.llamaindex.ai/) — [data connectors](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/) and the [web reader](https://llamahub.ai/l/readers/llama-index-readers-web) (the original `WebPageDemo` URL has since 404'd)
- [ChainLit](https://docs.chainlit.io/get-started/overview)
- DeepLearning.AI — [Building and Evaluating Advanced RAG](https://learn.deeplearning.ai/courses/building-evaluating-advanced-rag/lesson/2/advanced-rag-pipeline)
