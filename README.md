# 🧠 Building with OpenAI Assistants API

> ⚠️ **Note**: The Assistants API used in this project is **deprecated**. This project was created as a learning exercise to understand how the Assistants API works before transitioning to the new [OpenAI Responses API](https://platform.openai.com/docs/guides/responses).

This project is a hands-on demonstration of how to create and interact with an AI Assistant using the (now deprecated) OpenAI Assistants API. It covers the basic workflow of creating an assistant, managing threads, and retrieving intelligent responses — including function calling, custom instructions, and conversational memory.

---

## 📌 What This Project Does

This script:
- Initializes the OpenAI client with API credentials
- Uses a **pre-created Assistant and Thread** (IDs are hardcoded)
- Sends a **user message** to the thread
- Executes a **run** with custom instructions (e.g., "Address the user as James Bond")
- Polls the status until the run is complete
- Retrieves and prints the final assistant response

---

## 🔧 Technologies Used

- Python 3.8+
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- `dotenv` for environment management
- Logging and time tracking

---

## 📂 Project Structure

```
building_with_open_ai_assistants_api/
├── main.py        # Main script for interacting with the Assistant API
├── .env           # Stores your OpenAI API key
├── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mathncode-sid/building_with_open_ai_assistants_api.git
cd building_with_open_ai_assistants_api
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Environment Variables

Create a `.env` file and insert your OpenAI API key:

```env
OPEN_API_KEY=your_openai_key_here
```

> **Note**: Make sure to use a valid API key with access to GPT-4 and the Assistants API (or the new Responses API if migrating).

---

## ▶️ How to Run the Script

```bash
python main.py
```

Expected behavior:
- Sends a predefined message to an existing thread
- Executes the assistant run
- Waits for completion
- Prints the assistant’s final response

---

## ✅ Example Output

```bash
Run completed in 00:00:08
Assistant Response: The best exercises to build lean muscle and strength include compound movements such as squats, deadlifts, bench presses, pull-ups, and rows...
```

---

## 🧠 Key Concepts Demonstrated

- **Threading**: Maintaining conversation context
- **Custom Instructions**: Personalizing responses (e.g., “Address the user as James Bond”)
- **Polling Runs**: Monitoring run completion and handling errors
- **Deprecation Handling**: Ignoring deprecation warnings for a cleaner output

---

## 📌 To-Do:

- [ ] Migrate to the new **Responses API**
- [ ] Dynamically create new assistants/threads
- [ ] Store and load assistant/thread IDs from a file or DB
- [ ] Add support for uploading files to threads
- [ ] Implement function calling tools

---

## 📄 License

This project is open-source and licensed under the [MIT License](LICENSE).

---

**Built by [Sidney Baraka](https://github.com/mathncode-sid)** 🛠️
