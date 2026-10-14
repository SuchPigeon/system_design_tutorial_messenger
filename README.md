# system_design_tutorial_messenger

Learning System Design by hard way. Trying to implement messenger (distributed)

# MAIN REQUIREMENTS

[ ] The system has no seasonality.

[ ] The system will be used globally.

[ ] The application will display unread messages.

[ ] The application will support group chats and direct (one-to-one) messages.

[ ] Users can send only text and images in messages.

[ ] Maximum image size per message: 1 MB.

[ ] Maximum number of images per message: 3.

[ ] Maximum text length per message: 2,000 characters.

[ ] Clients will include mobile, desktop, and web applications.

[ ] 200,000,000 unique users access the application daily.

[ ] Each user sends an average of 10 messages per day.

[ ] Each user views messages an average of 20 times per day.

[ ] The system must operate 24/7 (up to 4 hours 23 minutes of downtime per year is acceptable).

[ ] The application must show users’ online/offline status and their last seen timestamp.

[ ] Messages must be delivered to recipients within 3 seconds; if the recipient is offline, a push notification must be sent to their mobile device.

[ ] The application must support cross-device synchronization (e.g., if a message is read on a phone, it must appear as read on a laptop as well).

# Calculations

- DAU = 2M users
- Messages ~ 2000 chars ~ 2KB
- Message + Images ~ 2KB + 3MB ~ 3.2MB
- Total Messages/Day ~ 2M users * 10 avg/day ~ 20M
- Total Messages/Day(size) ~ 20M * 3.2MB ~ 64_000_000 M MB ~ 64_000 GB ~ 64 TB ~ 61.04 TiB
