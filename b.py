import os
import openai
import sys
import subprocess
import argparse

parser = argparse.ArgumentParser(description="Translate unix commands to powershell commands")

parser.add_argument('-v', '--verbose', action="store_true",
                    default=False,
                    help='print verbose information')
parser.add_argument('--dry-run', action='store_true',
                    default=False,
                    help='print powershell command without executing it')
parser.add_argument('command', type=str, nargs='+',
                    help='command to translate')

args = parser.parse_args()


command = " ".join(args.command)
dry_run = args.dry_run
verbose = args.verbose

if verbose:
  print("args:", args)
  print("input:", command)

client = openai.OpenAI(api_key=os.environ['OPENAI_API_KEY'])
response = client.chat.completions.create(model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "you translate unix commands to the equivalent in powershell. you only provide the command without any additional texts.\n\nIf the user input is not a valid or unknown unix command, you return \"error\" with suggestions"
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

if not dry_run and "error" not in powershell_command:
  result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True)
  print(result.stdout.decode("utf-8"))