# Publishing This Skill to GitHub

Step-by-step instructions for publishing the skill to GitHub. Three paths
are documented depending on your comfort with technical tools.

- **Path A — Web interface only (no installs)** — recommended if you have
  never used Git or a code editor
- **Path B — GitHub Desktop** — recommended if you want a graphical tool
  but don't want to use the command line
- **Path C — Command line (Git)** — fastest once you know it

All three produce the same outcome: a public GitHub repository that
practitioners worldwide can find, fork, and adapt.

---

## Before you start

You will need:
1. A **GitHub account** (free) — sign up at <https://github.com>
2. The repository files prepared on your computer — you have these in the
   ZIP file Claude produced
3. About **20 minutes** the first time; 5 minutes for updates

The repository structure you will publish is the full tree shown in the
**Repository structure** section of `README.md` — root documentation files
plus the `whs-professional/` skill folder. The skill folder currently
contains 1 `SKILL.md`, 22 reference files under `references/`, and the
`examples/` folder. That inventory grows over time, so treat the README
tree as the source of truth and **package the whole `whs-professional/`
folder — do not hand-pick files**.

---

## Path A — Web interface only

You won't install anything; you'll do everything in a web browser.

### Step 1 — Create the repository

1. Sign in to <https://github.com>
2. Click the **+** icon in the top-right → **New repository**
3. Fill in:
   - **Repository name**: `whs-professional-skill` (or your preference)
   - **Description**: "Claude skill for AU/NZ Work Health and Safety
     professionals"
   - **Public** (so others can find it)
   - **Add a README file** — leave unchecked (you have your own)
   - **Add .gitignore** — None
   - **Choose a license** — None (you have your own LICENSE file)
4. Click **Create repository**

### Step 2 — Upload your files

1. On the new empty repository page, click **uploading an existing file**
   (in the "Quick setup" message). If you don't see it, click **Add file**
   → **Upload files**
2. Drag and drop these files from your computer into the upload area:
   - `README.md`
   - `ADAPTING.md`
   - `DISCLAIMER.md`
   - `CONTRIBUTING.md`
   - `LICENSE`
3. Scroll to the bottom; in **Commit changes**, write a short description
   (e.g. "Initial publication of repository documentation")
4. Click **Commit changes**

### Step 3 — Add the skill folder

GitHub's web interface doesn't allow drag-and-drop of folders directly, so
you upload files into a folder you create.

1. Click **Add file** → **Create new file**
2. In the filename box, type: `whs-professional/SKILL.md`
   (the slash creates the folder)
3. Open your local `SKILL.md` in a text editor (Notepad on Windows,
   TextEdit on Mac, or any code editor)
4. Copy the entire contents and paste into the GitHub editor
5. Scroll down; commit changes ("Add SKILL.md")

6. Repeat for every file in the skill folder — each reference file under
   `whs-professional/references/` and each file under
   `whs-professional/examples/`. The complete file list is the repository
   tree in `README.md` (currently 1 `SKILL.md` + 22 reference files +
   the `examples/` folder). Do not hand-pick a subset — the skill folder
   ships whole.

7. After all files are uploaded, your repository should match the
   structure shown in `README.md`.

### Step 4 — Add a Release with the packaged skill archive

So that practitioners can download a single ready-to-install archive.
Claude expects a **`.zip` of the single top-level skill folder**
(`whs-professional/` with `SKILL.md` inside); renaming the archive to
`.skill` is optional legacy naming — check <https://support.claude.com>
for the current upload wording.

1. On your computer, package the skill folder from a terminal:

   ```bash
   cd path/to/repo
   zip -r whs-professional.zip whs-professional -x "*.DS_Store" -x "__MACOSX/*"
   ```

   On macOS, `ditto -c -k --norsrc whs-professional whs-professional.zip`
   produces the same clean archive.

   > **Do not use macOS Finder "Compress"** (right-click → Compress): it
   > adds `__MACOSX/` and AppleDouble (`._*`) entries that can break the
   > skill upload. Use the command above, or download the artifact built
   > by the GitHub Action (`.github/workflows/package.yml`) when you push
   > a version tag.

2. In GitHub, on your repository page, click **Releases** (right
   sidebar) → **Create a new release** (or **Draft a new release**)
3. **Choose a tag**: type `v1.0.0` and click "Create new tag"
4. **Release title**: "v1.0.0 — Initial release"
5. **Description**: brief notes about what's in this release
6. **Attach binaries**: drag the `whs-professional.zip` (and optionally a
   copy renamed `whs-professional.skill`) into the "Attach binaries" area
7. Click **Publish release**

Practitioners can now download the packaged skill directly from your
Releases page.

### Step 5 — Verify

Open an incognito / private browsing window and navigate to your repository
URL. Confirm:
- The README displays on the front page
- The folder structure is correct
- You can navigate into `whs-professional/references/` and see all files
- The Releases page shows v1.0.0 with the `.skill` file attached

You are now published.

---

## Path B — GitHub Desktop

GitHub Desktop is a free graphical tool from GitHub. Install from
<https://desktop.github.com>.

### Step 1 — Create and clone the repository

1. Open GitHub Desktop → **File** → **New Repository**
2. Fill in:
   - **Name**: `whs-professional-skill`
   - **Local path**: choose a folder on your computer
   - **Initialise this repository with a README**: unchecked
   - **Git Ignore**: None
   - **License**: None
3. Click **Create Repository**

### Step 2 — Copy files in

1. Open the local folder GitHub Desktop created (it will show the path)
2. Copy in all your files following the structure shown above:
   - `README.md`, `ADAPTING.md`, `DISCLAIMER.md`, `CONTRIBUTING.md`,
     `LICENSE`, `PUBLISHING.md` at the root
   - `whs-professional/` folder containing `SKILL.md` and the `references/`
     subfolder

### Step 3 — Commit and publish

1. Switch back to GitHub Desktop — it will show all the files as changes
2. In the bottom-left, enter a commit summary: "Initial publication"
3. Click **Commit to main**
4. In the top toolbar, click **Publish repository**
5. In the dialog:
   - Uncheck "Keep this code private"
   - Click **Publish Repository**

### Step 4 — Add a Release

Follow Step 4 from Path A (in the GitHub web interface).

---

## Path C — Command line

Requires Git installed (<https://git-scm.com/downloads>) and a working
terminal.

```bash
# 1. Create an empty repository on github.com (web)
#    — name it whs-professional-skill, public, no README/.gitignore/license

# 2. On your computer, in the folder containing your files:
cd path/to/repo-folder
git init
git add .
git commit -m "Initial publication"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/whs-professional-skill.git
git push -u origin main

# 3. Package the skill archive (exclude macOS noise; never use Finder
#    "Compress", which adds __MACOSX/AppleDouble entries):
zip -r whs-professional.zip whs-professional -x "*.DS_Store" -x "__MACOSX/*"
#    (macOS alternative: ditto -c -k --norsrc whs-professional whs-professional.zip)
#    Optionally: cp whs-professional.zip whs-professional.skill  # legacy naming

# 4. Create the release (in the GitHub web interface, then attach the
#    archive) — or push a v* tag and let .github/workflows/package.yml
#    build and upload the artifact for you
```

---

## After publishing

### Promote it

- LinkedIn post linking to the repo
- Share in AIHS, NSCA, or other WHS practitioner forums
- Submit to relevant directories of Claude skills

### Maintain it

- When regulations change, edit the relevant file in the GitHub web
  interface (or locally) and commit
- For each meaningful update, draft a new release with the updated
  skill archive attached (push a `v*` tag and the packaging workflow
  builds it for you)
- Increment the version number: `v1.0.0` → `v1.1.0` for minor updates;
  `v2.0.0` for major restructures

### Respond to contributors

- Watch the **Issues** and **Pull Requests** tabs on your repository
- Review and merge worthwhile contributions
- Decline (politely) contributions that fall outside scope per
  `CONTRIBUTING.md`

---

## Common issues

**"I uploaded the files but the README doesn't show on the front page"**
Make sure the file is named exactly `README.md` at the root of the
repository, not inside a subfolder.

**"My skill archive won't install in Claude"**
The file must be a ZIP archive (`.zip`, or `.skill` as legacy naming for
the same ZIP). The structure inside must be a single top-level folder
(`whs-professional/`) containing `SKILL.md` and the `references/`
subfolder. Common errors:
- The ZIP contains the files directly, not inside a folder
- The ZIP contains `__MACOSX/` or `._*` entries from macOS Finder
  "Compress" — rebuild it with the CLI command in Step 4
- The folder name doesn't match the `name` field in `SKILL.md` frontmatter
- The `description` in `SKILL.md` exceeds 1024 characters

**"The folder structure looks wrong on GitHub"**
GitHub displays folder paths from the slashes in filenames. If you see
`whs-professional` as a folder but `SKILL.md` is sitting outside it, you
likely uploaded the file to the root instead of the folder. Delete the
file and re-upload using the full path `whs-professional/SKILL.md`.
