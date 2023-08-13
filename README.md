# HOW TO GET AN API TOKEN

go to `https://platform.openai.com/`, login/register, and open your profile. From there you can inspect your keys and generate new ones. You have to activate payment before you can use the keys.<br>
When you generate a token, export it in your terminal:<br>
Windows:<br>
`$env:OPENAI_API_KEY = "<token>"`<br>
Linux:<br>
`export OPENAI_API_KEY="<token>"`

# CAUTION
Chatgpt generates inconsistent responses, I recommend to `--dry-run` and then execute the generated command manually.
# EXMAPLE
```
b.py echo "hello world"

output:
Write-Output "hello world"
hello world
```

# ARGS

`--dry-run` : to check the chatgpt output without executing it on your system.<br>
`--debug` : to print extra information.
