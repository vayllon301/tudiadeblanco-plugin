# Connector 2.2 capabilities

This catalogue describes the source release. Call `get_capabilities` for the deployed connection. Installing the ZIP does not deploy the server.

Writes apply immediately, except `prepare_upload`, which creates a login-bound upload ticket. Publication and communication scopes are explicit; all operations follow Membership, Role, Module and Side.

| Tool | Module | Effect | Additional scopes |
| --- | --- | --- | --- |
| `get_wedding_overview` | Core | Read | — |
| `get_schedule` | Core | Read | — |
| `list_tasks` | Core | Read | — |
| `create_task` | Core | Write | — |
| `update_task` | Core | Write | — |
| `list_letters` | letters | Read | — |
| `mark_letter_read` | letters | Write | — |
| `list_news_posts` | news | Read | — |
| `draft_news_post` | news | Write | — |
| `list_guests` | guests | Read | — |
| `add_guest` | guests | Write | — |
| `update_guest` | guests | Write | — |
| `archive_guest` | guests | Write | — |
| `get_dietary_report` | dietary | Read | — |
| `get_seating_plan` | seating | Read | — |
| `create_table` | seating | Write | — |
| `assign_guest_to_table` | seating | Write | — |
| `get_budget` | budget | Read | — |
| `add_budget_item` | budget | Write | — |
| `update_budget_item` | budget | Write | — |
| `delete_budget_item` | budget | Write | — |
| `list_note_pages` | Core | Read | — |
| `get_note_page` | Core | Read | — |
| `create_note_page` | Core | Write | — |
| `update_note_page` | Core | Write | — |
| `delete_note_page` | Core | Write | — |
| `delete_task` | Core | Write | — |
| `set_task_options` | Core | Write | — |
| `create_task_list` | Core | Write | — |
| `rename_task_list` | Core | Write | — |
| `delete_task_list` | Core | Write | — |
| `reorder_task_lists` | Core | Write | — |
| `list_task_templates` | Core, Planner only | Read | — |
| `apply_task_template` | Core, Planner only | Write | — |
| `replace_schedule` | Core | Write | wedding.write, wedding.publish |
| `list_menu_items` | dietary | Read | — |
| `create_menu_item` | dietary | Write | — |
| `update_menu_item` | dietary | Write | — |
| `delete_menu_item` | dietary | Write | — |
| `archive_letter` | letters | Write | — |
| `update_news_post` | news | Write | wedding.write, wedding.publish |
| `delete_news_post` | news | Write | wedding.write, wedding.publish |
| `get_wedding_settings` | Core | Read | — |
| `update_wedding_settings` | Core | Write | wedding.write, wedding.publish |
| `export_guests` | guests | Read | — |
| `export_budget` | budget | Read | — |
| `get_invitation_website` | website | Read | — |
| `update_invitation_website` | website | Write | wedding.write, wedding.publish |
| `set_website_published` | website | Write | wedding.write, wedding.publish |
| `get_website_service` | website | Read | — |
| `get_website_slug` | website | Read | — |
| `update_website_slug` | website | Write | wedding.write, wedding.publish |
| `create_story_chapter` | website | Write | wedding.write, wedding.publish |
| `update_story_chapter` | website | Write | wedding.write, wedding.publish |
| `delete_story_chapter` | website | Write | wedding.write, wedding.publish |
| `reorder_story_chapters` | website | Write | wedding.write, wedding.publish |
| `create_faq_item` | website | Write | wedding.write, wedding.publish |
| `update_faq_item` | website | Write | wedding.write, wedding.publish |
| `delete_faq_item` | website | Write | wedding.write, wedding.publish |
| `create_gift_option` | website | Write | wedding.write, wedding.publish |
| `update_gift_option` | website | Write | wedding.write, wedding.publish |
| `delete_gift_option` | website | Write | wedding.write, wedding.publish |
| `reorder_gift_options` | website | Write | wedding.write, wedding.publish |
| `create_gallery_image` | website | Write | wedding.write, wedding.publish |
| `delete_gallery_image` | website | Write | wedding.write, wedding.publish |
| `get_wedding_domain` | domain | Read | — |
| `connect_wedding_domain` | domain, Owner only | Write | wedding.write, wedding.publish |
| `verify_wedding_domain` | domain, Owner only | Write | wedding.write, wedding.publish |
| `disconnect_wedding_domain` | domain, Owner only | Write | wedding.write, wedding.publish |
| `preview_concierge` | chatbot | Read | — |
| `get_concierge_config` | chatbot | Read | — |
| `update_concierge_config` | chatbot | Write | wedding.write, wedding.publish |
| `list_documents` | documents | Read | — |
| `search_documents` | documents | Read | — |
| `read_document_excerpt` | documents | Read | — |
| `update_document_category` | documents | Write | — |
| `delete_document` | documents | Write | — |
| `get_moodboard` | moodboard, Couple only | Read | — |
| `create_moodboard_collection` | moodboard, Couple only | Write | — |
| `rename_moodboard_collection` | moodboard, Couple only | Write | — |
| `delete_moodboard_collection` | moodboard, Couple only | Write | — |
| `create_moodboard_quote` | moodboard, Couple only | Write | — |
| `update_moodboard_clip` | moodboard, Couple only | Write | — |
| `delete_moodboard_clip` | moodboard, Couple only | Write | — |
| `get_invitation_email` | guests | Read | — |
| `update_invitation_email` | guests | Write | wedding.write, wedding.publish |
| `send_invitation_email_test` | guests | Write | wedding.write, wedding.communicate |
| `send_guest_invitations` | guests | Write | wedding.write, wedding.communicate |
| `send_task_reminder` | Core | Write | wedding.write, wedding.communicate |
| `get_communication_status` | Core | Read | — |
| `get_capabilities` | Core | Read | — |
| `get_proposal_status` | Core | Read | — |
| `prepare_upload` | Core | Upload ticket | — |
| `get_upload_status` | Core | Read | — |
| `apply_budget_batch` | budget | Write | — |
| `restore_guest` | guests | Write | — |
| `import_guests` | guests | Write | — |
| `apply_seating_batch` | seating | Write | — |
| `update_table` | seating | Write | — |
| `delete_table` | seating | Write | — |
| `record_budget_payment` | budget | Write | — |

Uploads: document 20 MB, Website image 5 MB, invitation email image 1 MB, Moodboard image 10 MB. Document reads are private literal-search/excerpt operations with sources; they do not claim full-document or semantic reading. Guest and export reads support pagination. Guest imports (200 operations) and Seating batches (500 assignments) are atomic. Payment recording never charges money.

No tool deletes an Account, charges money, edits credentials, changes subscription or manages Membership/Ownership. Planner business material outside the Wedding (Enquiries, Agenda, business tasks, fees, analytics, editing Task templates) stays on the web. Anonymous Letters and Side privacy are preserved. OIDC verified identity needs server key configuration and actual Account email verification; package creation is not public listing approval.
