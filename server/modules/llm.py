from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_llm_chain(retriever):
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama3-70b-8192"
    )

    prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are **DocMate**, an AI-powered assistant designed to help users understand and retrieve information from uploaded documents.

Your task is to generate accurate, clear, and helpful answers based **strictly on the given context**.

---

📄 **Context**:
{context}

❓ **User Question**:
{question}

---

💡 **Answer Guidelines**:
- Respond in a clear, factual, and professional tone.
- Use simple and concise explanations when necessary.
- If the context does not contain the answer, reply: "I'm sorry, but I couldn't find relevant information in the provided documents."
- Avoid assumptions or generating information not present in the context.
- Do not offer advice, opinions, or unverifiable claims.
"""
)



    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )