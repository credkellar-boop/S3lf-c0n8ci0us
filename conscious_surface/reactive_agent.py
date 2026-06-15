class ReactiveSupervisor:
    def evaluate_output(self, chunk, active_phase):
        # Checks if AI output matches the structural demands of the phase
        if "Phase [Deconstruct]" in active_phase and len(chunk.split()) < 5:
            return "WARNING: Deconstruction phase requires more detail."
        return "PASS"
