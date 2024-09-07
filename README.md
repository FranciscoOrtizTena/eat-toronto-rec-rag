# Restaurant Suggestion Toronto (RAG)

## Overview

Restaurant Suggestion Toronto (RAG) is a Retrieval-Augmented Generation (RAG) application designed to provide personalized restaurant suggestions in Toronto. By leveraging the Google Places API and advanced AI technologies, this project allows users to interact with a chatbot to get restaurant recommendations based on specific meal preferences, vibes, or cuisines in the Toronto area.

## Problem Description

In a bustling city like Toronto, there are thousands of restaurants offering diverse dining experiences. Whether you're a local or a visitor, it can be overwhelming to find the perfect place to eat that matches your specific tastes and needs. Traditional restaurant discovery tools often flood users with generic options, failing to cater to individual preferences like specific dishes, ambiance, or cuisine types.

### Why is this important?

- **Personalized recommendations**: Current platforms may suggest popular restaurants, but they often lack the granularity required to suggest restaurants based on meal preferences or specific experiences.
- **Efficient decision-making**: Instead of browsing through endless lists of restaurants, users can directly interact with the assistant to receive tailored suggestions that suit their needs.
- **Enhanced dining experience**: The application helps improve the overall dining experience by directing users to places that match their exact expectations, whether it’s a casual brunch spot or a fine dining establishment.

## Data Description

The data used in this project is sourced from the Google Places API. The dataset includes 2000 restaurant records, each containing customer reviews. Each restaurant's reviews have been condensed into one comprehensive summary using the ChatGPT-4o-mini model. The summary focuses on:

- **Dishes**: Highlighting the most popular or signature dishes offered by the restaurant.
- **Vibes**: Summarizing the overall ambiance of the restaurant (e.g., cozy, lively, romantic).
- **Types of meals**: Whether the restaurant specializes in breakfast, lunch, dinner, or other meal types.

The data structure includes the following fields:
- Restaurant name
- Location
- Summarized review
- Cuisine type
- Price range

The dataset is located in the `data` folder under `clean_data.csv`.

## Functionality

The core functionality of the Restaurant Suggestion Toronto (RAG) application revolves around a conversational assistant that users can interact with to receive restaurant recommendations. The assistant leverages the dataset mentioned above to provide relevant suggestions based on user queries.

### Key Features

- Restaurant recommendations based on specific dishes: Users can search for restaurants offering a particular dish (e.g., "Where can I find the best sushi?").
- Vibe-based suggestions: Users can search for restaurants with a particular ambiance (e.g., "Suggest a cozy place for dinner.").
- Cuisine-specific recommendations: Users can look for restaurants offering a certain type of cuisine (e.g., "Find an Italian restaurant near me.").
- Meal type filtering: Users can refine their search based on meal type (e.g., "Show me breakfast spots.").

### How it works

1. User query: Users input their preferences (e.g., dish name, vibe, cuisine type) into the chatbot interface.
2. Retrieval process: The system searches through the summarized reviews and data to find matching restaurants based on the query.
3. Response generation: The chatbot generates a personalized recommendation, complete with a brief description of the restaurant, its location, key dishes, and the overall vibe.

## Running it

We use pipenv for managing dependencies and Python 3.12

Make sure you have pipenv installed:

```bash
pip install pipenv
```

Installing the dependencies:

```bash
pipenv install
````

Running Jupyter notebook for experiments:

```bash
cd notebooks
pipenv run jupyter notebooks
```

## Ingestion

## Evaluation

For the code for evaluating the system, you can check the [notebooks/rag-test.ipynb](notebooks/rag-test.ipynb) notebook.

### Retrieval

The basic approach - using minsearch without any boosting - gave the following metrics:

- hit_rate: `58%`
- MRR: `45%`

The current system's hit rate of 58% and MRR of 45% can be attributed to the challenge of retrieving relevant results from a dataset of 2,000 restaurant records. Due to the size of the dataset, the retrieval model must efficiently sift through a large volume of information, increasing the likelihood of lower accuracy in matching the user's specific request. Furthermore, the complexity of the queries, which often involve preferences for specific meals, vibes, or cuisines, adds another layer of difficulty in pinpointing the optimal suggestion. As a result, the retrieval process can yield suboptimal matches, affecting both the hit rate and the MRR. Improving the precision of the search and ranking algorithm is essential to enhance the overall performance of the system.

The improved version (with better boosting)

- hit_rate: `71%`
- MRR: `54%`

The best boosting parameters:

```python
boost = {
    'displayname': 1.07,
    'primarytype': 0.14,
    'editorialsummary': 1.25,
    'reviews': 2.79
}
```

### RAG flow

We used the LLM-as-a-Judge metric to evaluate the quality of our RAG flow

For `gpt-4o-mini`, among 200 records, we had:

- 100 % Relevant
- 0 % Partly_revelant
- 0 % Irrelevant

We also tested `gpt-4o`

- 100 % Relevant
- 0 % Partly_revelant
- 0 % Irrelevant

We opted for using `gpt-4o-mini`.

## Monitoring

## Containerization