!include "nsDialogs.nsh"

; Add our customizations to the finish page
!macro customFinishPage
XPStyle on

Var DetectDlg
Var FinishDlg
Var ETHgreenSquirrelInstallLocation
Var ETHgreenSquirrelInstallVersion
Var ETHgreenSquirrelUninstaller
Var CheckboxUninstall
Var UninstallETHgreenSquirrelInstall
Var BackButton
Var NextButton

Page custom detectOldETHgreenVersion detectOldETHgreenVersionPageLeave
Page custom finish finishLeave

; Add a page offering to uninstall an older build installed into the ethgreen-blockchain dir
Function detectOldETHgreenVersion
  ; Check the registry for old ethgreen-blockchain installer keys
  ReadRegStr $ETHgreenSquirrelInstallLocation HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\ethgreen-blockchain" "InstallLocation"
  ReadRegStr $ETHgreenSquirrelInstallVersion HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\ethgreen-blockchain" "DisplayVersion"
  ReadRegStr $ETHgreenSquirrelUninstaller HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\ethgreen-blockchain" "QuietUninstallString"

  StrCpy $UninstallETHgreenSquirrelInstall ${BST_UNCHECKED} ; Initialize to unchecked so that a silent install skips uninstalling

  ; If registry keys aren't found, skip (Abort) this page and move forward
  ${If} ETHgreenSquirrelInstallVersion == error
  ${OrIf} ETHgreenSquirrelInstallLocation == error
  ${OrIf} $ETHgreenSquirrelUninstaller == error
  ${OrIf} $ETHgreenSquirrelInstallVersion == ""
  ${OrIf} $ETHgreenSquirrelInstallLocation == ""
  ${OrIf} $ETHgreenSquirrelUninstaller == ""
  ${OrIf} ${Silent}
    Abort
  ${EndIf}

  ; Check the uninstall checkbox by default
  StrCpy $UninstallETHgreenSquirrelInstall ${BST_CHECKED}

  ; Magic create dialog incantation
  nsDialogs::Create 1018
  Pop $DetectDlg

  ${If} $DetectDlg == error
    Abort
  ${EndIf}

  !insertmacro MUI_HEADER_TEXT "Uninstall Old Version" "Would you like to uninstall the old version of ETHgreen Blockchain?"

  ${NSD_CreateLabel} 0 35 100% 12u "Found ETHgreen Blockchain $ETHgreenSquirrelInstallVersion installed in an old location:"
  ${NSD_CreateLabel} 12 57 100% 12u "$ETHgreenSquirrelInstallLocation"

  ${NSD_CreateCheckBox} 12 81 100% 12u "Uninstall ETHgreen Blockchain $ETHgreenSquirrelInstallVersion"
  Pop $CheckboxUninstall
  ${NSD_SetState} $CheckboxUninstall $UninstallETHgreenSquirrelInstall
  ${NSD_OnClick} $CheckboxUninstall SetUninstall

  nsDialogs::Show

FunctionEnd

Function SetUninstall
  ; Set UninstallETHgreenSquirrelInstall accordingly
  ${NSD_GetState} $CheckboxUninstall $UninstallETHgreenSquirrelInstall
FunctionEnd

Function detectOldETHgreenVersionPageLeave
  ${If} $UninstallETHgreenSquirrelInstall == 1
    ; This could be improved... Experiments with adding an indeterminate progress bar (PBM_SETMARQUEE)
    ; were unsatisfactory.
    ExecWait $ETHgreenSquirrelUninstaller ; Blocks until complete (doesn't take long though)
  ${EndIf}
FunctionEnd

Function finish

  ; Magic create dialog incantation
  nsDialogs::Create 1018
  Pop $FinishDlg

  ${If} $FinishDlg == error
    Abort
  ${EndIf}

  GetDlgItem $NextButton $HWNDPARENT 1 ; 1 = Next button
  GetDlgItem $BackButton $HWNDPARENT 3 ; 3 = Back button

  ${NSD_CreateLabel} 0 35 100% 12u "ETHgreen has been installed successfully!"
  EnableWindow $BackButton 0 ; Disable the Back button
  SendMessage $NextButton ${WM_SETTEXT} 0 "STR:Let's Farm!" ; Button title is "Close" by default. Update it here.

  nsDialogs::Show

FunctionEnd

; Copied from electron-builder NSIS templates
Function StartApp
  ${if} ${isUpdated}
    StrCpy $1 "--updated"
  ${else}
    StrCpy $1 ""
  ${endif}
  ${StdUtils.ExecShellAsUser} $0 "$launchLink" "open" "$1"
FunctionEnd

Function finishLeave
  ; Launch the app at exit
  Call StartApp
FunctionEnd

; Section
; SectionEnd
!macroend
