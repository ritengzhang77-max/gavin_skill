---
name: remote-hpc-slurm
description: "Operate remote HPC/Slurm GPU clusters from Hermes: capture cluster docs locally, establish SSH identity, stage code/data, submit jobs, and poll logs without leaving long jobs attached to chat sessions."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [hpc, slurm, ssh, gpu, remote-execution, cluster]
---

# Remote HPC / Slurm Operations

Use this skill when Gavin asks to run large jobs on an external cluster, login node, university HPC system, Slurm partition, or remote GPU server from Hermes. The goal is to make Hermes a control plane from the current machine while respecting remote auth, scheduler, storage, and billing constraints.

## References

- `references/gautschi.md` — Purdue RCAC Gautschi specifics discovered from the Wanglab tutorial and initial SSH probe.

## Operating pattern

1. **Capture the remote docs locally first.**
   - If the user shares a Google Doc, web page, or cluster tutorial, save a local Markdown copy and optionally the raw HTML/PDF under a durable project/control-plane path.
   - Write a short companion note with the host, login pattern, Slurm account/allocation, storage roots, and open authentication questions.

2. **Separate three identities.**
   - Local Hermes identity: e.g. `whoami` and `hostname` on the current machine.
   - Remote login username: the Unix/Purdue/cluster username used in `ssh <user>@<host>`.
   - Slurm account/allocation: the billing/allocation name passed to `--account` or `-A`.
   Do not assume these are the same. In lab clusters, the Slurm account often names the PI/lab while the SSH username is the user's institutional account.

3. **Probe SSH safely before asking the user for secrets.**
   - Use non-interactive SSH first:
     ```bash
     ssh -o BatchMode=yes -o ConnectTimeout=12 -o StrictHostKeyChecking=accept-new <user>@<host> 'hostname'
     ```
   - This confirms network reachability, host key setup, and whether key auth already works.
   - Redact any password/passcode/token-like prompt text in shared output.

4. **Never ask the user to paste institutional passwords into chat.**
   - If the cluster uses Duo/BoilerKey/MFA, tell the user they likely need their institutional credentials and an MFA approval.
   - Prefer having the user complete the first interactive login out-of-band or approve an interactive SSH session, then add the Hermes machine's public key if the institution allows it.

5. **Set up key-based control when allowed.**
   - Read the local public key, usually `~/.ssh/id_ed25519.pub`.
   - Add it to the remote account's `~/.ssh/authorized_keys` only through an approved login/setup path.
   - After key setup, verify with `BatchMode=yes` again.

6. **Use Slurm as the durable job boundary.**
   - Do not keep big runs attached to a long-lived SSH terminal in Hermes.
   - Stage code/data, submit via `sbatch`, and poll `squeue`, job logs, and output artifacts.
   - Use `sinteractive` only for setup, smoke tests, and short debugging.

7. **Respect storage semantics.**
   - Identify persistent/project storage vs scratch/purgeable storage before launching jobs.
   - Put code, scripts, important outputs, and handoff notes in persistent storage.
   - Put large temporary datasets/checkpoints in scratch only when purge/backup risk is acceptable.

8. **Record reusable cluster facts.**
   - Save stable host/account/storage facts in the local project/control-plane notes and, if broadly useful, in memory.
   - Put session-specific details in `references/<cluster>.md` rather than creating a one-off narrow skill.

## Verification checklist

Before claiming Hermes can run jobs on the cluster:

- [ ] Local docs/notes saved.
- [ ] Remote login username confirmed.
- [ ] SSH reachability tested.
- [ ] Authentication mode known: SSH key, password+MFA, Kerberos/GSSAPI, etc.
- [ ] Non-interactive SSH works, or the need for interactive MFA is clearly stated.
- [ ] Slurm account/allocation and partition known.
- [ ] Persistent and scratch storage roots known.
- [ ] A tiny remote command or smoke-test job has succeeded.

## Pitfalls

- **Do not confuse Slurm account with SSH username.** `--account joywang` is not necessarily the login username.
- **Do not request passwords in Discord/chat.** Use institutional login/MFA flows and SSH keys.
- **Do not run heavy jobs directly over SSH.** Submit `sbatch` jobs and poll.
- **Do not put irreplaceable artifacts only in purgeable scratch.**
- **Do not overgeneralize one cluster's modules or CUDA/PyTorch versions.** Capture those in cluster-specific references.
