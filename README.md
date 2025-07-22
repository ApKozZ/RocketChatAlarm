# RocketChatAlarm
This is a program that can automatically send scheduled messages to a specific Rocket.Chat channel. It is only compatible with macOS.

Use your webhook in webhook_url = "".

Use
  launchctl load ~/Library/LaunchAgents/com.example.task.plist
to set timer

  launchctl unload ~/Library/LaunchAgents/com.example.task.plist
to cancle the timer

  launchctl list
to see timers
