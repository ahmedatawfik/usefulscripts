import openai

# This is a dummy key, replace with your actual OpenAI API key
openai.api_key = "9i-wmcxtsO-VuDJlPsbRlR9sqWfdLphxFEedbFIyw3MFHlcbtcTapxj6v4CfwmEtarZQWJ0ieEJXSCBHOEM5LP6m-Kd1KVfvuOKPBP8MAeVlvXQsudk8"

# Function to read the prompt from prompt.txt
def read_prompt_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        prompt = file.read()
    return prompt

# Function to write the response to response.txt
def write_response_to_file(file_path, response):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(response)

# Function to get response from ChatGPT
def get_chatgpt_response(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who provides cool answers!"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Main function to read, get response, and write
def main():
    prompt = read_prompt_from_file(r"/home/user/prompt.txt")
    response = get_chatgpt_response(prompt)
    write_response_to_file(r"/home/user/response.txt", response)
    print("Response has been written to response.txt")

if __name__ == "__main__":
    main()
