# Connector 2.0 capabilities

This catalogue describes the source release. Call `get_capabilities` for the deployed connection. Installing the ZIP does not deploy the server.

Writes create expiring proposals requiring web approval, except `prepare_upload`, which creates a login-bound upload ticket. Publication and communication scopes are explicit; all operations follow Membership, Role, Module and Side.

| Tool | Module | Effect | Additional scopes |
| --- | --- | --- | --- |
| `get_wedding_overview` | Core | Read | — |
| `get_schedule` | Core | Read | — |
| `list_tasks` | Core | Read | — |
| `create_task` | Core | Review write | — |
| `update_task` | Core | Review write | — |
| `list_letters` | letters | Read | — |
| `mark_letter_read` | letters | Review write | — |
| `list_news_posts` | news | Read | — |
| `draft_news_post` | news | Review write | — |
| `list_guests` | guests | Read | — |
| `add_guest` | guests | Review write | — |
| `update_guest` | guests | Review write | — |
| `archive_guest` | guests | Review write | — |
| `get_dietary_report` | dietary | Read | — |
| `get_seating_plan` | seating | Read | — |
| `create_table` | seating | Review write | — |
| `assign_guest_to_table` | seating | Review write | — |
| `get_budget` | budget | Read | — |
| `add_budget_item` | budget | Review write | — |
| `update_budget_item` | budget | Review write | — |
| `delete_budget_item` | budget | Review write | — |
| `list_note_pages` | Core | Read | — |
| `get_note_page` | Core | Read | — |
| `create_note_page` | Core | Review write | — |
| `update_note_page` | Core | Review write | — |
| `delete_note_page` | Core | Review write | — |
| `delete_task` | Core | Review write | — |
| `set_task_options` | Core | Review write | — |
| `replace_schedule` | Core | Review write | wedding.write, wedding.publish |
| `list_menu_items` | dietary | Read | — |
| `create_menu_item` | dietary | Review write | — |
| `update_menu_item` | dietary | Review write | — |
| `delete_menu_item` | dietary | Review write | — |
| `archive_letter` | letters | Review write | — |
| `update_news_post` | news | Review write | wedding.write, wedding.publish |
| `delete_news_post` | news | Review write | wedding.write, wedding.publish |
| `get_wedding_settings` | Core | Read | — |
| `update_wedding_settings` | Core | Review write | wedding.write, wedding.publish |
| `export_guests` | guests | Read | — |
| `export_budget` | budget | Read | — |
| `get_invitation_website` | website | Read | — |
| `update_invitation_website` | website | Review write | wedding.write, wedding.publish |
| `set_website_published` | website | Review write | wedding.write, wedding.publish |
| `get_website_service` | website | Read | — |
| `get_website_slug` | website | Read | — |
| `update_website_slug` | website | Review write | wedding.write, wedding.publish |
| `create_story_chapter` | website | Review write | wedding.write, wedding.publish |
| `update_story_chapter` | website | Review write | wedding.write, wedding.publish |
| `delete_story_chapter` | website | Review write | wedding.write, wedding.publish |
| `reorder_story_chapters` | website | Review write | wedding.write, wedding.publish |
| `create_faq_item` | website | Review write | wedding.write, wedding.publish |
| `update_faq_item` | website | Review write | wedding.write, wedding.publish |
| `delete_faq_item` | website | Review write | wedding.write, wedding.publish |
| `create_gift_option` | website | Review write | wedding.write, wedding.publish |
| `update_gift_option` | website | Review write | wedding.write, wedding.publish |
| `delete_gift_option` | website | Review write | wedding.write, wedding.publish |
| `reorder_gift_options` | website | Review write | wedding.write, wedding.publish |
| `create_gallery_image` | website | Review write | wedding.write, wedding.publish |
| `delete_gallery_image` | website | Review write | wedding.write, wedding.publish |
| `get_wedding_domain` | domain | Read | — |
| `connect_wedding_domain` | domain | Review write | wedding.write, wedding.publish |
| `verify_wedding_domain` | domain | Review write | wedding.write, wedding.publish |
| `disconnect_wedding_domain` | domain | Review write | wedding.write, wedding.publish |
| `preview_concierge` | chatbot | Read | — |
| `get_concierge_config` | chatbot | Read | — |
| `update_concierge_config` | chatbot | Review write | wedding.write, wedding.publish |
| `list_documents` | documents | Read | — |
| `search_documents` | documents | Read | — |
| `read_document_excerpt` | documents | Read | — |
| `update_document_category` | documents | Review write | — |
| `delete_document` | documents | Review write | — |
| `get_moodboard` | moodboard | Read | — |
| `create_moodboard_collection` | moodboard | Review write | — |
| `rename_moodboard_collection` | moodboard | Review write | — |
| `delete_moodboard_collection` | moodboard | Review write | — |
| `create_moodboard_quote` | moodboard | Review write | — |
| `update_moodboard_clip` | moodboard | Review write | — |
| `delete_moodboard_clip` | moodboard | Review write | — |
| `send_guest_invitations` | guests | Review write | wedding.write, wedding.communicate |
| `send_task_reminder` | Core | Review write | wedding.write, wedding.communicate |
| `get_communication_status` | Core | Read | — |
| `get_capabilities` | Core | Read | — |
| `get_proposal_status` | Core | Read | — |
| `prepare_upload` | Core | Review write | — |
| `get_upload_status` | Core | Read | — |
| `apply_budget_batch` | budget | Review write | — |
| `restore_guest` | guests | Review write | — |
| `import_guests` | guests | Review write | — |
| `apply_seating_batch` | seating | Review write | — |
| `update_table` | seating | Review write | — |
| `delete_table` | seating | Review write | — |
| `record_budget_payment` | budget | Review write | — |

Uploads: document 20 MB, Website image 5 MB, Moodboard image 10 MB. Document reads are private literal-search/excerpt operations with sources; they do not claim full-document or semantic reading. Guest and export reads support pagination. Guest imports (200 operations) and Seating batches (500 assignments) are atomic. Payment recording never charges money.

No tool approves a proposal, deletes an Account, charges money, edits credentials, changes subscription or manages Membership/Ownership. Anonymous Letters and Side privacy are preserved. OIDC verified identity needs server key configuration and actual Account email verification; package creation is not public listing approval.
