{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fa117d49-c46b-475c-aa19-5b90b39950dd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: langchain in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (0.3.27)\n",
      "Requirement already satisfied: langchain-core<1.0.0,>=0.3.72 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from langchain) (0.3.76)\n",
      "Requirement already satisfied: langchain-text-splitters<1.0.0,>=0.3.9 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from langchain) (0.3.11)\n",
      "Requirement already satisfied: langsmith>=0.1.17 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from langchain) (0.4.31)\n",
      "Requirement already satisfied: pydantic<3.0.0,>=2.7.4 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from langchain) (2.11.9)\n",
      "Requirement already satisfied: SQLAlchemy<3,>=1.4 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from langchain) (2.0.43)\n",
      "Requirement already satisfied: requests<3,>=2 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from langchain) (2.32.5)\n",
      "Requirement already satisfied: PyYAML>=5.3 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from langchain) (6.0.2)\n",
      "Requirement already satisfied: tenacity!=8.4.0,<10.0.0,>=8.1.0 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from langchain-core<1.0.0,>=0.3.72->langchain) (9.1.2)\n",
      "Requirement already satisfied: jsonpatch<2.0,>=1.33 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from langchain-core<1.0.0,>=0.3.72->langchain) (1.33)\n",
      "Requirement already satisfied: typing-extensions>=4.7 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from langchain-core<1.0.0,>=0.3.72->langchain) (4.15.0)\n",
      "Requirement already satisfied: packaging>=23.2 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from langchain-core<1.0.0,>=0.3.72->langchain) (25.0)\n",
      "Requirement already satisfied: jsonpointer>=1.9 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from jsonpatch<2.0,>=1.33->langchain-core<1.0.0,>=0.3.72->langchain) (3.0.0)\n",
      "Requirement already satisfied: annotated-types>=0.6.0 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from pydantic<3.0.0,>=2.7.4->langchain) (0.7.0)\n",
      "Requirement already satisfied: pydantic-core==2.33.2 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from pydantic<3.0.0,>=2.7.4->langchain) (2.33.2)\n",
      "Requirement already satisfied: typing-inspection>=0.4.0 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from pydantic<3.0.0,>=2.7.4->langchain) (0.4.1)\n",
      "Requirement already satisfied: charset_normalizer<4,>=2 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from requests<3,>=2->langchain) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from requests<3,>=2->langchain) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from requests<3,>=2->langchain) (2.5.0)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from requests<3,>=2->langchain) (2025.8.3)\n",
      "Requirement already satisfied: greenlet>=1 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from SQLAlchemy<3,>=1.4->langchain) (3.2.4)\n",
      "Requirement already satisfied: httpx<1,>=0.23.0 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from langsmith>=0.1.17->langchain) (0.28.1)\n",
      "Requirement already satisfied: orjson>=3.9.14 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from langsmith>=0.1.17->langchain) (3.11.3)\n",
      "Requirement already satisfied: requests-toolbelt>=1.0.0 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from langsmith>=0.1.17->langchain) (1.0.0)\n",
      "Requirement already satisfied: zstandard>=0.23.0 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from langsmith>=0.1.17->langchain) (0.25.0)\n",
      "Requirement already satisfied: anyio in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from httpx<1,>=0.23.0->langsmith>=0.1.17->langchain) (4.7.0)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from httpx<1,>=0.23.0->langsmith>=0.1.17->langchain) (1.0.9)\n",
      "Requirement already satisfied: h11>=0.16 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from httpcore==1.*->httpx<1,>=0.23.0->langsmith>=0.1.17->langchain) (0.16.0)\n",
      "Requirement already satisfied: sniffio>=1.1 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from anyio->httpx<1,>=0.23.0->langsmith>=0.1.17->langchain) (1.3.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install langchain"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "acc72f9a-61aa-4c2a-b7aa-f7f87eb42679",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: Openai in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (1.108.1)\n",
      "Requirement already satisfied: anyio<5,>=3.5.0 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from Openai) (4.7.0)\n",
      "Requirement already satisfied: distro<2,>=1.7.0 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from Openai) (1.9.0)\n",
      "Requirement already satisfied: httpx<1,>=0.23.0 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from Openai) (0.28.1)\n",
      "Requirement already satisfied: jiter<1,>=0.4.0 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from Openai) (0.11.0)\n",
      "Requirement already satisfied: pydantic<3,>=1.9.0 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from Openai) (2.11.9)\n",
      "Requirement already satisfied: sniffio in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from Openai) (1.3.0)\n",
      "Requirement already satisfied: tqdm>4 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from Openai) (4.67.1)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.11 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from Openai) (4.15.0)\n",
      "Requirement already satisfied: idna>=2.8 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from anyio<5,>=3.5.0->Openai) (3.7)\n",
      "Requirement already satisfied: certifi in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from httpx<1,>=0.23.0->Openai) (2025.8.3)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from httpx<1,>=0.23.0->Openai) (1.0.9)\n",
      "Requirement already satisfied: h11>=0.16 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from httpcore==1.*->httpx<1,>=0.23.0->Openai) (0.16.0)\n",
      "Requirement already satisfied: annotated-types>=0.6.0 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from pydantic<3,>=1.9.0->Openai) (0.7.0)\n",
      "Requirement already satisfied: pydantic-core==2.33.2 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from pydantic<3,>=1.9.0->Openai) (2.33.2)\n",
      "Requirement already satisfied: typing-inspection>=0.4.0 in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from pydantic<3,>=1.9.0->Openai) (0.4.1)\n",
      "Requirement already satisfied: colorama in c:\\users\\dell\\miniconda3\\envs\\env\\lib\\site-packages (from tqdm>4->Openai) (0.4.6)\n"
     ]
    }
   ],
   "source": [
    "!pip install Openai"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "54bddb2b-3779-4e83-ae46-ca0c02d9e2e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "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\n"
     ]
    }
   ],
   "source": [
    "from dotenv import load_dotenv, find_dotenv\n",
    "load_dotenv(find_dotenv(), override=True)\n",
    "import os\n",
    "\n",
    "mykey = os.getenv('OPENAI_API_KEY')\n",
    "print(mykey)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "86cc6784-6f07-4f5a-8ab9-c749b0fac17f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The currency of India is the Indian Rupee, denoted by the symbol \"₹\" and the code \"INR\".\n"
     ]
    }
   ],
   "source": [
    "from langchain.chat_models import ChatOpenAI\n",
    "from langchain.schema import HumanMessage\n",
    "\n",
    "# Initialize the OpenAI model\n",
    "chat = ChatOpenAI(\n",
    "    model=\"gpt-3.5-turbo\",  # Specify the model (e.g., gpt-4, gpt-3.5-turbo)\n",
    "    temperature=0.7,  # Adjust creativity level\n",
    ")\n",
    "\n",
    "# Send a message to the model\n",
    "response = chat([HumanMessage(content=\"What is currency of India\")])\n",
    "\n",
    "# Print the response\n",
    "print(response.content)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b901798-9afd-4afa-8595-c4909d61403c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
