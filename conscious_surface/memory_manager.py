import cognitive_core

class MemoryManager:
    def __init__(self, capacity=5):
        # Initialize the blazing-fast Rust memory buffer (max 5 items)
        self._rust_buffer = cognitive_core.RustMemoryBuffer(capacity)

    def memorize(self, prompt, response):
        entry = f"User: {prompt}\nAI Engine: {response}"
        self._rust_buffer.add_context(entry)

    def retrieve_context(self):
        return self._rust_buffer.get_full_context()

    def wipe_memory(self):
        self._rust_buffer.clear()
