# SPI Framework for Realistic Persona Generation
----
## Overview

This repository contains the code and data for our paper titled "SPI Framework for Realistic Persona Generation using Large Language Models." The SPI framework is a grounded and optimal approach for generating realistic individual personas using large language models (LLMs). Our framework incorporates a comprehensive set of personal attributes, including demographics, personality traits, values, and individualized information, to create well-rounded and believable character profiles.

## Dataset
### Prompts
- `data/prompts/profile_generation_template`: Prompt text file for generating the SPI dataset for fictional characters.
- `data/prompts/eval_template`: System prompt text file for performing TST and Guess Who tasks.
### Profile Generation Results
- `data/profile_result/`: Contains the SPI dataset for the 18 selected fictional characters. File naming convention:
  - `{id}_S.txt`: Demographics
  - `{id}_P_personality.txt`: Personality (BFI-2-S)
  - `{id}_P_value.txt`: Values (PVQ)
  - `{id}_I_behavior.txt`: Individualized information (typical behavior patterns)
  - `{id}_I_lovehate.txt`: Individualized information (preferences)

The table below lists the characters and their corresponding IDs:

| id  | title                   | character              |
|-----|-------------------------|------------------------|
| 0   | Breaking Bad            | Walter White           |
| 1   | Breaking Bad            | Jesse Pinkman          |
| 2   | Breaking Bad            | Hank Schrader          |
| 3   | Friends                 | Phoebe Buffay          |
| 4   | Friends                 | Chandler Bing          |
| 5   | Gossip Girl             | Serena van der Woodsen |
| 6   | Gossip Girl             | Blair Waldorf          |
| 7   | Gossip Girl             | Dan Humphrey           |
| 8   | How I Met Your Mother   | Robin Scherbatsky      |
| 9   | How I Met Your Mother   | Barney Stinson         |
| 10  | Modern Family           | Gloria                 |
| 11  | Modern Family           | Mitchell Pritchett     |
| 12  | Modern Family           | Jay Pritchett          |
| 13  | New Girl                | Schmidt                |
| 14  | New Girl                | Cece Parekh            |
| 15  | New Girl                | Jess Day               |
| 16  | The Big Bang Theory     | Leonard Hofstadter     |
| 17  | The Big Bang Theory     | Sheldon Cooper         |

## Code
- We includes functions for scoring BFI and PVQ, as well as functions utilizing the OpenAI API to output results in JSON format.