# Coda locale del thread principale

Copie degli script della coda (originali nella scratchpad della sessione, che si perde quando il container viene ricreato).
Dopo un reset: ricreare i worktree (`tcg_e030` ad ab6f2dd, `tcg_e031` su main, `e020_res` su questo branch), estrarre gli input
da `claude/project-thread-1tcjlo:dati/E-0xx-input` in `/home/claude/e0xx_in`, copiare questi script nella scratchpad e lanciarli con
`setsid nohup bash <script> &`. Gli incroci finiti si saltano e `--riprendi` riprende quelli a metà.
