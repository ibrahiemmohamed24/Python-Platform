# Security Policy

## Supported versions

The project is in early development. Security fixes are applied to the latest
commit on the `main` branch; no released versions are supported yet.

## Reporting a vulnerability

Do not open a public issue containing exploit details, credentials, or private
data.

If GitHub private vulnerability reporting is enabled for this repository, use
that channel. Otherwise, contact the repository owner privately through the
contact details on their GitHub profile and include:

- the affected component;
- steps to reproduce the issue;
- the potential impact;
- any suggested mitigation.

Please allow the maintainer time to investigate before public disclosure.

## Current deployment warning

The analysis API launches local quality tools against server-side files. It is
not designed for direct public exposure. A hosted version should use isolated
temporary workspaces, resource limits, bounded concurrency, and a file-upload
or source-code job contract.
