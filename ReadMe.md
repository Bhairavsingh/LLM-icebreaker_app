<a name="readme-top"></a>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

This project is dedicated for Ice Breaker application. This application uses LLMs and Proxycurl API for fetching the
LinkedIn data about a persona and provides icebreaker conversation information.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

Following major frameworks/libraries are used in this project.

*   Python (3.11)
*   LangChain
*   HuggingFace
*   ProxyCurl API
*   Tavily API
*   OpenAI -- GPT 3.5 Turbo

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

TODO

### Installation

Following steps are required for running the project scripts locally.

1. Get a OpenAI API Token Key at [https://platform.openai.com/](https://platform.openai.com/)
2. Get a PROXYCURL API Token Key at [https://nubela.co/proxycurl/](https://nubela.co/proxycurl/)
3. Get a TAVILY API Token Key at [https://tavily.com](https://tavily.com)
3. Set the tokens as following as ENVIRONMENT VARIABLE
   ```
   OPENAI_API_KEY={YOUR_API_TOKEN}
   PROXYCURL_API_KEY={YOUR_API_TOKEN}
   TAVILY_API_KEY={YOUR_API_TOKEN}
   ```
3. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Run the UI application using following command
   ```sh
   python run app.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Exploring LangChain framework
- [ ] Explore different pre-trained text generative models
    - [x] GPT-3.5 Turbo
    - [ ] GPT-4
    - [ ] Llama 3
    - [ ] Gemini


<p align="right">(<a href="#readme-top">back to top</a>)</p>