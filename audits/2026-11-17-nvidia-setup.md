# A third outside reading on NVIDIA's free API catalogue: setup (Nov 17, 2026)

Written in S13, second pass, part 1, at Duke's request. What it gives: a model from a different maker, run from a Claude Code session on the same audit prompt as Grok and ChatGPT or Gemini (`audits/2026-11-17-release-audit-prompt.md`). It is free within NVIDIA's trial limits; it is not Runpod, so the money rule does not apply.

## What was checked today

- The catalogue's address, `integrate.api.nvidia.com`, is reachable from a cloud session here. Its model list (32 models) opens without a key; a request to a model returns 401 without one, so a key is all that is missing.
- Models in the list suited to a long audit: `nvidia/nemotron-3-ultra-550b-a55b` (the largest; first choice), `mistralai/mistral-large-4-1t-a52b` (second reading, a different maker), `z-ai/glm-5.3-flash`, `stepfun-ai/step-5-preview`. The list changes; the session reads it again before choosing.
- The blueprint page Duke linked (NemoClaw blueprints) is for running an agent on NVIDIA's own hardware or cloud. It is not needed here: the Claude Code session is the agent, and it only needs the API key that the same site gives.

## Duke's steps (about 5 minutes)

1. Go to build.nvidia.com and sign in (or create a free NVIDIA account; it may ask to verify an email or phone number).
2. Open any model page, for example search for "nemotron-3-ultra", and choose **Get API Key** (or open your profile menu, then **API Keys**, then **Generate API Key**). Copy the key. It starts with `nvapi-`.
3. Do not paste the key into the chat. Start the fresh session (`/start-session S13`, part 2) and say "run the NVIDIA reading". Claude then opens a secure form for the host `integrate.api.nvidia.com` (a Bearer token); paste the key there. The key is stored on the cloud environment and added to requests to that host only; Claude never sees it.
4. If the form does not appear (some apps cannot show it), add the key by hand: claude.ai, Claude Code, the environment's settings, network secrets: host `integrate.api.nvidia.com`, header `Authorization`, value `Bearer nvapi-...`.

## What the session then does

1. Reads the model list again and picks the largest available model with a long context.
2. These models cannot browse, so the session builds a packet: the audit prompt with its links replaced by the files' text (the release 2 overview and question reports, the findings-page text, MODEL_SPEC section 14, the S68, S69 and S70 reports, the freeze preregistration's questions and rules, the Nov 9 audit), trimmed to fit the model's context, with a list of what was left out. The packet is saved in `audits/` so the reading can be repeated.
3. Sends it through the OpenAI-compatible endpoint (`/v1/chat/completions`), saves the full reply word for word in `audits/`, and triages it with the Grok and ChatGPT or Gemini replies.
4. Labels the result for what it is: a third AI reading, not an economist's review.
