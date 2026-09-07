---
layout: page
title: Environnement
permalink: /environment/
---

Ce guide vous aide à préparer votre environnement de travail pour les séances de TP du module **Systèmes d'Exploitation**.

**Important** : votre environnement doit être opérationnel **avant** la première séance de TP. Les 5 points d'« Environnement prêt » sont attribués si votre terminal fonctionne dès le début de la séance.

---

## Windows — Installer WSL2

WSL2 (Windows Subsystem for Linux version 2) permet d'exécuter un véritable noyau Linux directement sous Windows, sans machine virtuelle.

### Prérequis

- Windows 10 version 2004 (build 19041) ou supérieur, **ou** Windows 11
- Droits administrateur sur votre machine

### Étapes d'installation

#### 1. Activer WSL et installer Ubuntu

1. Ouvrez **PowerShell** en mode Administrateur (clic droit sur le menu Démarrer → Windows PowerShell (Admin) ou Terminal (Admin)).
2. Exécutez la commande suivante :

   ```powershell
   wsl --install -d Ubuntu
   ```

3. L'installation active automatiquement WSL2 et installe la distribution Ubuntu.
4. **Redémarrez votre ordinateur** si demandé.

#### 2. Créer votre compte utilisateur Linux

1. Après le redémarrage, Ubuntu se lance automatiquement. Sinon, cherchez « Ubuntu » dans le menu Démarrer.
2. Créez un **nom d'utilisateur** et un **mot de passe** pour Linux.
   - Le nom d'utilisateur n'a pas besoin d'être identique à celui de Windows.
   - Notez ce mot de passe — vous en aurez besoin pour les commandes `sudo`.
3. Une fois créé, vous voyez l'invite du shell :

   ```
   votreutilisateur@votremachine:~$
   ```

   Votre environnement Linux est prêt.

### Vérifier l'installation

Dans PowerShell (pas besoin d'être administrateur), exécutez :

```powershell
wsl -l -v
```

Résultat attendu :

```
  NAME      STATE           VERSION
  Ubuntu    Running         2
```

Si `VERSION` indique `1`, passez en WSL2 avec :

```powershell
wsl --set-version Ubuntu 2
```

### Problèmes fréquents

| Problème | Cause probable | Solution |
|----------|----------------|----------|
| `wsl` non reconnu | Windows trop ancien | Mettre à jour Windows ou utiliser l'[installateur manuel](https://learn.microsoft.com/fr-fr/windows/wsl/install-manual) |
| Erreur 0x80070003 | Fonctionnalité WSL non activée | `dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart` |
| Ubuntu ne démarre pas | Virtualisation désactivée dans le BIOS | Redémarrer → BIOS (F2/Del) → Activer Intel VT-x ou AMD SVM |
| WSL1 au lieu de WSL2 | Version par défaut en WSL1 | Exécuter `wsl --set-version Ubuntu 2` |

---

## macOS — Utiliser le Terminal intégré

macOS est un système UNIX — **aucune installation supplémentaire n'est nécessaire**.

1. Ouvrez **Terminal.app** :
   - `Applications` → `Utilitaires` → `Terminal`
   - Ou cherchez « Terminal » avec Spotlight (`Cmd + Espace`)

2. Vérifiez votre shell :

   ```bash
   echo $SHELL
   ```

   - Par défaut sur les macOS récents, c'est `zsh`, qui fonctionne parfaitement pour tous les TP.
   - Pour utiliser Bash, tapez `bash` ou changez votre shell par défaut avec `chsh -s /bin/bash`.

### Optionnel : installer Homebrew

Pour installer des outils Linux supplémentaires :

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

## Linux — Utiliser votre terminal natif

Si vous utilisez Linux (Ubuntu, Fedora, Debian, Arch, etc.), vous êtes **déjà prêt**.

1. Ouvrez votre émulateur de terminal :
   - **GNOME** : `gnome-terminal` ou `Console`
   - **KDE** : `konsole`
   - **XFCE** : `xfce4-terminal`
   - Tout autre : `alacritty`, `kitty`, `rxvt`, `st`

2. Vérifiez que Bash est disponible :

   ```bash
   echo $SHELL
   ```

   - Si ce n'est pas Bash, tapez `bash` pour le lancer.

### Mettre à jour les paquets (recommandé)

```bash
sudo apt update && sudo apt upgrade -y   # Ubuntu/Debian
# OU
sudo dnf upgrade                         # Fedora
```

---

## Vérification finale (tous les OS)

Ouvrez un terminal et exécutez ces deux commandes :

```bash
echo $SHELL
ls /
```

**Résultats attendus :**
- `echo $SHELL` → `/bin/bash` ou `/bin/zsh`
- `ls /` → une liste de répertoires système (`bin`, `etc`, `home`, `usr`, `var`, etc.)

Si les deux fonctionnent, vous êtes prêt pour le TP. Sinon, revenez à la section correspondant à votre OS ci-dessus.

---

## Ressources complémentaires

- [Documentation officielle WSL](https://learn.microsoft.com/fr-fr/windows/wsl/)
- [Installation manuelle WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install-manual)
- [Homebrew pour macOS](https://brew.sh)
