# Connecting to a Remote Repository

1. Initialize git (already done by Cookiecutter) or run `git init`.
2. Create an empty remote repository (GitHub/GitLab/Bitbucket) under the org/user you specified (`{{ cookiecutter.organization }}`).
3. Add the remote:
   - SSH: `git remote add origin git@github.com:{{ cookiecutter.organization }}/{{ cookiecutter.project_slug }}.git`
   - HTTPS: `git remote add origin https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_slug }}.git`
4. Push the default branch: `git push -u origin main`.
5. (Optional) Add a second remote, e.g., `git remote add upstream ...`.

## Personal Access Tokens (HTTPS)

When using HTTPS with PATs:

```bash
git config credential.helper store
git push -u origin main
```

Enter `username` and the PAT once; it will be cached locally.

## Keeping Forks in Sync

```
git fetch upstream
git merge upstream/main
```

## Troubleshooting

- Use `git remote -v` to verify URLs.
- Ensure you have permissions for the target org/project.
- SSH keys must be uploaded to the hosting provider before pushing.

