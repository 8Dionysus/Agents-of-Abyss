# Experience Deployment Law

1. A certified release may be activated only through a deployment plan.
2. A deployment plan must define rings, probes, watch windows, promotion gates and rollback path.
3. Codex may assemble deployment evidence and propose decisions, but cannot promote a ring or certify production stability.
4. An assistant cannot deploy, promote or roll back itself.
5. Every alarm that can cause durable rollback must receive bounded eval verdict or explicit emergency authority.
6. Rollout promotion is forbidden while material drift alarms remain open.
7. Post-release incidents must re-enter the experience loop instead of becoming hidden local patches.
