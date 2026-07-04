from prompts import SYSTEM_PROMPT


class ConversationManager:
  """
  Manages the conversation between the patient and Sarah.
  The conversation is stored in memory and is cleared
  automatically when the program exits. This is a temporary solution for the prototype.
  """

  def __init__(self):
    """Start every conversation with the system prompt."""
    self.messages = [
      {
        "role": "system",
        "content": SYSTEM_PROMPT
      }
    ]

  def add_user_message(self, message: str):
    """Add the patient's message to the conversation."""
    self.messages.append(
      {
        "role": "user",
        "content": message
      }
    )

  def add_assistant_message(self, message: str):
    """Add Sarah's reply to the conversation."""
    self.messages.append(
      {
        "role": "assistant",
        "content": message
      }
    )

  def get_messages(self):
    """Return the complete conversations."""
    return self.messages

  def clear(self):
    """Reset the conversation."""
    self.messages = [
      {
        "role": "system",
        "content": SYSTEM_PROMPT
      }
    ]

   







  
