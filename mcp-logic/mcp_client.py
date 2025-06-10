######## DEPRECATED ########

# import os
# import requests
# from langchain_community.vectorstores import FAISS
# from langchain_community.embeddings import OpenAIEmbeddings
# from langchain.text_splitter import CharacterTextSplitter
# from langchain_community.llms import OpenAI
# from langchain.chains import RetrievalQA
# from crewai.tools.mcp_tool import MCPTool

# class MCPClient:
#     def call(self, service, action, params):
#         if service == "discovery" and action == "web_activity_rag":
#             return self._web_activity_rag(params)
#         raise NotImplementedError()

#     def _web_activity_rag(self, params):
#         query = params["query"]
#         tavily_key = os.getenv("TAVILY_API_KEY")

#         # Tavily API call
#         response = requests.post(
#             "https://api.tavily.com/search",
#             headers={"Authorization": f"Bearer {tavily_key}"},
#             json={"query": query, "num_results": 5}
#         )

#         data = response.json()
#         snippets = [item["content"] for item in data["results"]]

#         # Chunk & embed
#         splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
#         documents = splitter.create_documents(snippets)

#         vectorstore = FAISS.from_documents(documents, OpenAIEmbeddings())
#         retriever = vectorstore.as_retriever()

#         # Run RAG query
#         qa = RetrievalQA.from_chain_type(
#             llm=OpenAI(),
#             retriever=retriever,
#             return_source_documents=False
#         )
#         answer = qa.run("Summarize the most interesting activities in the desired location.")
#         return answer