from openai import OpenAI
import os
from dotenv import load_dotenv
from datetime import datetime
import time
import logging
load_dotenv()

client = OpenAI(api_key=os.environ.get("OPEN_API_KEY"))
model = "gpt-3.5-turbo-16k"

# # === Create Assistant ===
# personal_trainer_assis = client.beta.assistants.create(
#     name="Personal Trainer",
#     instructions="""You're the best personal trainer and nutritionist who helps clients build lean muscles.
#     You've trained high-caliber athletes and movie stars.""",
#     model=model
# )

# #  Print the whole assistant object to debug
# print("Assistant Object:", personal_trainer_assis)

# # Now safely extract and print the assistant ID
# assistant_id = personal_trainer_assis.id
# print("Assistant ID:", assistant_id)

# # === Create Thread ===
# thread = client.beta.threads.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "How do I get started working out to lose fat and build muscle?"
#         }
#     ]
# )

# print("Thread ID:", thread.id)

#=== Hardcode our ids ===
assistant_id = "asst_BLfaLW8ikpeHKVcfmrBcKCMi"
thread_id = "thread_Hr6ZwH3qZzk8d9zSpcz8XFSE"

# === Create a Message ===
message = "What are the best exercises for lean muscles and getting strong?"
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content=message
)

#=== Run our assistant ===
run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
    instructions="Please address the user as James Bond"
)

def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5):
    """
    Waits for a run to complete and prints the elapsed time.
    :param client: OpenAI client instance
    :param thread_id = The ID of the thread
    :param run_id = The ID of the run
    :param sleep_interval: Time in seconds to wait between checks.
    """

    while True:
        try:
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            if run.completed_at:
                elapsed_time = run.completed_at - run.created_at
                formatted_elapsed_time = time.strftime(
                    "%H:%M:%S", time.gmtime(elapsed_time)
                )
                print(f"Run completed in {formatted_elapsed_time}")
                logging.info(f"RUn completed in {formatted_elapsed_time}")
                #Get messages once Run is complete
                messages = client.beta.threads.messages.list(thread_id=thread_id)
                last_message = messages.data[0]
                response = last_message.content[0].text.value
                print(f"Assistant Response: {response}")
                break
        except Exception as e:
                logging.error(f"An error occurred whule retrieving the run {e}")
                break
        logging.info("Waiting for run to complete...")
        time.sleep(sleep_interval)

# === Run ===
wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id)

        