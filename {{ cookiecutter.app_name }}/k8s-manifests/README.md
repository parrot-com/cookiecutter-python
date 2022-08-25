When starting a new project, you should be able to copy these files straight into `kube-workloads` repo.

While this should provide a good baseline, make sure to go over the manifests and make any changes that are necessary for your project.
You also need to update the following files:
- apps/sandbox/kustomization.yaml
- apps/sandbox/monitoring/prometheus-stack/servicemonitors/kustomization.yaml
- infra/sandbox/kustomization.yaml

If you wish to deploy to production, prepare files similarly to how they are in `sandbox` into `production` and move staging-only files to impl where it makes sense.
