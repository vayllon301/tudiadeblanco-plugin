# TuDiaDeBlanco

Manage your [Tu Día de Blanco](https://tudiadeblanco.com) wedding from Claude or ChatGPT: guests and RSVPs, seating, budget, tasks and notes, the day's schedule, your invitation website, Concierge, documents and Moodboard.

Version **2.5.4** bundles **10 skills** and connects to the remote MCP server at `https://tudiadeblanco.com/mcp`. Couples and wedding planners sign in with OAuth and connect one wedding at a time; current Membership, Module, Role and Side permissions apply on every call.

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

**Changes apply as soon as the assistant makes them.** Claude asks you to confirm each change in the chat, and the skills tell it to say exactly what will happen before removing information, publishing to guests or sending emails. Uploads work differently: `prepare_upload` creates a short-lived link where you choose the file on the website yourself, and the file is saved when you upload it there. Documents and Moodboard images stay private; Website and invitation email images are stored as public image files so they can be shown to guests, but putting one on your Website or invitation email is a separate change. Publishing and sending emails need extra consent (`wedding.publish`, `wedding.communicate`) on top of `wedding.write`; existing connections are not widened. Guest and Budget batches and Seating assignments are transactional. Accepted emails are not necessarily delivered, and unknown outcomes are never retried automatically.

Charges, subscriptions, account removal, credentials and Membership/Ownership changes stay on the website. Recording a payment you already made to a vendor never moves money. Notes respect Side privacy, Moodboard is Couple-only and anonymous Letters never reveal their author.

See the [capability catalogue](skills/wedding-workspace/references/capabilities.md) for every operation.

## Data and privacy

The plugin contains only skills and a connector reference; it runs no code on your computer. Claude talks to one server, `https://tudiadeblanco.com/mcp`, operated by Tu Día de Blanco:

- **Sent to the server:** the arguments of each tool call Claude makes (for example a Guest's name, a budget amount or a search term) and your OAuth token. Whole conversations, Claude's memory and your other files are never requested.
- **Returned to Claude:** the wedding data each tool reads, limited by your Role, Modules and Side.
- **Stored by Tu Día de Blanco:** a record of each change (the request, a preview of the affected records and its result), and an audit log of tool calls (tool name, success, error) for the connected wedding.
- **Passed on to other services:** invitation and reminder emails are sent through our email provider, Resend; changes to Tasks you chose to sync to Google Calendar or Google Tasks update them there; connecting or verifying a custom Website domain registers it with our hosting provider, Vercel, and checks its DNS records; and `preview_concierge` sends its sample question to the Tu Día de Blanco Concierge service, which answers with an AI model provider and counts against your Concierge quota.

See the [Privacy Policy](https://tudiadeblanco.com/legal/privacy) for retention and your rights.

## Build

```sh
python3 scripts/package-plugin.py   # dist/tudiadeblanco-<version>.zip (ChatGPT/Codex plugin)
./scripts/package-skills.sh         # dist/<skill>.zip (Claude.ai skill uploads)
```

Use `get_capabilities` to check the release the server is actually running. Support: [tudiadeblanco.com](https://tudiadeblanco.com) · [Privacy](https://tudiadeblanco.com/legal/privacy) · [Terms](https://tudiadeblanco.com/legal/terms).

## Model reliability

Tools expose input/output schemas, structured results and OAuth/safety metadata. Skills explain how to resolve real IDs, read all relevant pages, apply atomic batches and verify applied results. `get_capabilities.server_version` identifies the deployed server independently of this package.

Updating this package does not deploy the MCP server or update a directory submission.
