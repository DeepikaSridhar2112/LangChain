def generate_response(age,task_type,user_query):
    examples = [
    {
       "query": "What is a mobile" ,
       "answer":"Its a magical device which lets us see people"
    },
    {
        "query":"What happens when you get sick",
        "answer":"I love to sleep and drink my tonic"
    },
    {
        "query":"Do you like your mom or dad",
        "answer":"I love my mom like sun and dad like moon"
    },
    {
        "query":"What do you want to become",
        "answer":"I want to become an icecream man"
     }
    ]

    sample_template="""
     Question: {query},
     Response: {answer}
    """

    example_prompt = PromptTemplate(
     input_variables=["query","answer"],
     template=sample_template)

    prefix= """You are a {template_age} and {template_task_type}
        Here are some examples:
    """

    suffix = """
    Question: {userInput}
    Response:"""
    example_selector = LengthBasedExampleSelector(
        examples=examples,
        example_prompt=example_prompt,
        max_length=200)
    prompt_template= FewShotPromptTemplate(
        example_selector = example_selector,
        example_prompt= example_prompt,
        prefix = prefix,
        suffix= suffix,
        input_variables=["userInput","template_age","template_task_type"],
        example_separator="\n")
    query= form_input
    human_message_prompt = HumanMessagePromptTemplate(prompt= prompt_template)
    chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt])

    prompt = chat_prompt.format_prompt(userInput=user_query,template_age=age,template_task_type=task_type)
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)

    messages = prompt.to_messages()
    for message in messages:
        print(message.content)


    output= llm.invoke(prompt)
    print(output.content)
