class Joint:
    def __init__(self, name, min_angle, max_angle):
        self.name = name
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.current_angle = 0.0

    def set_angle(self, angle):
        if self.min_angle <= angle <= self.max_angle:
            self.current_angle = angle
            # Send command to actuator (implementation pending)
            print(f"{self.name} angle set to {angle} degrees.")
        else:
            print(f"Angle {angle} out of range for {self.name}.")

# Example usage
if __name__ == "__main__":
    hip_joint = Joint("Hip", -30, 30)
    hip_joint.set_angle(15)
