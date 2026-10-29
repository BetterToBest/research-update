# Auto-chain

status: on
max_chained_sessions_per_day: 6
delay_minutes: 5

When `status: on`, `/end-session` schedules the next step as a fresh Claude Code session (a one-shot scheduled task), so each step starts with a clean context and no one has to paste the start lines. Duke turns it off by changing `on` to `off` here (or deleting the scheduled tasks in Claude Code).

The chain stops by itself, and the next session is left for Duke to start, when:
- the next step waits on an unanswered ledger decision, Duke's own action (marked "(you)", the chat exports for S31, the Academia links for S43), or money (S48, Runpod);
- the step just finished is not done (checks red, PR left open, or the work ran out of room);
- the daily limit above is reached;
- the scheduling tool is not available in the session.

## Log
<!-- /end-session appends one line per scheduled run: date time UTC, from step, to step, model, effort -->
