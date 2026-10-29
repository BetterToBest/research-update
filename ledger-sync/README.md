# Ledger sync queue

When a session cannot write the ledger (artifact F1hceP6XEfPQ1pf6Sw1Ki8), `/end-session` saves the change here as `<YYYY-MM-DD>-<step ID>.json`. The next Chat or session that has the ledger tool applies the files oldest first and deletes them.
