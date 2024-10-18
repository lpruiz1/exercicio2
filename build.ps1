$exclude = @("venv", "bot_produto_POO.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_produto_POO.zip" -Force