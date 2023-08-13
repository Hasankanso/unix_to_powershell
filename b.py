import os
import openai
import sys
import subprocess

openai.api_key = os.getenv("OPENAI_API_KEY")

command = None
dry_run = False
debug = False
if (len(sys.argv) > 1):
  for i in range(1, len(sys.argv)):
    if (sys.argv[i] == "--dry-run"):
      dry_run = True
      continue
    if (sys.argv[i] == "--debug"):
      debug = True
      continue
    elif (command is None):
      command = sys.argv[i]
    else:
      command = command + " " + sys.argv[i]
else:
  raise Exception("Please provide a command")

if debug:
  print("input:", command)

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "you translate unix commands to the equivalent in powershell. you only provide the command without any additional texts.\n\nIf the user input is not a valid or unknown unix command, you return \"error\""
    },
    {
      "role": "user",
      "content": command
    },
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

powershell_command = response.choices[0].message.content
print(powershell_command)

if not dry_run:
  result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True)
  print(result.stdout.decode("utf-8"))