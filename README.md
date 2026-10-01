# Tu Día de Blanco for Claude and ChatGPT

Manage your [Tu Día de Blanco](https://tudiadeblanco.com) wedding from Claude or ChatGPT: guests and RSVPs, seating, budget, tasks and notes, the day's schedule, your invitation website, Concierge, documents and Moodboard.

Version **2.0.0** bundles **10 skills** and connects to the remote MCP server at `https://tudiadeblanco.com/mcp`. Couples and wedding planners sign in with OAuth and connect one wedding at a time; current Membership, Module, Role and Side permissions apply on every call.

## Install

### Claude Code

```
/plugin marketplace add vayllon301/tudiadeblanco-plugin
/plugin install tudiadeblanco@tudiadeblanco
```

Restart Claude Code, run `/mcp` and sign in to Tu Día de Blanco to choose the wedding to connect.

### Claude.ai and Claude Desktop

Add a custom connector (Settings → Connectors → Add custom connector) with the URL `https://tudiadeblanco.com/mcp` and sign in. To add the skills, download the [latest release](https://github.com/vayllon301/tudiadeblanco-plugin/releases/latest) and upload them in Settings → Capabilities → Skills.

### ChatGPT and Codex

Download [`tudiadeblanco-chatgpt.zip`](https://github.com/vayllon301/tudiadeblanco-plugin/releases/latest/download/tudiadeblanco-chatgpt.zip) and add it as a plugin, then sign in when prompted. For Codex without the plugin, see [codex/config.toml](codex/config.toml).

## How changes work

**Every change produces a 30-minute proposal that you review and approve on the website.** Saying yes in the chat cannot apply it. Publishing and sending emails need extra consent (`wedding.publish`, `wedding.communicate`) on top of `wedding.write`; existing connections are not widened. Guest and Budget batches and Seating assignments are transactional. Accepted emails are not necessarily delivered, and unknown outcomes are never retried automatically.

Charges, subscriptions, account removal, credentials and Membership/Ownership changes stay on the website. Recording a payment you already made to a vendor never moves money. Notes respect Side privacy, Moodboard is Couple-only and anonymous Letters never reveal their author.

See the [capability catalogue](skills/wedding-workspace/references/capabilities.md) for every operation.

## Build

```sh
python3 scripts/package-plugin.py   # dist/tudiadeblanco-<version>.zip (ChatGPT/Codex plugin)
./scripts/package-skills.sh         # dist/<skill>.zip (Claude.ai skill uploads)
```

Use `get_capabilities` to check the release the server is actually running. Support: [tudiadeblanco.com](https://tudiadeblanco.com) · [Privacy](https://tudiadeblanco.com/legal/privacy) · [Terms](https://tudiadeblanco.com/legal/terms).
