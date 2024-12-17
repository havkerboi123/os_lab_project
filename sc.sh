#!/bin/bash

# Read user input
echo "Enter your message: "
read user_input

# Make the API request with user input
response=$(curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d "{
    \"model\": \"gpt-4\",
    \"messages\": [
      {\"role\": \"system\", \"content\": \"You are a helpful assistant.\"},
      {\"role\": \"user\", \"content\": \"$user_input\"}
    ],
    \"max_tokens\": 100
  }")

# Extract only the 'content' from the response using jq
chatbot_response=$(echo "$response" | jq -r '.choices[0].message.content')

# Print the chatbot's response
echo "$chatbot_response"
