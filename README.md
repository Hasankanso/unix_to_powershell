# HOW TO GET AN API TOKEN

go to `https://platform.openai.com/api-keys`, login/register, and open your profile. From there you can inspect your keys and generate new ones. You have to activate payment before you can use the keys.<br>
When you generate a token, export it in your terminal:<br>
Windows:<br>
`$env:OPENAI_API_KEY = "<token>"`<br>
Linux:<br>
`export OPENAI_API_KEY="<token>"`

# CAUTION
Chatgpt generates inconsistent responses, I recommend to use `--dry-run` flag to inspect the powershell command beforehand.
# INSTALLATION
```
pip install -r requirements.txt
```
# USAGE
command:
```
python b.py echo "hello world"
```
output:
```
Write-Output "hello world"
hello world
```
command:
```
python b.py -v whereis argocd
```
output:
```
Get-Command argocd << command name in powershell

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Application     argocd.exe                                         0.0.0.0    C:\Users\Hassa\bin\argocd.exe
```
# ARGS

`--dry-run` : to check the chatgpt output without executing it on your system.<br>
`-v` or `--verbose` : to print extra information.
