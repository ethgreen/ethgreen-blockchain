# $env:path should contain a path to editbin.exe and signtool.exe

$ErrorActionPreference = "Stop"

git status

Write-Output "   ---"
Write-Output "Setup npm packager"
Write-Output "   ---"
Set-Location -Path ".\npm_windows" -PassThru
npm install
$Env:Path = $(npm bin) + ";" + $Env:Path

Set-Location -Path "..\..\" -PassThru
git submodule update --init ethgreen-blockchain-gui

Set-Location -Path ".\ethgreen-blockchain-gui" -PassThru

Write-Output "   ---"
Write-Output "Build GUI npm modules"
Write-Output "   ---"
$Env:NODE_OPTIONS = "--max-old-space-size=3000"

Write-Output "lerna clean -y"
lerna clean -y
Write-Output "npm install"
npm install
# Audit fix does not currently work with Lerna. See https://github.com/lerna/lerna/issues/1663
# npm audit fix

git status

Write-Output "npm run build"
npm run build
If ($LastExitCode -gt 0){
    Throw "npm run build failed!"
}

# Remove unused packages
Remove-Item node_modules -Recurse -Force

# Other than `ethgreen-blockchain-gui/package/gui`, all other packages are no longer necessary after build.
# Since these unused packages make cache unnecessarily fat, unused packages should be removed.
Write-Output "Remove unused @ethgreen packages to make cache slim"
Remove-Item packages\api -Recurse -Force
Remove-Item packages\api-react -Recurse -Force
Remove-Item packages\core -Recurse -Force
Remove-Item packages\icons -Recurse -Force
Remove-Item packages\wallets -Recurse -Force

# Remove unused fat npm modules from the gui package
Set-Location -Path ".\packages\gui\node_modules" -PassThru
Write-Output "Remove unused node_modules in the gui package to make cache slim more"
Remove-Item electron\dist -Recurse -Force # ~186MB
Remove-Item "@mui" -Recurse -Force # ~71MB
Remove-Item typescript -Recurse -Force # ~63MB

# Remove `packages/gui/node_modules/@ethgreen` because it causes an error on later `electron-packager` command
Remove-Item "@ethgreen" -Recurse -Force
