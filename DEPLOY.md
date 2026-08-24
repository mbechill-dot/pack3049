# Putting the site on GitHub and pointing pack3049.com at it

Two halves. GitHub hosts the files, Spaceship tells the internet where to find them. Do them in that order, because GitHub needs to see the domain before it will issue the certificate.

The repository is **already initialized and committed** in this folder, so you are starting from step 2, not step 1.

---

## Part 1: GitHub

### 1. Make an empty repository

On github.com, click the green **New** button at the top of your Top repositories list.

- **Name:** `pack3049` is fine. The name does not appear anywhere once the custom domain is working.
- **Public.** GitHub Pages is only free on public repositories, and this site has nothing private in it.
- **Do not** tick "Add a README", "Add .gitignore", or "Choose a license". The repository must be empty or the push below will be rejected.

Click **Create repository**. Leave that page open, you need the URL from it.

### 2. Push this folder

Open a terminal in this folder and run these two lines. Your username is already filled in.

```bash
git remote add origin https://github.com/mbechill-dot/pack3049.git
git push -u origin main
```

The branch is already named `main`, so there is no `git branch -M` step.

If it asks for a password, GitHub does not accept your account password here. Use a **personal access token** instead: github.com, your avatar, Settings, Developer settings, Personal access tokens, Tokens (classic), Generate new token, tick **repo**, then paste that token as the password.

The commit is already made, so nothing else needs doing. If you would rather avoid the terminal entirely, the repository page has an **uploading an existing file** link where you can drag this whole folder in. That works, it is just slower to update later.

### 3. Turn on Pages

In the repository: **Settings**, then **Pages** in the left sidebar.

- **Source:** Deploy from a branch
- **Branch:** `main`, folder `/ (root)`
- **Save**

Give it a minute or two. The site appears at `https://mbechill-dot.github.io/pack3049/`. **Open it and check it works before touching DNS.** If something is wrong, it is much easier to diagnose here than after the domain is in the mix.

### 4. Tell GitHub about the domain

Still in **Settings, Pages**, under **Custom domain**, type:

```
pack3049.com
```

and Save. It will complain that DNS is not configured. That is expected and correct. That is Part 2.

The `CNAME` file in this repository already says `pack3049.com`, so GitHub may fill this in for you automatically.

---

## Part 2: Spaceship

Sign in at spaceship.com, then go to **Advanced DNS Manager** and select **pack3049.com**. Open **DNS records**, then **Custom records**.

**Delete any parking or placeholder records first.** Spaceship adds its own A record and sometimes a CNAME pointing at a parked page. If you leave those, they fight with the ones below and the site will load intermittently or not at all. Remove every existing A, AAAA, and CNAME record for `@` and `www` before adding these.

### The records to add

Six records total. Four A records for the bare domain, one CNAME for www, and that is it.

| Type | Host | Value | TTL |
|---|---|---|---|
| A | `@` | `185.199.108.153` | Automatic |
| A | `@` | `185.199.109.153` | Automatic |
| A | `@` | `185.199.110.153` | Automatic |
| A | `@` | `185.199.111.153` | Automatic |
| CNAME | `www` | `mbechill-dot.github.io` | Automatic |

Yes, four separate A records all on `@`. That is not a mistake. Add them one at a time with **+ Add record**.

The CNAME value is your GitHub username followed by `.github.io`, with a trailing dot if Spaceship adds one. It is **not** the repository name and **not** the full Pages URL.

### Optional, for IPv6

Nothing breaks without these, but they help visitors on IPv6-only networks.

| Type | Host | Value |
|---|---|---|
| AAAA | `@` | `2606:50c0:8000::153` |
| AAAA | `@` | `2606:50c0:8001::153` |
| AAAA | `@` | `2606:50c0:8002::153` |
| AAAA | `@` | `2606:50c0:8003::153` |

---

## Part 3: Wait, then turn on HTTPS

DNS changes spread across the internet on their own schedule. Usually under an hour, occasionally several.

Go back to **Settings, Pages** on GitHub and watch the message under Custom domain. When it changes from an error to **DNS check successful**, the **Enforce HTTPS** checkbox becomes available. Tick it.

GitHub says the certificate can take up to 24 hours. In practice it is usually minutes once the DNS check passes.

**Do not skip Enforce HTTPS.** Without it the site is served over plain `http`, and browsers will show visitors a "Not secure" warning next to a page asking families to register their children.

---

## If something goes wrong

**"There isn't a GitHub Pages site here"** right after adding the domain. Normal. DNS has not spread yet. Wait.

**The site loads but has no styling.** The `.nojekyll` file is missing or was not committed. It is in this repository, so this should not happen.

**Spaceship's parked page keeps appearing.** An old A or CNAME record is still there. Go back and delete every record for `@` and `www` that is not in the tables above.

**HTTPS never becomes available.** Almost always a CNAME pointing at the wrong place. It must be `mbechill-dot.github.io`, not `pack3049.com` and not the repository URL.

**A note on your other repositories.** You already have `mbechill-dot.github.io`, which is your GitHub user site, and `summitbiofilm-site`. Neither is affected by any of this. A user site and a project site with its own custom domain coexist fine, and the `www` CNAME pointing at `mbechill-dot.github.io` is correct even though that repository exists. GitHub routes by the `CNAME` file inside each repository, not by the hostname alone.

**You want to check DNS yourself.** From a terminal:

```bash
dig pack3049.com +short          # should list the four 185.199.x.x addresses
dig www.pack3049.com +short      # should show mbechill-dot.github.io
```

---

## Making changes later

Edit the files, then:

```bash
git add -A
git commit -m "what you changed"
git push
```

GitHub rebuilds within a minute. If you use the generator, run `python3 build.py` before committing so the HTML matches `content.py`.

Read `LAUNCH.md` for what is still a placeholder and what works the moment this goes live.
