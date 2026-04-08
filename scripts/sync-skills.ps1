<#
.SYNOPSIS
    Sync Skills to OneDrive archive
.DESCRIPTION
    One-click sync all skill repos to OneDrive backup.
    Copies skill directories (excluding .git) to the archive folder.
.USAGE
    # Sync all skills:
    .\sync-skills.ps1

    # Sync a specific skill:
    .\sync-skills.ps1 -Name power-automate-dev-skills

    # Add a new skill source:
    .\sync-skills.ps1 -Add -Name my-new-skill -Path "C:\path\to\skill"
#>

param(
    [string]$Name,
    [switch]$Add,
    [string]$Path
)

# === Configuration ===
$ArchiveRoot = "C:\Users\v-lexinhuang\OneDrive - Microsoft\The Garage - Beijing, Greater China-GCR Garage Staff - Lab Manager\CLI file\2.Sklls"
$ConfigFile = Join-Path $PSScriptRoot "skills-registry.json"

# === Initialize registry ===
if (Test-Path $ConfigFile) {
    $registry = Get-Content $ConfigFile -Raw | ConvertFrom-Json
} else {
    $registry = @{
        skills = @(
            @{ name = "power-automate-dev-skills"; path = "C:\Users\v-lexinhuang\power-automate-dev-skills" }
        )
    }
    $registry | ConvertTo-Json -Depth 3 | Set-Content $ConfigFile -Encoding utf8
    Write-Host "[INIT] Created registry: $ConfigFile" -ForegroundColor Cyan
}

# === Add new skill ===
if ($Add) {
    if (-not $Name -or -not $Path) {
        Write-Host "[ERROR] Usage: .\sync-skills.ps1 -Add -Name <name> -Path <path>" -ForegroundColor Red
        exit 1
    }
    if (-not (Test-Path $Path)) {
        Write-Host "[ERROR] Path not found: $Path" -ForegroundColor Red
        exit 1
    }
    $existing = $registry.skills | Where-Object { $_.name -eq $Name }
    if ($existing) {
        Write-Host "[SKIP] Skill '$Name' already registered." -ForegroundColor Yellow
    } else {
        $registry.skills += @{ name = $Name; path = $Path }
        $registry | ConvertTo-Json -Depth 3 | Set-Content $ConfigFile -Encoding utf8
        Write-Host "[ADDED] Skill '$Name' -> $Path" -ForegroundColor Green
    }
    exit 0
}

# === Sync ===
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Skills Sync to OneDrive" -ForegroundColor Cyan
Write-Host "  Archive: $ArchiveRoot" -ForegroundColor DarkGray
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$skillsToSync = if ($Name) {
    $registry.skills | Where-Object { $_.name -eq $Name }
} else {
    $registry.skills
}

if (-not $skillsToSync) {
    Write-Host "[ERROR] No skills found to sync." -ForegroundColor Red
    exit 1
}

$synced = 0
$failed = 0

foreach ($skill in $skillsToSync) {
    $src = $skill.path
    $dst = Join-Path $ArchiveRoot $skill.name

    Write-Host "[$($skill.name)]" -ForegroundColor White -NoNewline

    if (-not (Test-Path $src)) {
        Write-Host " SKIP - source not found: $src" -ForegroundColor Yellow
        $failed++
        continue
    }

    # Sync with robocopy (mirror mode, exclude .git)
    $null = robocopy $src $dst /MIR /XD .git /NFL /NDL /NJH /NJS /NC /NS 2>&1

    $fileCount = (Get-ChildItem $dst -Recurse -File).Count
    Write-Host " OK - $fileCount files synced" -ForegroundColor Green
    $synced++
}

Write-Host ""
Write-Host "Done: $synced synced, $failed skipped" -ForegroundColor Cyan
Write-Host ""
