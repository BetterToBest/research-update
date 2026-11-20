# Outside readings through OpenRouter's free tier: setup and choice of model (Nov 20, 2026)

Written in S85 part 4, after Duke added an OpenRouter key to this environment because NVIDIA's daily allowance may run out. It is a second route to a reader that is not Claude, for the same jobs as the NVIDIA catalogue (`audits/2026-11-17-nvidia-setup.md`): an independent reading of a preregistration, analysis plan or results before they are published, a second check of a derivation, bulk classification or summaries of long text. It cannot run a study: a model returns text and has no machine to run code on. Which model to use and when is Claude's call.

## What was checked on Nov 20

- `openrouter.ai` is reachable from a cloud session here and the proxy adds the key (no key is held in the session). The model list (443 models) opens; the key's own page says: free tier, no spending limit set, no credit used, **50 requests a day to free models** (the counter lags by a call or two, so count your own).
- One chat call to `nvidia/nemotron-3-ultra-550b-a55b:free` answered ("ready", 23 tokens in, 23 out, cost 0). One call to `google/gemma-4-31b-it:free` was refused with a 429 from Google's side ("temporarily rate-limited upstream", a pool shared by all free users, not this key); a retry later is the remedy. Later the same day four more tries, 90 seconds apart, were refused the same way, so no Google reading exists yet (`audits/2026-11-20-s85-part4-reading.md`); Nemotron on OpenRouter answered every call.
- The free models on Nov 20 (15 listed with price 0; ids end in `:free` except two Google music models whose ids do not, which are not language readers): `nvidia/nemotron-3-ultra-550b-a55b:free` (1,000,000 tokens of context, 65,536 out; the same model the NVIDIA catalogue serves, so it is the same reader, not a new one), `nvidia/nemotron-3.5-super-vl:free`, `nvidia/nemotron-3.5-lightning:free` and `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` (NVIDIA again), `google/gemma-4-31b-it:free` and `google/gemma-4-26b-a4b-it:free` (Google; 262,144 context, 32,768 out; a different maker), `baidu/ernie-5.5-flash-preview:free` (1,024,000), `inclusionai/ling-3.2-flash:free` (1,048,576), `particle-ai/particle-1:free` (1,048,576), `dots-studio/dots-3-note-preview:free` (512,000), `recursive/flint-v1.0:free` (262,144), `liquid/lfm-3-1.7b:free` (a 1.7 billion parameter model: too small for a reading), and the router `openrouter/free` (it picks any free model; use only when the reader does not matter). The list changes; read it again before choosing.

## How Claude chooses

1. **A reader from a different maker than Claude, and than the last reading, is the point.** Nemotron already read the S82, S90 and S85 documents; a Gemma reading (Google) of the same packet adds a maker. Gemma's 32,768-token output limit and 262,144-token context are enough for a packet of about 150,000 characters (an earlier packet was 119,191). Where a packet is longer than that, cut it by section and say what was left out, as the earlier packets did.
2. **Nemotron on OpenRouter is the fallback** when the NVIDIA catalogue's daily allowance is used up: same model, same prompts, so a repeat reading is comparable to the earlier ones.
3. **The newer models from makers I have no track record for (Baidu, inclusionAI, Particle, dots, Recursive) are tried on a small packet first.** Reading a model's page on OpenRouter before using it is part of choosing; a reader whose answer shows it did not read the packet (wrong section names, invented figures) is dropped and the reply is saved with that said.
4. **Only ids ending in `:free`.** The key has no credit set, but the money rule (CLAUDE.md) holds: nothing that costs money runs. A model id without `:free` is never sent.

## How a reading is requested

`POST https://openrouter.ai/api/v1/chat/completions` with `{"model": "<id>:free", "messages": [...], "max_tokens": N}`. Reasoning models spend `max_tokens` on reasoning first (the NVIDIA lesson): give a long packet 40,000 where the model allows it, 30,000 for Gemma. The answer is in `choices[0].message.content`, the reasoning in `choices[0].message.reasoning`. On a 429 wait and retry; on a 200 with an empty `content` and a full `reasoning`, raise `max_tokens` and ask again.

## What may be sent

Free providers can keep and train on what they receive. Send only what is already public in the repositories (preregistrations, reports, results tables, source texts), as every packet so far has been, and never personal details of Duke or anyone else. The packet is saved in `audits/` beside the reply so the reading can be repeated, and the reply is saved word for word.

## What an outside reading is

A reading, not a result and not an economist's review. Nothing it says enters a figure without the source being opened; where it is right, the fix is made and dated; where it is wrong or out of scope, the reply is kept and the reason written beside it.
