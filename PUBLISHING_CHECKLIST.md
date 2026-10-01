# IberOS v1.0 publication checklist

## Automatic once accounts/connectors are available

### GitHub
1. Create public repository `IberOS`.
2. Upload this repository tree.
3. Keep `main` as default branch.
4. Enable GitHub Pages using GitHub Actions.
5. Create release `v1.0.0`.

### Zenodo
1. Connect Zenodo to the same GitHub account.
2. Enable the `IberOS` repository.
3. Publish GitHub release `v1.0.0`.
4. Verify imported metadata, creator and license.
5. Record the version DOI in the repository.

### PyPI
1. Create/claim the `iberos` project through Trusted Publishing.
2. Configure GitHub repository, workflow `publish-pypi`, environment `pypi`.
3. Publish GitHub release.
4. Verify `pip install iberos`.

### Hugging Face
1. Create a public dataset repository named `iberos-curated-benchmark`.
2. Upload the contents of `/data`.
3. Keep `/data/README.md` as the Dataset Card.
4. Verify the dataset viewer and license metadata.

### Software Heritage
1. After GitHub is public, request Save Code Now, or let the included release workflow request archival.
2. Record the resulting SWHID in `CITATION.cff` / README once available.

## Manual decisions still required

- GitHub username/organization and final repository URL.
- Whether `iberos` is available as a PyPI project name.
- Final GitHub Pages URL.
- Whether to publish the benchmark under a personal Hugging Face account or an organization.
- Zenodo version DOI after release ingestion.
