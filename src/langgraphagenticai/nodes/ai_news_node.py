from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate


class AINewsNode:
    def __init__(self, llm):
        """
            Initialize the AINewsNode with API Keys for Tavily and OpenAI.
        """
        self.tavily = TavilyClient()
        self.llm = llm

        # this is used to capture various steps in this file so that later can be use for steps shown.
        self.state = {}

    
    def fetch_news(self, state: dict) -> dict:
        """
            Fetch AI News based on the specified frequency.

            Args:
                state (dict): The state dictionary containing 'frequency'.

            Returns: 
                dict: updated states with 'news_data' key containing fetched news.
        """

        frequency = state['messages'][0].content.lower()
        self.state['frequency'] = frequency
        time_range_map = {'daily': 'd', 'weekly': 'w', 'monthly': 'm', 'yearly': 'y'}
        days_map = {'daily': 1, 'weekly': 7, 'monthly': 30, 'yearly': 365}

        response = self.tavily.search(
            query="Top Artificial Intelligence (AI) technology news India and globally",
            topic="news",
            time_range=time_range_map[frequency],
            include_answer='advanced',
            max_results=20,
            days=days_map[frequency]
        )

        state['news_data'] = response.get('results', [])
        self.state['news_data'] = state['news_data']
        return state
    

    def summarize_news(self, state: dict) -> dict:
        """
            Summarize the feteched news using an LLM.

            Args:
                state (dict): The state dictionary containing 'news_data'.

            Returns:
                state (dict): updated states with 'summary' key containing summarized news.
        """

        news_items = self.state['news_data']

        prompt_template = ChatPromptTemplate.from_messages([
            (
                'system', """
                    Summarize AI news artical into markdown format. For each item include:
                        - Date in YYYY-MM-DD format in IST Timezone
                        - Concise sentences summary from latest news
                        - sort news by date wise (latest first)
                        - source url as link
                        use format:
                        ### [Date]
                            [Summary]
                            [URL]
                """
            ),
            ("user", "Articles: \n{articles}")
        ])

        articles_str = "\n\n".join([
            f"Content: {item.get('content', '')}\nURL: {item.get('url', '')}\nDate: {item.get('published_date', '')}" for item in news_items
        ])

        response = self.llm.invoke(prompt_template.format(articles=articles_str))

        state['summary'] = response.content
        self.state['summary'] = state['summary']
        return self.state

    def save_result(self, state):
        frequency = self.state['frequency']
        summary = self.state['summary']

        filename = f"./AINews/{frequency}_summary.md"
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(f'# {frequency.capitalize()} AI News Summary\n\n')
            f.write(summary)
        
        self.state['filename'] = filename

        return self.state

