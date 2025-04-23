Maciej, [22.04.2025 20:30]
param (
    [string]$FilePath = "telegram_bot.py"
)

$Token = "7600816191:AAHglqWYgD2aVfiCba6m6m6qS3_aG-prlXQ"
$ChatID = "6673294456"
$Url = "https://api.telegram.org/bot$Token/sendDocument"

Write-Host "Wysyłam plik: $FilePath na Telegram..."

if (Test-Path $FilePath) {
    $Boundary = [System.Guid]::NewGuid().ToString()
    $LF = "rn"
    $BodyLines = (
        "--$Boundary",
        "Content-Disposition: form-data; name="chat_id"$LF",
        $ChatID,
        "--$Boundary",
        "Content-Disposition: form-data; name=`

Maciej, [22.04.2025 20:32]
param (
    [string]$FilePath = "telegram_bot.py"
)

$Token = "7600816191:AAHglqWYgD2aVfiCba6m6m6qS3_aG-prlXQ"
$ChatID = "6673294456"
$Url = "https://api.telegram.org/bot$Token/sendDocument"

Write-Host "Wysyłam plik: $FilePath na Telegram..."

if (Test-Path $FilePath) {
    $Form = @{
        chat_id = $ChatID
        document = Get-Item $FilePath
    }
    Invoke-WebRequest -Uri $Url -Method Post -Form $Form | Out-Null
    Write-Host "Plik został wysłany!"
} else {
    Write-Host "Błąd: Plik '$FilePath' nie istnieje!"
}