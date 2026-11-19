
import httpx

# Apple's Foundation Models API socket
socket_path = "/tmp/fm.sock"

# Connect through the Unix domain socket
transport = httpx.HTTPTransport(
    uds=socket_path
)

# Create an HTTP client
with httpx.Client(
    transport=transport,
    base_url="http://localhost"
) as client:

    response = client.post(
        "/v1/chat/completions",
        json={
            "model": "system",
            "messages": [
                {
                    "role": "user",
                    "content": "Explain what Artificial Intelligence is in simple English."
                }
            ],
            "stream": False
        }
    )

    response.raise_for_status()

    result = response.json()

    answer = result["choices"][0]["message"]["content"]

    print("\nApple Foundation Model Response:\n")
    print(answer)
