# SPeCtrum: A Grounded Framework for Multidimensional Identity Representation in LLM-Based Agent
----
## Overview

This repository contains the code and data for our paper titled **"SPeCtrum: A Grounded Framework for Multidimensional Identity Representation in LLM-Based Agent"**. The SPeCtrum framework is a grounded and optimal approach for generating realistic individual personas using large language models (LLMs). Our framework incorporates a comprehensive set of personal attributes, including demographics, personality traits, values, and personal life context, to create well-rounded and believable character profiles.

## Dataset
### Prompts
- `data/prompts/profile_generation_template`: Prompt text file for generating the SPC dataset for fictional characters.
- `data/prompts/eval_template`: System prompt text file for performing TST and Guess Who tasks.
### Profile Generation Results
- `data/profile_result/`: Contains the SPC dataset for the 18 selected fictional characters. File naming convention:
  - `{id}_S.txt`: Demographics
  - `{id}_P_personality.txt`: Personality (BFI-2-S)
  - `{id}_P_value.txt`: Values (PVQ)
  - `{id}_C_behavior.txt`: Personal Life Context (typical behavior patterns)
  - `{id}_C_lovehate.txt`: Personal Life Context (preferences)

The table below lists the characters and their corresponding IDs:

| ID | TV Show | Character Name |
|-------|---------|----------------|
| 0 | The Big Bang Theory | Leonard Hofstadter |
| 1 | The Big Bang Theory | Sheldon Cooper |
| 2 | The Big Bang Theory | Penny |
| 3 | The Big Bang Theory | Howard Wolowitz |
| 4 | The Big Bang Theory | Raj Koothrappali |
| 5 | The Big Bang Theory | Bernadette Rostenkowski |
| 6 | The Big Bang Theory | Amy Farrah Fowler |
| 7 | Gossip Girl | Serena van der Woodsen |
| 8 | Gossip Girl | Dan Humphrey |
| 9 | Gossip Girl | Blair Waldorf |
| 10 | Gossip Girl | Chuck Bass |
| 11 | Gossip Girl | Nate Archibald |
| 12 | Gossip Girl | Lily van der Woodsen |
| 13 | Gossip Girl | Rufus Humphrey |
| 14 | Gossip Girl | Jenny Humphrey |
| 15 | Gossip Girl | Vanessa Abrams |
| 16 | Gossip Girl | Dorota Kishlovsky |
| 17 | Friends | Phoebe Buffay |
| 18 | Friends | Chandler Bing |
| 19 | Friends | Rachel Green |
| 20 | Friends | Monica Geller |
| 21 | Friends | Joey Tribbiani |
| 22 | Friends | Ross Geller |
| 23 | Friends | Gunther |
| 24 | How I Met Your Mother | Ted Mosby |
| 25 | How I Met Your Mother | Marshsall Eriksen |
| 26 | How I Met Your Mother | Robin Scherbatsky |
| 27 | How I Met Your Mother | Barney Stinson |
| 28 | How I Met Your Mother | Lily Aldrin |
| 29 | Modern Family | Jay Pritchett |
| 30 | Modern Family | Gloria Delgado-Pritchett |
| 31 | Modern Family | Claire Dunphy |
| 32 | Modern Family | Phil Dunphy |
| 33 | Modern Family | Mitchell Pritchett |
| 34 | Modern Family | Cameron Tucker |
| 35 | Modern Family | Manny Delgado |
| 36 | Modern Family | Luke Dunphy |
| 37 | Modern Family | Haley Dunphy |
| 38 | Modern Family | Alex Dunphy |
| 39 | Modern Family | Lily Tucker-Pritchett |
| 40 | New Girl | Jess Day |
| 41 | New Girl | Nick Miller |
| 42 | New Girl | Schmidt |
| 43 | New Girl | Cece Parekh |
| 44 | New Girl | Winston Bishop |

## Code
- We includes functions for scoring BFI and PVQ, as well as functions utilizing the OpenAI API to output results in JSON format.