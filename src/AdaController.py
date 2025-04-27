class AdaButterworthFilter:
    """
    Dummy implementation of Butterworth filter, will be used later if needed
    a lowpass filter
    """

    def __init__(self):
        return None


class AdaPIDController:

    def __init__(self, kp, ki, kd, iTerm_min=-float(1), iTerm_max=float(1)):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.iTerm = 0
        self.prevError = 0
        self.iTerm_min = iTerm_min
        self.iTerm_max = iTerm_max

    def compute(self, error, dt=1):
        pTerm = self.kp * error
        self.iTerm += self.ki * error * dt

        # Clamp the iTerm
        self.iTerm = max(self.iTerm_min, min(self.iTerm, self.iTerm_max))

        dTerm = self.kd * (error - self.prevError) / dt

        output = pTerm + self.iTerm + dTerm

        self.prevError = error

        return output
