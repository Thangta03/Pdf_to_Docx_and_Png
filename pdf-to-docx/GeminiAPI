# Import libraries
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Fetch API key from environment variable
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Config
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(
    'Tell me a story about a magic backpack.',
    generation_config=genai.types.GenerationConfig(
        # Only one candidate for now.
        candidate_count=1,
        stop_sequences=['x'],
        max_output_tokens=20,
        temperature=1.0)
)

#max tokens

#embedding text 
result = genai.embed_content(
    model="models/embedding-001",
    content="What is the meaning of life?",
    task_type="retrieval_document",
    title="Embedding of single string")

# 1 input > 1 vector output
print(str(result['embedding'])[:50], '... TRIMMED]')

result = genai.embed_content(
    model="models/embedding-001",
    content=[
      'What is the meaning of life?',
      'How much wood would a woodchuck chuck?',
      'How does the brain work?'],
    task_type="retrieval_document",
    title="Embedding of list of strings")

# A list of inputs > A list of vectors output
for v in result['embedding']:
  print(str(v)[:50], '... TRIMMED ...') 

# While the genai.embed_content function accepts simple strings or lists of strings, it is actually built around the glm.Content type (like GenerativeModel.generate_content). glm.Content objects are the primary units of conversation in the API.

# While the glm.Content object is multimodal, the embed_content method only supports text embeddings. This design gives the API the possibility to expand to multimodal embeddings.

response.candidates[0].content

result = genai.embed_content(
    model='models/embedding-001',
    content=response.candidates[0].content)

# 1 input > 1 vector output

chat.history
print(str(result['embedding'])[:50], '... TRIMMED ...')
